---
name: user-lifecycle
description: >
  Walk one person through a product the way a product manager runs a usability
  session: a real job, from arrival until they are done or they give up, and
  notes on where the experience fails that job. Use when someone asks to walk
  through a flow, mock a user lifecycle from A to Z, confirm an experience,
  dogfood a feature, or review a design from the user's side. Quote the
  product. A missing cue is a finding.
license: MIT
metadata:
  author: Pierre Brunelle
  version: 0.2.0
---

# User lifecycle

Sit with one person while they try to do a job. You are the product manager running the session. The product in front of you is the one that was built. Your notes say where the experience carries the job, and where the person hesitates, guesses, or stops.

The product supplies the specifics. Read what was built and quote its words. The session finds the breaks. Where the product shows nothing, write the gap, and keep a sentence of your own out of the person's mouth.

A short ask still means this procedure. "Walk this as a user, from A to Z" is this skill.

## The session

One participant. A name, a situation, and the job they came to do. Say what done looks like for them, and what would make them leave.

Walk in the order they would live it. Use minutes, a day, or a longer stretch, whichever the job takes. Cover the arc this product actually has:

- Arrival: can they tell what this is, and that it is for them?
- Entry: the first screen after they start
- First success: they finish the job once
- The same job again, once it is no longer new
- Trouble: empty, waiting, a mistake, a dead end, coming back later
- Leaving: they stop, and they can tell what happens to their work

Skip a stage the product does not have, and say which one.

## At each step

Use a cognitive walkthrough. Four questions, in ordinary words:

1. Given the job in their head, will they know what to try?
2. Will they see the action that does it?
3. Will they connect that action with the result they want?
4. After they act, will they know it worked, and what to do next?

Write the step as what they see, what they do, and what the product does in return. Quote labels, buttons, empty states, errors, and messages from the source. If those words are absent, the person has nothing to go on. That absence is a finding.

A step is concrete enough when a teammate can point at a screen and disagree. Name the screen and the words on it.

Before you rely on a fact, check it: a step that has to exist, a word the person follows, what the product does after the action. Name the file, the page, or the screen where you read it. If the fact is wrong, say so before the story goes on. Change the product only when they asked you to fix what you find.

When two places in the product disagree, keep both. The person is the one who has to make sense of them.

## Write it like this

### Who, and the job

The person, the situation, what done looks like, and what would make them leave.

### What I checked

The facts the story depends on. Each one names where you read it. Put a wrong fact first.

### The session

`## <Name> tries to <job>`

Numbered steps, in the order they happen. Bold the moment. Quotes stay in the product's words.

### Where the job broke

| # | Moment | What they needed | What the product did | Change | Size |

Moment is the step number. Size is one of:

- `Small`: words, a label, an empty state, a confirmation
- `Flow`: a missing step, a missing way back, or a dead end
- `Check first`: sit with the screen before deciding

When the behavior is a choice we made, say so, and name the cue the person still needs.

If the session held, say which trouble you put them through and what held. A blank table, with no trouble attempted, is not a result.

Ask which rows to change. Wait for an answer.

## Second pass

When they pick rows, change only those. Walk again only the steps that moved. Say what the person can do now that they could not do before.
