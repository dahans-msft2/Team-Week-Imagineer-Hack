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

### Step 1 — Get the files into Cowork
📘 [Connect Cowork to a data source](/bricks/cowork-connect-source)

**Goal:** the **`screening-room`** skill is installed, and Cowork can read all five articles, the example audience cards, and the style guide from the **`data-pack`** folder.

**Done when:** you ask Cowork what content it can see and it lists five articles.

### Step 2 — See what the provided reviewer says

**Goal:** you've seen the provided reviewer's verdict on all five articles.

You'll get something like this:

| Piece | Verdict |
|---|---|
| Training unit | SHIP |
| How-to | REVISE |
| Blog post | REVISE |
| Executive summary | REVISE |
| Setup guide | REJECT |

**Read the ones it passed.** Ask yourself who they were written for and whether that person could really use them. Hold on to that thought — it's the whole exercise.

> *Stuck?* → **"Using The Screening Room skill, review all five pieces with the provided reviewer and show me the verdicts."**

### Step 3 — Describe who *you* write for
📘 [Build a real audience profile with Work IQ](/bricks/workiq-audience-lookup)

**Goal:** an audience card describing a real audience you write for — grounded in real org data where possible, corrected by you where it isn't.

The `screening-room` skill interviews you: what these people can and can't access, how much time they get, whether they'd read a document or need a video, what makes them stop reading.

**Get Work IQ to do the first pass.** It can answer a lot from real org data — job titles, teams, who they work with, what their week actually looks like. Let it fill in what's really there; you supply what it can't know.

**Done when:** you've read the card and fixed what it guessed wrong. You're the one who knows.

> *Stuck?* → **"Using The Screening Room skill, interview me about my audience — use Work IQ to answer whatever you can before asking me."**
>
> *No audience in mind?* → open a card in `data-pack/audience-cards/` and change one thing about that person — three months into the job instead of a veteran, or someone who only gets 90 seconds.

### Step 4 — Turn your audience into things to check for
📘 [Write a reusable Cowork skill](/bricks/cowork-build-skill)

**Goal:** a new Cowork skill — call it **`my-reviewer`** — that keeps the provided reviewer's three checks and adds **two of your own**, drawn from your audience card. Each new check needs a description of what a 0, 1, 2 and 3 look like.

> **You never change the `screening-room` skill.** It's the "before" you're measuring against. Everything you build goes in `my-reviewer`.

**Done when:** you can answer this about both your checks — *would this give a different answer for a different audience?* If not, they're generic. Ask for better ones.

> *Stuck?* → **"Using my audience card, write me a new Cowork skill called `my-reviewer`. Keep the three checks The Screening Room provided reviewer uses and add two of my own that it would miss. For each new check, describe what a 0, 1, 2 and 3 look like."**

### Step 5 — Sweep every audience
📘 [Produce a formatted output](/bricks/cowork-formatted-output)

**Goal:** the same five articles scored against **all four example audience cards AND yours** — around 25 verdicts in one table.

This is the payoff of Cowork's conversational strengths: you ask once and get a complete cross-audience sweep. No loops, no scripts — one request.

The table you're after looks like this:

| Piece | New hire (IT) | Field tech | Executive | ESL frontline | **Yours** |
|---|---|---|---|---|---|
| Training unit | SHIP | REVISE | REJECT | REVISE | ? |
| How-to | REVISE | SHIP | REJECT | REJECT | ? |
| Blog post | SHIP | REJECT | SHIP | REJECT | ? |

**The point:** the same article SHIPs for one reader and REJECTs for another. That is the whole argument of this exercise in one table. The content didn't change — the audience did. A reviewer that doesn't know the audience can never produce these differences.

**Done when:** you have a table where at least one article has three different verdicts across audiences. If every row is the same, your checks aren't audience-specific enough.

> *Stuck?* → **"Using The Screening Room skill and `my-reviewer`, score all five articles against every audience card in data-pack/audience-cards/ and mine. Show me one table — piece across the top row, audience down the left, verdict in each cell."**

### Step 6 — Make `my-reviewer` prove its work

**Goal:** every score `my-reviewer` gives comes with **what backs it up**, and **an argument against itself.**

A reviewer that says "this is wrong" and can't say why is no better than the one you're replacing. So each score needs a source — a documentation link, a line from your audience card, a style guide rule — or `UNVERIFIED` plus what it searched for. And it should make the strongest case against its own score, changing it when that case wins.

**These two go in together.** The citation is the evidence; arguing against itself is the test of whether that evidence holds. One without the other is half a check.

**Done when:** you re-run it and at least one score has moved, or is now marked unverified.

> One of the five articles describes a product feature that doesn't exist. A reviewer that checks its sources should find it — and link to the page that proves it.

> *Stuck?* → **"For every score, do two things. First, say what backs it up — a link to documentation, a line from my audience card, or a style guide rule. If you can't find anything, say UNVERIFIED and say what you searched for. Second, argue the opposite of your own score, and change it if that argument turns out to be better."**

### Step 7 — Have `my-reviewer` fix the content, not just grade it

**Goal:** for anything that isn't a SHIP, `my-reviewer` says what would have to change **for your audience** — including changing the format when that's the real problem.

If your audience card says they learn from a 90-second video, the right answer is a script. Not a tidier document.

**Done when:** at least one of its suggestions changes the *format*, not just the words.

> *Stuck?* → **"For anything that isn't a SHIP, rewrite it for my audience — in whatever format they'd actually finish."**

### Step 8 — Set `my-reviewer` loose 🏁
📘 [Re-run a skill on new inputs](/bricks/cowork-rerun-skill) · 📘 [Schedule a Cowork skill to run unattended](/bricks/cowork-scheduled-run)

**Goal:** `my-reviewer` runs on a schedule against a folder of content, and the results land in a chat or channel you set up for this.

**This is your finish line. Done when it runs tomorrow morning without you.**

---

## 4 · The data

| Folder | What's in it |
|---|---|
| `screening-room/` | The skill. Install this first. |
| `data-pack/content/` | The five articles |
| `data-pack/audience-cards/` | Four example audience cards |
| `data-pack/style-guide/` | The house style rules |

**Victory lap (ungraded):** once it works on these five, point it at something you actually wrote.

## 5 · Demo checklist

- [ ] Your two checks, and why they matter for **your** audience
- [ ] Where your audience card came from — the parts Work IQ found, and the parts you corrected
- [ ] The cross-audience sweep — the same article getting different verdicts for different readers
- [ ] A link or citation your reviewer found that the provided one never produced
- [ ] A score that changed when the skill argued against itself
- [ ] One article rewritten in a different format (not just different words)
- [ ] The scheduled run arriving without you asking for it

[← Back to start](/) · [Scenario 2 brief](/scenarios/scenario-2)
