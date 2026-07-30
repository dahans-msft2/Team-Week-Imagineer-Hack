---
title: 🟢 Base · Copilot-Crafted — Scenario 2
---

# 🟢 Base · Copilot-Crafted
## Scenario 2 — The Screening Room

**Building with:** Microsoft 365 Copilot + Cowork

## 1 · Your mission

Build a Cowork skill that reviews content for a specific audience — then set it to run on its own.

## 2 · What you'll demonstrate

See the required functions for this altitude on the [🟢 Base · Copilot-Crafted level page](/levels/base/).

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

**Your job.** Build a second reviewer — **your own Cowork skill** — that knows about a real audience you pick. Run both. Show where they disagree.

---

## 3 · Assembly map — snap these blocks together

> Each step gives you the **end state** — what has to be true before you move on. How you get there is yours. If you're stuck, there's a suggested prompt at the end of each step.

**The shape of the session:** get something working fast, then attack its weaknesses. Steps 1–4 give you a rough reviewer in about 35 minutes. Everything after that makes it good.

### Step 1 — Get the files into Cowork
📘 [Connect Cowork to a data source](/bricks/cowork-connect-source)

**Goal:** the **`screening-room`** skill is installed, and Cowork can read all five articles, the example audience cards, and the style guide from the **`data-pack`** folder.

**Done when:** you ask Cowork what content it can see and it lists five articles.

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
📘 [Build a real audience profile with Work IQ](/bricks/workiq-audience-lookup)
*~12 minutes*

**Goal:** an audience card describing a real audience you write for — grounded in real org data where possible, corrected by you where it isn't.

**Get Work IQ to do the first pass.** It can answer a lot from real org data — job titles, teams, who they work with, what their week actually looks like. Let it fill in what's really there; you supply what it can't know.

**Done when:** you've read the card and fixed what it guessed wrong. You're the one who knows.

> *Stuck?* → **"Using the screening-room skill, interview me about my audience — use Work IQ to answer whatever you can before asking me."**
>
> *No audience in mind?* → open a card in `data-pack/audience-cards/` and change one thing about that person — three months into the job instead of a veteran, or someone who only gets 90 seconds.

### Step 4 — Get a rough reviewer working
📘 [Write a reusable Cowork skill](/bricks/cowork-build-skill) · 📘 [Produce a formatted output](/bricks/cowork-formatted-output)
*~15 minutes*

**Goal:** a skill called **`my-reviewer`** that keeps the provided reviewer's three checks and adds **two of your own** from your audience card — and a table showing both reviewers' verdicts side by side.

| Piece | Provided | `my-reviewer` | Why |
|---|---|---|---|
| Training unit | SHIP | SHIP | — |
| Executive summary | REVISE | **REJECT** | *"quote from the content"* |

> **You never change the `screening-room` skill.** It's the "before" you're measuring against. Everything you build goes in `my-reviewer`.

**Done when:** at least one verdict differs. **Don't polish yet** — rough is fine. The next three steps are where it gets good.

> *Stuck?* → **"Using my audience card, write me a new Cowork skill called `my-reviewer`. Keep the three checks the provided reviewer uses and add two of my own that it would miss. For each new check, describe what a 0, 1, 2 and 3 look like. Then compare all five pieces against the provided reviewer."**

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

## Step 10 — Sweep every audience

**Goal:** all five articles scored against all four example cards *and* yours — around 25 verdicts in one table.

| Article | 🛒 Retail | 🏦 Financial | 🏥 Health | 🏭 Manufacturing |
|---|:---:|:---:|:---:|:---:|
| Executive summary | REJECT | **SHIP** | REVISE | REVISE |
| Setup guide | REJECT | REJECT | REJECT | REJECT |

**The same article ships for one reader and fails for another.** That's the whole argument of this scenario in one table — and Cowork produces it in a single request while other altitudes have to build for it.

**Done when:** you have a row where the same article gets two different verdicts.

> *Stuck?* → **"Score all five articles against each of the four example audience cards and mine. Show it as one table, articles down the side, audiences across the top."**

### Step 11 — Have `my-reviewer` fix the content, not just grade it

**Goal:** for anything that isn't a SHIP, `my-reviewer` says what would have to change **for your audience** — including changing the format when that's the real problem.

If your audience card says they learn from a 90-second video, the right answer is a script. Not a tidier document.

**Done when:** at least one of its suggestions changes the *format*, not just the words.

> *Stuck?* → **"For anything that isn't a SHIP, rewrite it for my audience — in whatever format they'd actually finish."**

### Step 12 — Set `my-reviewer` loose 🏁
📘 [Re-run a skill on new inputs](/bricks/cowork-rerun-skill) · 📘 [Schedule a Cowork skill to run unattended](/bricks/cowork-scheduled-run)

**Goal:** `my-reviewer` runs on a schedule against a folder of content, and the results land in a chat or channel you set up for this.

::: warning Approval matters
Route the digest to a chat or channel you created for this exercise — not a live team channel, and not an individual colleague. Nothing your reviewer writes should reach a real author without you reading it first.
:::

**This is your finish line. Done when it runs tomorrow morning without you.**

## 4 · The data

| Folder | What's in it |
|---|---|
| `screening-room/` | The skill. Install this first. |
| `data-pack/content/` | The five articles |
| `data-pack/audience-cards/` | Four example audience cards |
| `data-pack/style-guide/` | The house style rules |

**Victory lap (ungraded):** once it works on these five, point it at something you actually wrote.

## 5 · Demo checklist

- [ ] Your audience card, and the one line on it that changed the most about how you review
- [ ] Where the card came from — the parts Work IQ found, and the parts you corrected
- [ ] Your two checks, and one you cut during NARROW and why
- [ ] A citation your reviewer produced that the provided one never could
- [ ] A score that moved when the reviewer argued against itself
- [ ] **The twist** — what happened when you ran on another team's audience card
- [ ] The cross-audience sweep — one article, two different verdicts
- [ ] One article rewritten in a different format (not just different words)
- [ ] The scheduled run arriving without you asking for it

[← Back to start](/) · [Scenario 2 brief](/scenarios/scenario-2)
