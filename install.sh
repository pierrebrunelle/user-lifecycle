#!/usr/bin/env bash
set -euo pipefail

# User lifecycle skill installer
# Prefer: npx skills add pierrebrunelle/user-lifecycle
# Usage:
#   Interactive:  ./install.sh
#   Direct:       ./install.sh --platform cursor-skill

REPO_URL="https://raw.githubusercontent.com/pierrebrunelle/user-lifecycle/main"

TARGET_DIR=""
PLATFORM=""

usage() {
  cat <<EOF
User lifecycle skill installer

Usage:
  ./install.sh                              Interactive mode
  ./install.sh --platform <name> [--target]  Direct mode

Platforms: claude-code, cursor-skill, codex-skill, antigravity

Options:
  --platform  claude-code, cursor-skill, codex-skill, or antigravity
  --target    Target project directory (defaults to current directory)
  --help      Show this help message
EOF
  exit 0
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --platform) PLATFORM="$2"; shift 2 ;;
    --target)   TARGET_DIR="$2"; shift 2 ;;
    --help)     usage ;;
    *)          echo "Unknown option: $1"; usage ;;
  esac
done

TARGET_DIR="${TARGET_DIR:-.}"

install_skill() {
  local platform="$1"
  local skill_dest

  if [[ "$platform" == "cursor-skill" ]]; then
    skill_dest="$HOME/.cursor/skills/user-lifecycle"
  elif [[ "$platform" == "codex-skill" ]]; then
    skill_dest="$HOME/.agents/skills/user-lifecycle"
  elif [[ "$platform" == "claude-code" ]]; then
    skill_dest="$TARGET_DIR/.claude/skills/user-lifecycle"
  elif [[ "$platform" == "antigravity" ]]; then
    # Antigravity reads ~/.gemini/antigravity/skills, which npx skills does not write.
    skill_dest="$HOME/.gemini/antigravity/skills/user-lifecycle"
  else
    echo "Unknown platform: $platform"
    echo "Available: claude-code, cursor-skill, codex-skill, antigravity"
    exit 1
  fi

  if [[ -d "$skill_dest" ]]; then
    echo "  Directory already exists: $skill_dest"
    read -rp "  Overwrite? [y/N] " answer < /dev/tty
    if [[ ! "$answer" =~ ^[Yy] ]]; then
      echo "  Skipped."
      return
    fi
  fi

  mkdir -p "$skill_dest/agents" "$skill_dest/references"

  local script_dir
  script_dir="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || echo ".")"

  if [[ -f "$script_dir/skills/user-lifecycle/SKILL.md" ]]; then
    cp "$script_dir/skills/user-lifecycle/SKILL.md" "$skill_dest/"
    cp "$script_dir/skills/user-lifecycle/agents/openai.yaml" "$skill_dest/agents/"
    cp "$script_dir/skills/user-lifecycle/references/"*.md "$skill_dest/references/"
  else
    curl -fsSL "$REPO_URL/skills/user-lifecycle/SKILL.md" -o "$skill_dest/SKILL.md"
    curl -fsSL "$REPO_URL/skills/user-lifecycle/agents/openai.yaml" -o "$skill_dest/agents/openai.yaml"
    local ref
    for ref in stages.md floor.md example.md; do
      curl -fsSL "$REPO_URL/skills/user-lifecycle/references/$ref" -o "$skill_dest/references/$ref"
    done
  fi

  echo "  Installed: $skill_dest (SKILL.md, agents/openai.yaml, references/)"
}

if [[ -n "$PLATFORM" ]]; then
  install_skill "$PLATFORM"
  exit 0
fi

if [[ ! -t 0 ]]; then
  echo "Error: Interactive mode requires a terminal."
  echo "Usage: ./install.sh --platform claude-code"
  exit 1
fi

echo ""
echo "User lifecycle skill installer"
echo "=============================="
echo ""
echo "  1) Claude Code"
echo "  2) Cursor (agent skill)"
echo "  3) Codex (standalone skill)"
echo "  4) Antigravity"
echo ""
read -rp "Choice [1-4]: " choice < /dev/tty

case "$choice" in
  1) install_skill "claude-code" ;;
  2) install_skill "cursor-skill" ;;
  3) install_skill "codex-skill" ;;
  4) install_skill "antigravity" ;;
  *) echo "Invalid choice."; exit 1 ;;
esac

echo ""
echo "Done. https://github.com/pierrebrunelle/user-lifecycle"
echo ""
