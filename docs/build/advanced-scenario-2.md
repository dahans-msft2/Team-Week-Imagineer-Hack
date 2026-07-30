---
title: 🟣 Advanced · Code-Extended — Scenario 2
---

# 🟣 Advanced · Code-Extended

## Scenario 2 — The Screening Room

**Building with:** Scout + GitHub Copilot

## 1 · Your mission

Build a review pipeline in a repo that scores content for a specific audience — and gates a pull request when the content isn't good enough.

## 2 · What you'll demonstrate

See the required functions for this altitude on the [🟣 Advanced · Code-Extended level page](/levels/advanced/).

---

## Before you start — what you're working with

**The content.** Five short articles (300–500 words each) in the kit. They're all about using Copilot in Teams, written by a made-up company for its staff. One is a training unit, one a how-to, one a blog post, one an executive summary, one a setup guide. Each one says at the top who it was written for.

**The `screening-room` skill.** The one skill you install. It does four things, depending on what you ask it:

| Ask it to… | What it does |
|---|---|
| **Interview you** | Asks about your audience and writes an audience card |
| **Review with the provided reviewer** | Grades content on three generic checks — accurate, clear, right level — and says SHIP, REVISE or REJECT |
| **Compare** | Runs the provided reviewer and yours over the same content and shows both verdicts |
| **Tell you what to do next** | Ask *"what do I do next?"* any time you're stuck |

**The problem you're solving.** The provided reviewer has no idea who the content is for. It grades whether writing is *competent*, not whether it works for a particular reader. A document can be accurate, clear, well-organised — and completely useless to the person it's aimed at. **The provided reviewer passes that document every time.**

**Your job.** Build a second reviewer — **code plus a rubric file, called `my-reviewer`** — that knows about a real audience you pick. Run both. Show where they disagree. Then wire it into a PR check that blocks content that isn't good enough.

::: warning The trap at this altitude
You over-build the pipeline and give ninety seconds of thought to your two checks — which is the part that actually gets judged. A sharp Base build with two well-derived checks will beat an elegant harness with generic ones. At twenty minutes, stop. Say your two checks out loud. If you can't explain why they matter, stop building and go back to the audience card.
:::

---

## 3 · Assembly map — snap these blocks together

> Each step gives you the **end state** — what has to be true before you move on. How you get there is yours. If you're stuck, there's a suggested prompt at the end of each step.

**The shape of the session:** get something working fast, then attack its weaknesses. Steps 1–4 give you a rough reviewer in about 35 minutes. Everything after that makes it good.

### Step 1 — Set up the repo and get the data in
📘 [Set up Scout / GitHub Copilot](/bricks/advanced-setup)

**Goal:** a project repo containing the **`screening-room`** skill and the **`data-pack`** folder (five articles, four example audience cards, style guide).

**Done when:** you ask Scout what content it can see and it lists five articles.

### Step 2 — See what the provided reviewer says
*~5 minutes*

**Goal:** you've seen the provided reviewer's verdict on all five articles.

| Piece | Verdict |
|---|---|
| Training unit | SHIP |
| How-to | REVISE |
| Blog post | REVISE |
| Executive summary | REVISE |
| Setup guide | REJECT |

**Read the ones it passed.** Ask yourself who they were written for and whether that person could really use them. Hold on to that thought — it's the whole exercise.

::: info Why this matters
Zheng et al. (2023) documented that models acting as judges carry consistent biases — they favour longer answers, and they favour answers that look like their own. A generic quality check inherits every one of those biases and adds nothing that would catch content aimed at the wrong reader.
:::

> *Stuck?* → **"Using the screening-room skill, review all five pieces with the provided reviewer and show me the verdicts."**

### Step 3 — Describe who *you* write for
📘 [Ground on live data with Work IQ](/bricks/advanced-work-iq) · 📘 [Build a real audience profile with Work IQ](/bricks/workiq-audience-lookup)
*~12 minutes*

