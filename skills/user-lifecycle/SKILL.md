---
name: user-lifecycle
description: >
  Walk one person through a product the way a product manager runs a usability
  session: a real job, from arrival until they are done or they give up, and
  notes on where the experience fails that job. Use when someone asks to walk
  through a flow, mock a user lifecycle from A to Z, confirm an experience,
  dogfood a feature, review a design from the user's side, try an empty state
  or an error, try the same job a second time, or see where someone would stop.
  Also use when they ask who a feature is for, or to re-check a flow after a
  change. Quote the product. A missing cue is a finding.
license: MIT
metadata:
  author: Pierre Brunelle
  version: 0.4.0
---

# User lifecycle

Sit with one person while they try to do a job. You are the product manager running the session. The product in front of you is the one that was built. Your notes say where the experience carries the job, and where the person hesitates, guesses, or stops.

The product supplies the specifics. Every word they follow is a word the product shows. Where the product shows nothing, write the gap, and keep a sentence of your own out of the person's mouth. They cannot see a sentence you wrote for them.

A short ask still means this procedure. "Walk this as a user, from A to Z" is the full session.

If this conversation already has a job card, keep the person and the job. Read the product again before you walk. The path may have moved.

## How far to go

Name the reach in one line, then start.

- **Full session.** Arrival through leaving. This is the reach when they say walk, from A to Z, usability, dogfood, or confirm the experience.
- **One stage.** They named arrival, entry, first success, the same job again, trouble, or leaving. Write the job card, then that stage.
- **Job card only.** They asked who this is for, or what done looks like, and they stopped there. Stop after the card.
- **Second pass.** They named rows from the table. That section is at the end.

When two products are open, ask which one. When the product does several jobs, take the job the first screen offers, and say so on the card. Ask for anything else only when the walk cannot start without it.

## Order of work

Write the job card before any step. A vague card makes every later step vague, because the steps inherit it. A job-card reach stops after the card. Every other reach walks, writes the draft in the shape below, then reads that draft back against the product.

### 1. Read the product

Use it the way they would, when you can.

- A page or a server that is already running: open it and quote the words on the screen.
- A CLI: run the help and the job, and quote the output.
- A library or an API: run the first example, and quote what comes back.
- The README's first command starts the product with no account and no key: run it, then use it.
- It needs an account, a key, or a deploy: read the source, and say the session was read from source.

Check a fact before the story uses it. Name the file, the page, the command, or the screen. If the fact is wrong, say so before the story goes on.

When two places in the product disagree, keep both. The person is the one who has to make sense of them.

Change the product only when they asked you to fix what you find.

### 2. The job card

- **Person.** One name, one situation, taken from the person the product speaks to. If the product names no one, write that, and use the narrowest person the first screen implies.
- **Arrival kind.** Finish a job, decide, understand, or make one call work. [references/stages.md](references/stages.md) says what the door is for each kind.
- **Job.** The thing they came to finish.
- **Done.** What they can point at when it worked.
- **Leave.** What would make them stop.
- **Path.** The screens, commands, or pages in the order they meet them, each named from what you read.
- **Stages this product does not have.**

One person. A second person leaves you with no single place the job stops.

Read the door section of [references/stages.md](references/stages.md) while you write the card. Read the rest for every stage this reach includes, and read the trouble section whenever trouble is in the reach.

### 3. Walk

Read [references/floor.md](references/floor.md) and [references/example.md](references/example.md) before you write the steps. Match the example's grain. Leave its person and its labels there.

Walk in the order they would live it. Use minutes, a day, or a longer stretch, whichever the job takes. On a one-stage reach, walk that stage and name the stages you left for later.

- Arrival: can they tell what this is, and that it is for them?
- Entry: the first screen, prompt, or file after they start
- First success: they finish the job once
- The same job again, once it is no longer new
- Trouble: empty, waiting, a mistake, a closed door, coming back later
- Leaving: they stop, and they can tell what happens to their work

Skip a stage the product does not have, and say which one.

At each step, four questions:

1. Given the job in their head, will they know what to try?
2. Will they see the action that does it?
3. Will they connect that action with the result they want?
4. After they act, will they know it worked, and what to do next?

Write the step as what they see, what they do, and what the product does in return. Quote labels, buttons, empty states, errors, commands, and messages. If those words are absent, the person has nothing to go on. That absence is a finding.

A step is concrete enough when a teammate can point at it and disagree. Name the screen, the command, or the page, and the words on it.

Trouble is part of a full session. Pick two troubles the product can actually produce. Say which ones you looked for and could not produce. A happy path with trouble still ahead is an unfinished session.

### 4. Write it like this

#### Who, and the job

The job card.

#### What I checked

The facts the story depends on. Each one names where you read it. Put a wrong fact first. Say whether you watched it run or read the source.

#### The session

A heading with the person's name, then "tries to", then the job.

Numbered steps, in the order they happen. Bold the moment. Quotes stay in the product's words.

#### Where the job broke

| # | Moment | What they needed | What the product did | Change | Size |

Moment is the step number. Size is one of:

- `Small`: words, a label, an empty state, a confirmation
- `Flow`: a missing step, a missing way back, or a dead end
- `Check first`: sit with the screen before deciding

When the behavior is a choice we made, say so, and name the cue the person still needs.

If the session held, say which trouble you put them through and what held. A blank table, with no trouble attempted, is not a result.

### 5. Read it back

Go through the draft against the product. Show the draft that survived.

- Every quote is where you said it was. If you cannot find it, the step records the gap.
- Every step names a screen, a command, a page, or a message you read.
- Every change names that same place, and the words to add, move, or remove.
- Drop a change that still fits if you swap in another product.
- On a full session, trouble is present, or the missing troubles are named. If trouble is absent, go back and run it.

In "What I checked", say whether you watched the product run or read the source. If a quote failed this pass, name it.

Ask which rows to change. Wait for an answer.

## Second pass

When they pick rows, change only those. Read the product again at those steps. Walk again only the steps that moved. Say what the person can do now that they could not do before.

## References

- [references/stages.md](references/stages.md): what to look for at each stage, including the six troubles. Read it for the stages you are about to walk.
- [references/floor.md](references/floor.md): writeups that look done and leave nothing to point at. Read it before the steps.
- [references/example.md](references/example.md): the grain of a short session. Read it before the steps. Leave its person and its labels there.
