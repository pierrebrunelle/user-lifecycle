#!/usr/bin/env python3
"""Validate the walk-the-job plugin layout. Pure stdlib; no third-party deps.

Checks:
  1. All JSON manifests parse.
  2. Portable and compatibility manifests agree and component pointers resolve.
  3. Every skills/<name>/SKILL.md has name and description frontmatter.
  4. Listed command and agent files exist, and discovered ones have frontmatter.
  5. Versions agree, each skill has agents/openai.yaml, and SKILL.md stays under 500 lines.

Exit non-zero if any check fails.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN_NAME = "walk-the-job"
errors = []
checks = 0


def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        errors.append(msg)


def load_json(rel):
    path = ROOT / rel
    if not path.is_file():
        errors.append(f"missing manifest: {rel}")
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, ValueError) as exc:
        errors.append(f"invalid JSON in {rel}: {exc}")
        return None
    if not isinstance(data, dict):
        errors.append(f"invalid JSON in {rel}: expected an object")
        return None
    return data


def frontmatter(md_path):
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else ""


def main():
    manifests = [
        "plugin.json",
        ".plugin/plugin.json",
        ".cursor-plugin/plugin.json",
        ".claude-plugin/plugin.json",
        ".claude-plugin/marketplace.json",
        ".codex-plugin/plugin.json",
        ".agents/plugins/marketplace.json",
        "package.json",
    ]
    parsed = {rel: load_json(rel) for rel in manifests}

    portable = parsed.get("plugin.json") or {}
    check(
        portable.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "plugin.json: missing Agent Plugins 1.0 schema",
    )
    check(portable.get("name") == PLUGIN_NAME, f"plugin.json: name must be {PLUGIN_NAME!r}")
    openai_extension = ((portable.get("extensions") or {}).get("com.openai") or {})
    codex = parsed.get(".codex-plugin/plugin.json") or {}
    check(
        openai_extension.get("interface") == codex.get("interface"),
        "plugin.json OpenAI interface must match .codex-plugin compatibility metadata",
    )
    check(codex.get("skills") == "./skills/", ".codex-plugin/plugin.json: skills must point to ./skills/")

    marketplace = parsed.get(".agents/plugins/marketplace.json") or {}
    entries = marketplace.get("plugins") or []
    entry = next((item for item in entries if item.get("name") == PLUGIN_NAME), None)
    check(entry is not None, f".agents/plugins/marketplace.json: missing {PLUGIN_NAME} entry")
    if entry is not None:
        source = entry.get("source") or {}
        path = source.get("path")
        check(source.get("source") == "local", "Codex marketplace source must be local")
        check(
            isinstance(path, str) and (ROOT / path).resolve() == ROOT,
            "Codex marketplace path must resolve to plugin root",
        )

    for rel in (".plugin/plugin.json", ".cursor-plugin/plugin.json"):
        data = parsed.get(rel)
        if not data:
            continue
        for key in ("skills", "agents", "commands"):
            if key in data:
                check((ROOT / data[key]).is_dir(), f"{rel}: '{key}' dir not found: {data[key]}")

    skill_files = list((ROOT / "skills").glob("*/SKILL.md"))
    check(len(skill_files) >= 1, "no skills/*/SKILL.md found")
    for skill_file in skill_files:
        matter = frontmatter(skill_file)
        rel = skill_file.relative_to(ROOT)
        check("name:" in matter, f"{rel}: missing 'name' in frontmatter")
        check("description:" in matter, f"{rel}: missing 'description' in frontmatter")

    claude = parsed.get(".claude-plugin/plugin.json") or {}
    for key in ("commands", "agents"):
        for rel in claude.get(key, []):
            check((ROOT / rel).is_file(), f".claude-plugin/plugin.json: {key} file not found: {rel}")

    for command in (ROOT / "commands").glob("*.md"):
        check("description:" in frontmatter(command), f"commands/{command.name}: missing 'description'")
    for agent in (ROOT / "agents").glob("*.md"):
        matter = frontmatter(agent)
        check("name:" in matter, f"agents/{agent.name}: missing 'name'")
        check("description:" in matter, f"agents/{agent.name}: missing 'description'")
        for line in matter.splitlines():
            if line.strip().startswith("tools:"):
                value = line.split(":", 1)[1].strip()
                check(not value.startswith("["), f"agents/{agent.name}: 'tools' must be comma-separated, not a list")

    versions = {}
    version_getters = {
        "plugin.json": lambda data: data.get("version"),
        ".plugin/plugin.json": lambda data: data.get("version"),
        ".cursor-plugin/plugin.json": lambda data: data.get("version"),
        ".claude-plugin/plugin.json": lambda data: data.get("version"),
        ".claude-plugin/marketplace.json": lambda data: (data.get("metadata") or {}).get("version"),
        ".codex-plugin/plugin.json": lambda data: data.get("version"),
        "package.json": lambda data: data.get("version"),
    }
    for rel, getter in version_getters.items():
        data = parsed.get(rel)
        if data is None:
            continue
        version = getter(data)
        check(version is not None, f"{rel}: missing version field")
        if version is not None:
            versions[rel] = version
    for skill_file in skill_files:
        match = re.search(r"^\s*version:\s*(.+?)\s*$", frontmatter(skill_file), re.MULTILINE)
        if match:
            versions[str(skill_file.relative_to(ROOT))] = match.group(1).strip().strip("\"'")
        openai_yaml = skill_file.parent / "agents" / "openai.yaml"
        check(openai_yaml.is_file(), f"{skill_file.parent.relative_to(ROOT)}: missing agents/openai.yaml")
        if openai_yaml.is_file():
            metadata = openai_yaml.read_text(encoding="utf-8", errors="ignore")
            check("display_name:" in metadata, f"{openai_yaml.relative_to(ROOT)}: missing display_name")
            check("short_description:" in metadata, f"{openai_yaml.relative_to(ROOT)}: missing short_description")
        line_count = len(skill_file.read_text(encoding="utf-8", errors="ignore").splitlines())
        check(line_count < 500, f"{skill_file.relative_to(ROOT)}: {line_count} lines, must stay under 500")
        for name in (
            "stages.md",
            "floor.md",
            "example.md",
            "card.md",
            "walk.md",
            "cast.md",
            "trouble.md",
            "research.md",
            "critic.md",
            "brief.md",
            "questions.md",
        ):
            ref = skill_file.parent / "references" / name
            check(ref.is_file(), f"{skill_file.parent.relative_to(ROOT)}: missing references/{name}")
    check(
        len(set(versions.values())) <= 1,
        "version mismatch (all manifests + SKILL.md must match): "
        + "; ".join(f"{key}={value}" for key, value in sorted(versions.items())),
    )

    if errors:
        print(f"FAIL ({len(errors)} of {checks} checks):", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        sys.exit(1)
    print(f"OK: {checks} checks passed ({len(skill_files)} skill(s)).")


if __name__ == "__main__":
    main()