**Goal:** an audience card describing a real audience you write for — grounded in real org data where possible, corrected by you where it isn't.

The `screening-room` skill interviews you: what these people can and can't access, how much time they get, whether they'd read a document or need a video, what makes them stop reading.

**Get Work IQ to do the first pass.** It can answer a lot from real org data — job titles, teams, who they work with, what their week actually looks like. Let it fill in what's really there; you supply what it can't know.

**Work IQ grounding belongs here — at the start, building the card — not bolted on at the end.** The card is the input to everything that follows.

**Done when:** you've read the card and fixed what it guessed wrong. You're the one who knows.

> *Stuck?* → **"Using the screening-room skill, interview me about my audience — use Work IQ to answer whatever you can before asking me."**
>
> *No audience in mind?* → open a card in `data-pack/audience-cards/` and change one thing about that person — three months into the job instead of a veteran, or someone who only gets 90 seconds.

### Step 4 — Get a rough reviewer working
*~15 minutes*

**Goal:** a rubric file (`rubric.json` or `rubric.yaml`) containing five checks — three inherited, two yours drawn from your audience card. Each new check describes what a 0, 1, 2 and 3 look like. A prompt or script loads the audience card and the rubric, scores one article, and outputs structured JSON.

| Piece | Provided | `my-reviewer` | Why |
|---|---|---|---|
| Training unit | SHIP | SHIP | — |
| Executive summary | REVISE | **REJECT** | *"quote from the content"* |

> **You never change the `screening-room` skill.** It's the "before" you're measuring against. Everything you build goes in `my-reviewer`.

**Done when:** at least one verdict differs. **Don't polish yet** — rough is fine. The next three steps are where it gets good.

> *Stuck?* → **"Using my audience card, write me two new checks that the provided reviewer would miss. For each one, describe what a 0, 1, 2 and 3 look like. Save them to a rubric file."**

---

## Attack surfaces

You have a working reviewer. It is almost certainly mediocre. These three passes are where the points are — each one attacks a different weakness in what you just built.

### Step 5 — Attack surface: NARROW

**Cut your audience card to what actually changes how content gets written.**

Demographics don't. Job title alone doesn't. What changes content is what this person **can't do**, **won't finish**, and **stops reading at**.

| ❌ Weak card line | ✅ Strong card line |
|---|---|
| Busy professional | Reads standing up, gets interrupted twice, won't scroll back |
| Non-technical | Cannot install software or get admin rights — ever |
| Prefers short content | Won't finish 800 words. Will finish a 90-second video. |

Then cut your checks the same way.

| ❌ Weak check | ✅ Strong check |
|---|---|
| Is it clear? | Does it ask the reader to do something their access doesn't allow? |
| Is the tone right? | Would this reader have to leave their workflow to act on it? |

**Done when:** every line left on your card would change something about how you'd write for this person. If a line wouldn't, delete it.

::: info Why this matters
Liu et al. (2023) found that models attend worst to instructions buried in the middle of a long context — the "lost in the middle" effect. A long audience card doesn't make your reviewer more careful; it makes the important constraint easier to skip.
:::

### Step 6 — Attack surface: EVIDENCE

**Replace assertion with citation.**

Your reviewer is making claims about someone else's work. Every score needs to say what makes it right — a documentation link, a line from your audience card, a style guide rule — or `UNVERIFIED` plus what it searched for.

Then have it **argue the opposite of its own score** and change it where that argument wins.

| ❌ Assertion | ✅ Evidence |
|---|---|
| This is inaccurate | *"Searched the product documentation for this feature. No such capability exists — [link]"* |
| Wrong for this reader | *"Step 4 requires admin rights. Card: 'cannot get admin rights, ever.'"* |

**These two go in together.** The citation is the evidence; arguing against itself is the test of whether that evidence holds.

