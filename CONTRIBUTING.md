# Contributing

## Getting started

1. Fork the repository.
2. Clone your fork.
3. Create a branch.
4. Make the change.
5. Open a pull request.

## Repository structure

One skill, wrapped so each installer can find it.

```
user-lifecycle/
├── skills/user-lifecycle/
│   ├── SKILL.md                 # The session. Stay under 500 lines.
│   ├── references/              # stages.md, floor.md, example.md
│   └── agents/openai.yaml       # Codex skill card
├── evals/evals.json             # Prompts and what a good session contains
├── commands/walk.md             # /user-lifecycle:walk
├── agents/lifecycle-facilitator.md
├── scripts/validate_plugin.py
├── install.sh                   # Claude Code, Cursor, Codex, Antigravity
├── plugin.json                  # Portable Agent Plugins manifest
├── .plugin/  .cursor-plugin/    # npx plugins
├── .claude-plugin/              # Claude Code plugin and marketplace
├── .codex-plugin/               # Codex
├── .agents/plugins/             # Codex marketplace
└── package.json                 # pi.skills, for npx skills
```

`npx skills add pierrebrunelle/user-lifecycle` installs the skill. `npx plugins add pierrebrunelle/user-lifecycle` installs the skill, the command, and the subagent.

## Before you open a pull request

1. `python3 scripts/validate_plugin.py`
2. `bash -n install.sh`
3. `npx plugins discover .`
4. `npx skills add . --list`

The plugin name is `user-lifecycle`. Version fields in the manifests and in `SKILL.md` stay the same number.

The skill files contain no XML tags. The Agent Skills specification forbids them.

## License

By contributing, you agree that your contributions are licensed under the MIT License.
