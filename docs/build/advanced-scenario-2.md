---
title: 🟣 Advanced · Code-Extended — Scenario 2
---

# 🟣 Advanced · Code-Extended

## Scenario 2 — The Critic

**Building with:** Scout + GitHub Copilot

## 1 · Your mission

Build a review pipeline in a repo that scores content for a specific audience — and gates a pull request when the content isn't good enough.

## 2 · What you'll demonstrate

See the required functions for this altitude on the [🟣 Advanced · Code-Extended level page](/levels/advanced/).

---

## 3 · Assembly map — snap these blocks together

Steps 1–4 give you a rough reviewer in about 35 minutes. Everything after that makes it good.

### Step 1 — Set up the repo and get the data in
📘 [Set up Scout / GitHub Copilot](/bricks/advanced-setup)

**Goal:** a project repo containing the **`the-critic`** skill and the **`data-pack`** folder (five articles, four example audience cards, style guide).

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

### Step 3 — Describe who *you* write for
📘 [Ground on live data with Work IQ](/bricks/advanced-work-iq) · 📘 [Build a real audience profile with Work IQ](/bricks/workiq-audience-lookup)
*~12 minutes*

**Goal:** an audience card describing a real audience you write for — grounded in real org data where possible, corrected by you where it isn't.

**Work IQ grounding belongs here — at the start, building the card — not bolted on at the end.**

> *Stuck?* → **"Using the the-critic skill, interview me about my audience — use Work IQ to answer whatever you can before asking me."**

### Step 4 — Get a rough reviewer working
*~15 minutes*

**Goal:** a rubric file (`rubric.json` or `rubric.yaml`) containing five checks — three inherited, two yours drawn from your audience card. Each new check describes what a 0, 1, 2 and 3 look like. A prompt or script loads the audience card and the rubric, scores one article, and outputs structured JSON.

| Piece | Provided | `my-reviewer` | Why |
|---|---|---|---|
| Training unit | SHIP | SHIP | — |
| Executive summary | REVISE | **REJECT** | *"quote from the content"* |

> **You never change the `the-critic` skill.** It's the "before" you're measuring against. Everything you build goes in `my-reviewer`.

**Done when:** at least one verdict differs.

> *Stuck?* → **"Write me two new checks the provided reviewer would miss. For each one, describe what a 0, 1, 2 and 3 look like. Save them to a rubric file."**

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

At this altitude, EVIDENCE also applies to code — your deterministic checks (Step 10) should cite the card line that justifies each threshold.

**Done when:** at least one score has moved, or is now marked unverified.

> One of the five articles describes a product feature that doesn't exist. A reviewer that checks its sources should find it.

::: info Why this matters
Madaan et al. (2023) showed that self-critique improves quality — but only when the critique step is separate from the first answer.
:::

### Step 7 — Attack surface: CONFLICT

**A check that only catches obvious failures is worth nothing.** The provided reviewer already catches those.

Test it: take the article the provided reviewer scored **highest**. Does your reviewer have anything to say about it?

**Done when:** your reviewer says something meaningful about a piece the provided reviewer passed.

---

---

## Steps 8 and 9 — the two shared beats

Around halfway the room stops for a **team checkpoint**, and at ~55 minutes a **twist** lands. Both are on the [Scenario 2 brief](/scenarios/scenario-2#two-beats-everyone-hits).

---

# Step 10 — Add the checks a model shouldn't be doing

**Goal:** deterministic code checks alongside the model's judgement — code catches what's countable, the model catches what's contextual.

The kit ships `the-critic-starter/checks.py` with two working examples:

- **`check_reading_time`** — fails content that exceeds the audience card's time budget.
- **`check_banned_terms`** — flags stop-reading words from the card and style guide.

Both draw thresholds from the audience card, not hardcoded values.

**You add two more.** Look for anything countable on your card:

- "they're on a phone" → tables wider than N columns
- "they can't install anything" → instructions containing "install"

**You are not expected to hand-write Python.** Describe the check to Copilot or Scout. **But test it against content you know should fail.**

**Done when:** at least two articles fail at least one of your four deterministic checks.

> *Stuck?* → **"Find two countable things on my audience card. Write a Python function for each in the style of check_reading_time. Run them against the five articles."**

### Step 11 — Make the run fail when the review is sloppy
📘 [Add a guardrail / output check](/bricks/advanced-guardrail)

**Goal:** validation that rejects the reviewer's output when a score has no quote or no citation — the run fails rather than producing a review nobody can check.

Every score must have a non-empty `evidence` field and a `source` field. Missing either → the run errors.

::: warning Over-building
This is roughly ten lines of code. Do not build a framework.
:::

**Done when:** you remove the evidence from one score and the run refuses to complete.

### Step 12 — Have the reviewer open the pull request

**Goal:** for content that fails, `my-reviewer` writes the rewrite and opens a pull request. The author reviews the diff.

**Done when:** a PR is open against main with the rewrite.

### Step 13 — Gate that pull request 🏁
📘 [Build a custom connector (MCP)](/bricks/advanced-mcp-connector) · 📘 [Add a guardrail / output check](/bricks/advanced-guardrail)

**Goal:** the check runs on the PR and turns it red until the content passes. Deterministic checks and model checks both run.

**The thing that wrote the fix is not allowed to merge it.** The reviewer proposes; the check gates; a human approves.

**Done when a pull request fails because the content wasn't good enough — and passes after the fix.**

---

## 4 · The data

| Folder | What's in it |
|---|---|
| `the-critic/` | The skill. Install this first. |
| `data-pack/content/` | The five articles |
| `data-pack/audience-cards/` | Four example audience cards |
| `data-pack/style-guide/` | The house style rules |
| `the-critic-starter/` | Two working deterministic checks (`check_reading_time`, `check_banned_terms`) plus room for yours |

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