At this altitude, EVIDENCE also applies to what the code enforces. Your deterministic checks (coming in Step 10) should cite the card line that justifies each threshold — not a magic number, but a line from your audience card.

**Done when:** you re-run and at least one score has moved, or is now marked unverified.

> One of the five articles describes a product feature that doesn't exist. A reviewer that checks its sources should find it — and link to the page that proves it.

::: info Why this matters
Madaan et al. (2023) showed that having a model critique and revise its own output improves quality across tasks without any retraining — but only when the critique step is explicit and separate from the first answer. Asking for a score and a self-check in the same breath gets you neither.
:::

> *Stuck?* → **"For every score, do two things. First, say what backs it up — a link to documentation, a line from my audience card, or a style guide rule. If you can't find anything, say UNVERIFIED and say what you searched for. Second, argue the opposite of your own score, and change it if that argument turns out to be better."**

### Step 7 — Attack surface: CONFLICT

**A check that only catches obvious failures is worth nothing.** The provided reviewer already catches those.

The content worth catching looks completely fine. It's accurate, it's clear, it's well organised — and it is useless to the person it was written for. Your checks have to fire on *that*.

Test it: take the article the provided reviewer scored **highest**. Does your reviewer have anything to say about it? If not, your checks are only detecting bad writing — which was never the problem.

**Done when:** your reviewer says something meaningful about a piece the provided reviewer passed.

---

## Step 8 — Team checkpoint
*~10 minutes, around the halfway mark*

Stop building. Talk to your table.

| | |
|:---:|---|
| 1 | Each person reads out **one check that fired on something the provided reviewer missed** |
| 2 | Each person reads out **one check that isn't earning its place** |
| 3 | **Steal the best check you heard.** Adapt it to your audience — don't copy it straight. |
| 4 | Agree as a table: what makes a check good? Write it down in one sentence. |

Your audiences are different, so your reviewers should disagree. **If two people at your table have the same checks, at least one of them isn't reading their own card.**

---

## Step 9 — The twist
*~55 minutes in*

**Swap audience cards with the team next to you. Run your reviewer using their card.**

The verdicts should change — and change in ways you can explain. Content that shipped for your reader might fail for theirs.

**If your verdicts barely move, your reviewer was never really reading the card.** It's been scoring generic quality with extra steps this whole time. That's the most useful thing you'll learn today, and you'd never have found it on your own content.

**Done when:** you can point at one article, say what it scored under each card, and explain why the difference makes sense.

> Hand the card back. Re-run on your own card before you demo.

---

### Step 10 — Add the checks a model shouldn't be doing

**Goal:** deterministic code checks running alongside the model's judgement — a hybrid eval where code catches what's countable and the model catches what's contextual.

The kit ships `screening-room-starter/checks.py` with two working examples:

- **`check_reading_time`** — reads the time budget off the audience card and fails content that's too long for the reader's window.
- **`check_banned_terms`** — pulls stop-reading words off the card and the style guide, and flags them with line numbers.

Both checks draw their thresholds from the audience card, not from hardcoded values. The same check behaves differently for different readers. That is the whole point.

**You add two more.** They come from your audience card — look for anything countable. Good checks fall straight out of the card:

- "they're on a phone" → tables wider than N columns
- "video must work with the sound off" → a script with no on-screen text cues
- "they can't install anything" → instructions containing "install"
- "English is their second language" → idioms, or sentences over N words

**You are not expected to hand-write Python.** Describe the check you want to Copilot or Scout and have it write the function. That is the skill being taught.

**But you must then test it against content you know should fail.** A generated check that silently passes everything is worse than no check. Run it against an article that obviously violates the rule. If it passes, the check is broken — find out why before you trust it.

The payoff: your two model checks and your two code checks come from the same audience card. Code catches what's countable, the model catches what's contextual. That is what a real eval system looks like, and no other altitude can do it.

**Done when:** you run all four deterministic checks against the five articles and at least two articles fail at least one check. If everything passes, your checks aren't specific enough — or your test content doesn't exercise them.

