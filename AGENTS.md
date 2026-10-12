# AGENTS.md

This repo is the user-lifecycle plugin: one skill, three subagents, and six slash commands. Install with `npx plugins add pierrebrunelle/user-lifecycle` or `npx skills add pierrebrunelle/user-lifecycle`.

## Structure

```
skills/user-lifecycle/
├── SKILL.md                 # command routing and the shared rules
├── references/              # one file per command, plus the card, the ten questions, stages, floor, example
└── agents/openai.yaml

commands/                    # walk, cast, trouble, research, critic, brief
agents/                      # facilitator, researcher, critic
evals/evals.json             # prompts and what a good result contains
scripts/validate_plugin.py
```

Manifests: root `plugin.json` (portable), `.plugin/plugin.json`, `.cursor-plugin/plugin.json`, `.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/`, and `package.json`. Keep the name `user-lifecycle` and the version in sync.

## Rules

- One skill. `SKILL.md` routes the command. The procedure for that command lives in `references/` and is opened when the router says so. The commands and the subagents point at `SKILL.md`.
- `research` and `critic` leave the product and the job card as they found them.
- Keep `SKILL.md` under 500 lines.
- The skill stays generic. The product in front of the agent supplies the screens and the words.
- Run `python3 scripts/validate_plugin.py` after a structural change.
- Bump every version field together, including `metadata.version` in `SKILL.md`.
