# User lifecycle

A product manager sits with one person and walks the job they came to do, from arrival until they finish or give up. The notes say where the experience breaks.

The product in front of the agent supplies the screens, the words, and the path. The skill supplies the session.

## Install

### Skill (recommended for most assistants)

Install the portable skill with [npx skills](https://github.com/vercel-labs/skills):

```bash
npx skills add pierrebrunelle/user-lifecycle
```

This installs `SKILL.md` for supported coding assistants, including Cursor, Copilot, Windsurf, Codex, and Antigravity.

Antigravity reads `~/.gemini/antigravity/skills`. Current `npx skills` writes that path when you name the agent:

```bash
npx skills add pierrebrunelle/user-lifecycle --agent antigravity
```

`./install.sh --platform antigravity` copies the same files without npx.

### Full plugin

Install the skill with its command and subagent using [npx plugins](https://www.npmjs.com/package/plugins):

```bash
npx plugins add pierrebrunelle/user-lifecycle
```

Client-native marketplace options:

- **Claude Code:** `/plugin marketplace add pierrebrunelle/user-lifecycle`, then `/plugin install user-lifecycle@user-lifecycle`
- **ChatGPT desktop and Codex:** `codex plugin marketplace add pierrebrunelle/user-lifecycle --ref main`, then `codex plugin add user-lifecycle@user-lifecycle`. Use `/plugins` in Codex or the **Plugins** page in ChatGPT desktop.

Restart or start a new conversation after installing. Repository marketplaces are team-distribution sources. They do not publish to a public directory.

### Any LLM

Paste the skill into context:

[SKILL.md](https://raw.githubusercontent.com/pierrebrunelle/user-lifecycle/main/skills/user-lifecycle/SKILL.md)

## Prompt

Paste this when you want the session in one message:

```text
Run a usability session on what we just built. You are the product manager. One person, one job, from the moment they arrive until they are done or they give up.

Say who they are, what done looks like, and what would make them leave. Walk in the order they would live it: arrival, entry, first success, the same job again, trouble, and leaving. Skip a stage this product does not have, and say which one.

At each step, ask: will they know what to try, will they see the action, will they connect it with the result they want, and after they act will they know it worked? Write what they see, what they do, and what the product does in return. Quote the labels, buttons, empty states, errors, and messages from the source. If the words are missing, record the gap and keep a sentence of your own out of their mouth.

Check any fact the story depends on before you use it, and name where you read it. If a fact is wrong, say so before the story goes on. Change the product only if I asked you to fix what you find.

End with a table: moment, what they needed, what the product did, the change, and the size (Small, Flow, or Check first). Ask which rows to change. Wait.
```

The skill in [`skills/user-lifecycle/SKILL.md`](skills/user-lifecycle/SKILL.md) is this prompt, for when the ask is only "walk this as a user, from A to Z."

## What's inside

```
skills/user-lifecycle/
├── SKILL.md                         # The session
└── agents/openai.yaml               # Codex skill card

agents/lifecycle-facilitator.md      # Subagent that runs the session
commands/walk.md                     # /user-lifecycle:walk
```

Client manifests live next to the skill so each installer can discover the format it understands.

## What you get back

1. The person, the job, and what done looks like.
2. The facts the session depends on, each with where it was read.
3. The session, step by step, in the product's words.
4. A table of where the job broke, and a question about which rows to change.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Run `python3 scripts/validate_plugin.py` after a structural change.

## License

[MIT](LICENSE)
