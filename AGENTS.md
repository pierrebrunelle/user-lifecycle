# AGENTS.md

This repo is the user-lifecycle plugin: one skill, one subagent, and one slash command. Install with `npx plugins add pierrebrunelle/user-lifecycle` or `npx skills add pierrebrunelle/user-lifecycle`.

## Structure

```
skills/user-lifecycle/
├── SKILL.md                 # the session procedure
├── references/              # stages, floor, example; opened from SKILL.md
└── agents/openai.yaml

commands/walk.md                 # /user-lifecycle:walk
agents/lifecycle-facilitator.md  # runs the session
evals/evals.json                 # prompts and what a good session contains
scripts/validate_plugin.py
```

Manifests: root `plugin.json` (portable), `.plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/`, and `package.json`. Keep the name `user-lifecycle` and the version in sync.

## Rules

- One skill. The session procedure lives in `SKILL.md`. Stage notes live in `references/` and are opened when the procedure says so. The subagent and the command point at `SKILL.md`.
- Keep `SKILL.md` under 500 lines.
- The skill stays generic. The product in front of the agent supplies the screens and the words.
- Run `python3 scripts/validate_plugin.py` after a structural change.
- Bump every version field together, including `metadata.version` in `SKILL.md`.
