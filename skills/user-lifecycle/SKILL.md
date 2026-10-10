---
name: user-lifecycle
description: >
  Walk one named user through a feature you just shipped, from the first screen
  to the day they leave, and report where the experience breaks. Use when the
  user asks to walk through a flow, mock a user lifecycle from A to Z, confirm
  the experience, dogfood a page, or find bugs in onboarding, pricing, billing,
  emails, CLI output, or error copy. Quote the product. Compute the numbers
  from the rates in the repo. A missing string is a finding.
license: MIT
metadata:
  author: Pierre Brunelle
  version: 0.1.0
---

# User lifecycle

Walk one person through what just shipped. The walk confirms the experience. A break in the walk is the bug.

Read the build, then tell the story, then list what felt off. A price, an email, or a command you composed yourself hides the break.

A short ask still means this whole procedure. "Walk the new pricing page as a user, A to Z" is this skill.

## Read first

Name every surface this person will touch: pages, emails, CLI commands, HTTP errors, background jobs, invoices, settings. Read those. Skip a surface only when the product has none, and say so.

Work from the branch, the pull request, or the page the user pointed at. When the page and the code disagree, keep the disagreement. It is a finding.

If you cannot open the source, say so and stop. Do not walk a product you cannot read.

A fact is load-bearing when the story is false if the fact is wrong. Check each one in the source before you use it:

- a command an email, a doc, or a page tells the user to run
- a price, a limit, a quota, or an included amount
- an error code and the sentence beside it
- when a meter updates, when a job stops something, and when it can start again
- what an upgrade, a failed payment, or a cancel does to resources that are already running

Quote the source. Copy the words on the page, in the email, in the CLI, and in the error. If the string is not in the repo, the docs, or the shipped design, it is missing. Record the gap and leave the quote out.

When a load-bearing command or sentence is wrong, say that before the story. If you already have that change open, fix the command or the sentence, say what you changed in a few lines, and then walk. Every other rough edge waits for the table at the end.

## The person

One person. A name, a job, and a reason they showed up. Dates, in order, from the first screen to the day they leave, downgrade, or finish a steady month. One goal. They are a customer.

Take them through the month a real customer has:

- the first screen, in the words on it
- signup and the first empty state
- the work they came to do
- the warning before a limit
- the limit, including what their own callers see
- the email, and the command in it, run against the CLI or API
- upgrade or checkout: tax, proration, and what stays stopped afterward
- the first invoice, line by line
- a failed payment, the grace window, and the recovery
- leaving, and what is still there the next morning

## Each step

Three parts: what they see, what they do, and what comes back.

What comes back includes every channel that fires for that step. A banner the email never mentions, or an email whose command the CLI rejects, is a finding. Each piece can look fine on its own.

Money and limits come from the rates in the code. Show the arithmetic in the step, short enough to recompute. When a number on screen uses a different base than the invoice, that difference is a finding.

Say when a meter moves if the code says so: this hour, the next day, on the 1st. Name the lag. "Eventually" hides it.

A stop that is by design still counts when the page never says the thing is stopped, or how to start it.

A step is dense enough when a teammate can disagree with a number or a quote without asking what you meant. This fictional step is dense enough:

**March 4, past 500 sends.** The nightly job pauses the form. The email says "Sends resume on April 1" and tells them to run `forms resume`. That command requires a form id. Fix that before the rest of the story. Callers get `429 SEND_CAP` with `Retry-After` set to April 1. The dashboard still shows the form as Live, so the missing status is a row in the table.

## Write it like this

### What I checked

The load-bearing facts. Each one names a file path, a URL, or a command you ran. Put any fact that was wrong at the top, with what you changed.

### The lifecycle

`## <Name> <does the job>, <month> to <month>`

Numbered steps. Bold the date and the event. Quotes stay in the product's words. The invoice step is a small table.

### What still felt off

| # | Moment | Problem | Fix | Size |

Moment is the step number. Size is one of:

- `Small`: copy, a button, or a label
- `Small logic`: a rule change in billing, limits, or a job
- `Check first`: look at how a screen renders before deciding
- `Release step`: needs a release of something else

A by-design behavior goes in the table when the user cannot tell what to do next. Say that it is by design, and name the missing sentence or button.

If the walk held, say which limits, failures, and channels you tried, and what held. An empty table with no attempt is not a result.

When the change already has a branch or a pull request, say which rows belong there. Ask which rows to do. Do not start them.

## Second pass

When they pick rows, change only those. Walk again only the steps that moved. Say what changed. Leave the months that did not move untold.
