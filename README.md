# user-lifecycle

An agent skill. After you build something, the agent walks one user from the first screen to the day they leave, checks that story against the code, and lists the bugs and rough edges.

```bash
npx skills add pierrebrunelle/user-lifecycle
```

Works in Cursor, Claude Code, Codex, and the other agents the [skills CLI](https://github.com/vercel-labs/skills) supports. Add `-g` to install it for every project.

## Prompt

Paste this when you want the walk in one message:

```text
Walk one user through what we just built, from the first screen to the day they leave. Confirm the experience. Report where it breaks.

Before the story, list the facts it depends on and check each one in the code, the copy, and the commands. Check every price, limit, email, error, and any command we tell the user to run. Name the file, page, or command where you read it. If a fact is wrong, say so before the story. If that wrong fact is a command or a sentence the user will follow, and you already have the change open, fix it, then walk. Leave every other issue for the end.

One person, with a name, a job, and dates. At each step say what they see, what they do, and what comes back on every channel that fires: the page, the email, the CLI or API, and the HTTP response their callers get. Quote those words from the source. If the string is not there, record the gap and keep that sentence out of the story.

Use the rates and limits in the repo and show the arithmetic. Take them through a real month: the warning before a limit, the limit itself, paying, a failed payment, and leaving, including what is still stopped the next morning. A stop we chose on purpose still counts when the page never says so.

End with a table: moment (the step), problem, fix, and size (Small, Small logic, Check first, or Release step). Say which rows you would do, and where they would land. Ask. Do not start them.
```

The skill in [`skills/user-lifecycle/SKILL.md`](skills/user-lifecycle/SKILL.md) is this prompt, with the steps an agent needs when the ask is only "walk the new page as a user."

## What you get back

1. The facts it checked, including any command or sentence it had to fix first.
2. A dated lifecycle for one named user, with quotes and arithmetic from the source.
3. A table of what still felt off, each row tied to a step, and a question about which rows to do.

## License

[MIT](LICENSE)
