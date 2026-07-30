---
title: 🟢 Base · Copilot-Crafted — Scenario 2
---

# 🟢 Base · Copilot-Crafted
## Scenario 2 — The Critic

**Building with:** Microsoft 365 Copilot + Cowork

## 1 · Your mission

Build a Cowork skill that reviews content for a specific audience — then set it to run on its own.

## 2 · What you'll demonstrate

See the required functions for this altitude on the [🟢 Base · Copilot-Crafted level page](/levels/base/).

---

## 3 · Assembly map — snap these blocks together

Steps 1–4 give you a rough reviewer in about 35 minutes. Everything after that makes it good.

### Step 1 — Get the files into Cowork
📘 [Connect Cowork to a data source](/bricks/cowork-connect-source)

**Goal:** the **`the-critic`** skill is installed, and Cowork can read all five articles, the example audience cards, and the style guide from the **`data-pack`** folder.

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

**Read the ones it passed.** Ask yourself who they were written for and whether that person could really use them.

::: info Why this matters
Zheng et al. (2023) documented that models acting as judges carry consistent biases — they favour longer answers, and answers that look like their own. A generic quality check adds nothing that would catch content aimed at the wrong reader.
:::

### Step 3 — Describe who *you* write for
📘 [Build a real audience profile with Work IQ](/bricks/workiq-audience-lookup)
*~12 minutes*

**Goal:** an audience card describing a real audience you write for — grounded in real org data where possible, corrected by you where it isn't.

> *Stuck?* → **"Using the the-critic skill, interview me about my audience — use Work IQ to answer whatever you can before asking me."**

### Step 4 — Get a rough reviewer working
📘 [Write a reusable Cowork skill](/bricks/cowork-build-skill) · 📘 [Produce a formatted output](/bricks/cowork-formatted-output)
*~15 minutes*

**Goal:** a skill called **`my-reviewer`** that keeps the provided reviewer's three checks and adds **two of your own** from your audience card — and a table showing both reviewers' verdicts side by side.

| Piece | Provided | `my-reviewer` | Why |
|---|---|---|---|
| Training unit | SHIP | SHIP | — |
| Executive summary | REVISE | **REJECT** | *"quote from the content"* |

> **You never change the `the-critic` skill.** It's the "before" you're measuring against. Everything you build goes in `my-reviewer`.

**Done when:** at least one verdict differs.

> *Stuck?* → **"Write a new Cowork skill called `my-reviewer` with the provided reviewer's three checks plus two of my own from my audience card. Score all five pieces and compare."**

---

## Attack surfaces

### Step 5 — Attack surface: NARROW

**Cut your audience card to what actually changes how content gets written.**

What changes content is what this person **can't do**, **won't finish**, and **stops reading at**.

| ❌ Weak card line | ✅ Strong card line |
|---|---|
| Busy professional | Reads standing up, gets interrupted twice, won't scroll back |
| Non-technical | Cannot install software or get admin rights — ever |

Then cut your checks the same way.

| ❌ Weak check | ✅ Strong check |
|---|---|
| Is it clear? | Does it ask the reader to do something their access doesn't allow? |
| Is the tone right? | Would this reader have to leave their workflow to act on it? |

::: info Why this matters
Liu et al. (2023) found that models attend worst to instructions buried in the middle of a long context — the "lost in the middle" effect. A long audience card doesn't make your reviewer more careful; it makes the important constraint easier to skip.
:::

### Step 6 — Attack surface: EVIDENCE

**Replace assertion with citation.**

Every score needs to say what makes it right — a documentation link, a line from your audience card, a style guide rule — or `UNVERIFIED`. Then have it **argue the opposite of its own score** and change it where that argument wins.

| ❌ Assertion | ✅ Evidence |
|---|---|
| This is inaccurate | *"Searched the product documentation for this feature. No such capability exists — [link]"* |
| Wrong for this reader | *"Step 4 requires admin rights. Card: 'cannot get admin rights, ever.'"* |

**Done when:** at least one score has moved, or is now marked unverified.

> *Stuck?* → **"For every score, cite what backs it up — a doc link, a card line, or a style rule. If nothing, say UNVERIFIED. Then argue the opposite and change it where that argument wins."**

### Step 7 — Attack surface: CONFLICT

**A check that only catches obvious failures is worth nothing.** The provided reviewer already catches those.

Test it: take the article the provided reviewer scored **highest**. Does your reviewer have anything to say about it? If not, your checks are only detecting bad writing — which was never the problem.

**Done when:** your reviewer says something meaningful about a piece the provided reviewer passed.

---

---

## Steps 8 and 9 — the two shared beats

Around halfway the room stops for a **team checkpoint**, and at ~55 minutes a **twist** lands. Both are on the [Scenario 2 brief](/scenarios/scenario-2#two-beats-everyone-hits).

---

# Step 10 — Sweep every audience

**Goal:** all five articles scored against all four example cards *and* yours — around 25 verdicts in one table.

| Article | 🛒 Retail | 🏦 Financial | 🏥 Health | 🏭 Manufacturing |
|---|:---:|:---:|:---:|:---:|
| Executive summary | REJECT | **SHIP** | REVISE | REVISE |
| Setup guide | REJECT | REJECT | REJECT | REJECT |

**Done when:** the same article gets two different verdicts for two different audiences.

### Step 11 — Have `my-reviewer` fix the content, not just grade it

**Goal:** for anything that isn't a SHIP, `my-reviewer` says what would have to change **for your audience** — including changing the format when that's the real problem (a script, not a tidier document).

**Done when:** at least one suggestion changes the *format*, not just the words.

### Step 12 — Set `my-reviewer` loose 🏁
📘 [Re-run a skill on new inputs](/bricks/cowork-rerun-skill) · 📘 [Schedule a Cowork skill to run unattended](/bricks/cowork-scheduled-run)

**Goal:** `my-reviewer` runs on a schedule against a folder of content, and the results land in a chat or channel you set up for this.

::: warning Approval matters
Route the digest to a chat or channel you created for this exercise — not a live team channel, and not an individual colleague. Nothing your reviewer writes should reach a real author without you reading it first.
:::

**Done when it runs tomorrow morning without you.**

## 4 · The data

| Folder | What's in it |
|---|---|
| `the-critic/` | The skill. Install this first. |
| `data-pack/content/` | The five articles |
| `data-pack/audience-cards/` | Four example audience cards |
| `data-pack/style-guide/` | The house style rules |

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