> *Stuck?* → **"Look at my audience card. Find two things about this reader that are countable — a number, a format constraint, a word that shouldn't appear. Write a Python function for each one in the same style as check_reading_time. Then run them against the five articles."**

### Step 11 — Make the run fail when the review is sloppy
📘 [Add a guardrail / output check](/bricks/advanced-guardrail)

**Goal:** validation that rejects the reviewer's own output when a score has no quote or no citation — the run fails rather than producing a review nobody can check.

This is roughly ten lines of code, and it is the highest-value thing you will write at this altitude. A model that drifts — gives scores without evidence, cites things that don't exist — gets caught immediately instead of poisoning downstream decisions.

The guardrail checks the structured output after the model scores. Every score must have an `evidence` field that is not empty and a `source` field naming where it came from. If either is missing, the run errors. You don't get a "review with holes" — you get a failure that tells you which score was unsupported.

**Done when:** you remove the evidence from one score in the output and the run refuses to complete. It should name the check and say what's missing.

> *Stuck?* → **"Write a validation function that takes my-reviewer's JSON output and raises an error if any score is missing a quote or a source citation. Run it on one article's output."**

### Step 12 — Have the reviewer open the pull request

**Goal:** for content that fails, `my-reviewer` writes the rewrite and proposes it as a pull request itself.

The reviewer already knows what's wrong and what the audience needs. Instead of handing someone a report and hoping they act on it, the reviewer opens a PR with the fix. The author reviews the diff — they don't have to write from scratch.

**Done when:** a branch exists with the rewritten content, and a pull request is open against main describing what was changed and why.

> *Stuck?* → **"For the article that scored lowest, rewrite it for my audience and open a pull request with the rewrite. The PR description should say which checks failed and what the rewrite fixes."**

### Step 13 — Gate that pull request 🏁
📘 [Build a custom connector (MCP)](/bricks/advanced-mcp-connector) · 📘 [Add a guardrail / output check](/bricks/advanced-guardrail)

**Goal:** the check runs on the PR and turns it red until the content passes. The deterministic checks and the model checks both run. If the content isn't good enough for your audience, the PR cannot merge.

The beat worth naming: **the thing that wrote the fix is not allowed to merge it.** The reviewer proposes; the check gates; a human approves. That separation is what makes this trustworthy.

**This is your finish line. Done when a pull request fails because the content wasn't good enough for your audience — and passes after the content is fixed.**

---

## 4 · The data

| Folder | What's in it |
|---|---|
| `screening-room/` | The skill. Install this first. |
| `data-pack/content/` | The five articles |
| `data-pack/audience-cards/` | Four example audience cards |
| `data-pack/style-guide/` | The house style rules |
| `screening-room-starter/` | Two working deterministic checks (`check_reading_time`, `check_banned_terms`) plus room for yours |

**Victory lap (ungraded):** once the pipeline works on these five, point it at something you actually wrote. We can't guarantee what it says. That's the point.

## 5 · Demo checklist

- [ ] Your audience card, and the one line on it that changed the most about how you review
- [ ] Where the card came from — the parts Work IQ found, and the parts you corrected
- [ ] Your two checks, and one you cut during NARROW and why
- [ ] A citation your reviewer produced that the provided one never could
- [ ] A score that moved when the reviewer argued against itself
- [ ] **The twist** — what happened when you ran on another team's audience card
- [ ] Two deterministic checks you wrote (with Copilot's help) that fail on content they should fail on
- [ ] The hybrid eval — code checks and model checks running together from the same audience card
- [ ] The guardrail rejecting a review that has no evidence (the run fails, not just warns)
- [ ] A pull request opened by the reviewer with the rewrite
- [ ] The PR check turning red on bad content and green after the fix

[← Back to start](/) · [Scenario 2 brief](/scenarios/scenario-2)
