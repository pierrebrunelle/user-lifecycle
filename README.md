# user-lifecycle

An agent skill. A product manager sits with one person and walks the job they came to do, from arrival until they finish or give up. The notes say where the experience breaks.

The product in front of the agent supplies the screens, the words, and the path. The skill supplies the session.

```bash
npx skills add pierrebrunelle/user-lifecycle
```

Works in Cursor, Claude Code, Codex, and the other agents the [skills CLI](https://github.com/vercel-labs/skills) supports. Add `-g` to install it for every project.

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

## What you get back

1. The person, the job, and what done looks like.
2. The facts the session depends on, each with where it was read.
3. The session, step by step, in the product's words.
4. A table of where the job broke, and a question about which rows to change.

## License

[MIT](LICENSE)
