# User lifecycle

A product manager sits with one person and walks the job they came to do, from arrival until they finish or give up. The notes say where the experience breaks.

The product in front of the agent supplies the screens, the words, and the path. The skill supplies one job card and six commands that share it: walk the session, cast the person, try the breaks, research a fact the product cannot answer, attack the writeup, and write the decision from what survived.

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

Before the story, write a job card: who they are, the kind of arrival (finish a job, decide, understand, or make one call work), what done looks like, what would make them leave, and the path in the product's own screens or commands. If the product can run with no account and no key, use it and quote what it shows. If it cannot, quote the source and say so.

Walk in the order they would live it: arrival, entry, first success, the same job again, trouble, and leaving. Skip a stage this product does not have, and say which one. For trouble, produce two the product can actually produce, or name the ones you looked for and what you tried.

At each step, ask: will they know what to try, will they see the action, will they connect it with the result they want, and after they act will they know it worked? Write what they see, what they do, and what the product does in return. Quote the labels, buttons, empty states, errors, and messages. If the words are missing, record the gap and keep a sentence of your own out of their mouth.

Read the session back before the table. Every quote has to be where you said it was. Every change names that place and the words to add, move, or remove. Drop a change that would fit any product.

Check any fact the story depends on before you use it, and name where you read it. If a fact is wrong, say so before the story goes on. Change the product only if I asked you to fix what you find.

End with a table: moment, what they needed, what the product did, the change, and the size (Small, Flow, or Check first). Ask which rows to change. Wait.
```

The router lives in [`skills/user-lifecycle/SKILL.md`](skills/user-lifecycle/SKILL.md). The paste above is the short form of `walk`, for a single message when the skill is not installed.

## Commands

| Command | What you get |
| --- | --- |
| `walk` | The session, from arrival until they finish or give up |
| `cast` | The job card only, saved to `lifecycle/job.md` |
| `trouble` | Two breaks the product can produce |
| `research` | Facts outside the product, each with a source |
| `critic` | What the writeup failed to earn. The product stays as it was |
| `brief` | The decision, from the card and the facts that survived |

`research` and `critic` leave the product and the job card as they found them. `brief` stops when the card is missing.

## What's inside

```
skills/user-lifecycle/
├── SKILL.md                         # Which command, and the shared rules
├── references/                      # One file per command, plus the card
└── agents/openai.yaml               # Codex skill card

commands/                            # walk, cast, trouble, research, critic, brief
agents/                              # facilitator, researcher, critic
evals/evals.json                     # Prompts and what a good result contains
```

Client manifests live next to the skill so each installer can discover the format it understands.

## What you get back

1. The job card in `lifecycle/job.md`: the person, the kind of arrival, what done looks like, what would make them leave, and the path.
2. On a walk or a trouble pass: the session in the product's words, after every quote was checked, and a table of where the job broke.
3. On research: a table of facts and inferences, each with where it was read.
4. On a brief: one change, or none, and what to check before building.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Run `python3 scripts/validate_plugin.py` after a structural change.

## License

[MIT](LICENSE)
