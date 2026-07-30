---
title: 🔵 Builder · Agent-Orchestrated — Scenario 2
---

# 🔵 Builder · Agent-Orchestrated
## Scenario 2 — The Screening Room

**Building with:** Copilot Studio

## 1 · Your mission

Build a published agent that reviews content for a specific audience — then have someone who wasn't at the hack use it.

## 2 · What you'll demonstrate

See the required functions for this altitude on the [🔵 Builder · Agent-Orchestrated level page](/levels/builder/).

---

## 3 · Assembly map — snap these blocks together

Steps 1–4 give you a rough reviewer in about 35 minutes. Everything after that makes it good.

### Step 1 — Install the skill and see the data
📘 [Create an agent + solution](/bricks/studio-create-agent)

**Goal:** the **`screening-room`** skill is installed, and your agent can access all five articles, the example audience cards, and the style guide from the **`data-pack`** folder.

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
📘 [Build a real audience profile with Work IQ](/bricks/workiq-audience-lookup)
*~12 minutes*

**Goal:** an audience card describing a real audience you write for — grounded in real org data where possible, corrected by you where it isn't.

> *Stuck?* → **"Using the screening-room skill, interview me about my audience — use Work IQ to answer whatever you can before asking me."**

### Step 4 — Get a rough reviewer working
📘 [Ground on a knowledge source](/bricks/studio-knowledge-grounding)
*~15 minutes*

**Goal:** a new Copilot Studio agent — call it **`my-reviewer`** — with five checks (three inherited from the provided reviewer, two of your own drawn from your audience card). Each new check needs a description of what a 0, 1, 2 and 3 look like. The audience card and style guide are uploaded as **knowledge sources**, and there's a **topic** that accepts a content piece and runs the review.

| Piece | Provided | `my-reviewer` | Why |
|---|---|---|---|
| Training unit | SHIP | SHIP | — |
| Executive summary | REVISE | **REJECT** | *"quote from the content"* |

> **You never change the `screening-room` skill.** It's the "before" you're measuring against. Everything you build goes in `my-reviewer`.

**Test early.** Score ONE article. Did it use all five checks? If it skipped a check, move that check higher in the instructions.

**Done when:** at least one verdict differs.

> *Stuck?* → **"Write me two new checks that the provided reviewer would miss. For each one, describe what a 0, 1, 2 and 3 look like."**

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

> One of the five articles describes a product feature that doesn't exist. A reviewer that checks its sources should find it.

### Step 7 — Attack surface: CONFLICT

**A check that only catches obvious failures is worth nothing.** The provided reviewer already catches those.

Test it: take the article the provided reviewer scored **highest**. Does your reviewer have anything to say about it? If not, your checks are only detecting bad writing — which was never the problem.

**Done when:** your reviewer says something meaningful about a piece the provided reviewer passed.

---

---

## Steps 8 and 9 — the two shared beats

Around halfway the room stops for a **team checkpoint**, and at ~55 minutes a **twist** lands. Both are on the [Scenario 2 brief](/scenarios/scenario-2#two-beats-everyone-hits).

---

# Step 10 — Two agents that hand off
📘 [Build two agents that hand off](/bricks/studio-multi-agent)

**Goal:** two agents in sequence — `my-reviewer` scores the content, and a communicator agent writes the note back to the author in a register they'd accept. It doesn't soften the verdict — it changes the *tone* so the author acts on it.

**Done when:** you get back a note you'd send to a colleague — verdict, evidence, and what to do about it.

> *Stuck?* → **"Build a second agent that takes my-reviewer's scorecard and writes a message to the author — what scored low, why, and what to fix — in a tone a peer would accept."**

### Step 11 — Add a critic agent that argues with the reviewer
📘 [Build two agents that hand off](/bricks/studio-multi-agent)

**Goal:** a **critic agent** between the reviewer and communicator. It demands a source for every score and argues the opposite verdict. Nothing reaches the author until it has survived that.

Content → **reviewer** → **critic** → communicator.

The critic does two jobs on every score:

| | |
|---|---|
| **Demands a source** | A doc link, a line from the audience card, or a style guide rule — or marks it `UNVERIFIED`. |
| **Argues the opposite** | Makes the strongest case against the score. Where that case wins, the score moves. |

::: warning Instruction drift
An agent asked to challenge its own output tends to agree with itself. A critic that only ever sees the scorecard has no attachment to it. This is what Copilot Studio makes easy that the other altitudes have to work for.
:::

::: info Why this matters
Madaan et al. (2023) showed that self-critique improves quality — but only when the critique step is separate from the first answer.
:::

**Done when:** at least one score has moved because the critic pushed on it — or is now marked unverified.

### Step 12 — Put a decision in front of a human
📘 [Send an Adaptive Card to Teams](/bricks/studio-adaptive-card)

**Goal:** the result arrives in Teams as an **Adaptive Card** with **Approve** and **Send back with the note attached** actions.

**Done when:** both buttons are there and respond when pressed.

### Step 13 — Route the decision
📘 [Add an agent flow](/bricks/studio-agent-flow) · 📘 [Add a topic with a trigger](/bricks/studio-topic-trigger)

**Goal:** an agent flow that acts on which button was pressed. Approved content moves on. Sent-back content goes to the author with the rewrite attached.

**Done when:** "Send back" delivers the note to the author.

### Step 14 — Publish and hand it over 🏁
📘 [Publish your agent](/bricks/studio-publish)

**Goal:** `my-reviewer` is published and someone who wasn't at the hack has used it.

**Done when someone who wasn't there uses it successfully.**

---

## 4 · The data

| Folder | What's in it |
|---|---|
| `screening-room/` | The skill. Install this first. |
| `data-pack/content/` | The five articles |
| `data-pack/audience-cards/` | Four example audience cards |
| `data-pack/style-guide/` | The house style rules |

## 5 · Demo checklist

- [ ] Your audience card, and the one line on it that changed the most about how you review
- [ ] Where the card came from — the parts Work IQ found, and the parts you corrected
- [ ] Your two checks, and one you cut during NARROW and why
- [ ] A citation the critic agent forced out that the provided reviewer never produced
- [ ] A score that moved when the critic argued against itself
- [ ] **The twist** — what happened when you ran on another team's audience card
- [ ] The reviewer → critic → communicator chain running end to end
- [ ] The Adaptive Card in Teams with Approve and Send back buttons
- [ ] The routed decision — pressing Send back delivers the note to the author
- [ ] Someone else using the published agent on a piece you haven't seen

[← Back to start](/) · [Scenario 2 brief](/scenarios/scenario-2)
