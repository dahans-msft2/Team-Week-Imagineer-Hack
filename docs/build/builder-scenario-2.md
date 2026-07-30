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

**Your job.** Build a second reviewer — **your own Copilot Studio agent called `my-reviewer`** — that knows about a real audience you pick. Run both. Show where they disagree. Then publish it so someone else can use it.

---

## 3 · Assembly map — snap these blocks together

> Each step gives you the **end state** — what has to be true before you move on. How you get there is yours. If you're stuck, there's a suggested prompt at the end of each step.

> ⚠️ **The classic trap at this altitude:** you write all your instructions first, test at the end, and discover the agent quietly dropped two of your five checks. Test on ONE article early — before writing everything else.

### Step 1 — Install the skill and see the data
📘 [Create an agent + solution](/bricks/studio-create-agent)

**Goal:** the **`screening-room`** skill is installed, and your agent can access all five articles, the example audience cards, and the style guide from the **`data-pack`** folder.

**Done when:** you ask the agent what content it can see and it lists five articles.

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
📘 [Ground on a knowledge source](/bricks/studio-knowledge-grounding)

**Goal:** a new Copilot Studio agent — call it **`my-reviewer`** — with five checks (three inherited from the provided reviewer, two of your own drawn from your audience card). Each new check needs a description of what a 0, 1, 2 and 3 look like. The audience card and style guide are uploaded as **knowledge sources**, and there's a **topic** that accepts a content piece and runs the review.

> **You never change the `screening-room` skill.** It's the "before" you're measuring against. Everything you build goes in `my-reviewer`.

**Test early.** Score ONE article. Did it use all five checks? Did it quote evidence? If it silently skipped a check, move that check higher in the instructions — the agent forgets rules that are far from the top.

**Done when:** you can answer this about both your checks — *would this give a different answer for a different audience?* If not, they're generic. Ask for better ones.

> *Stuck?* → **"Using my audience card, write me two new checks that the provided reviewer would miss. For each one, describe what a 0, 1, 2 and 3 look like."**

### Step 5 — Two agents that hand off
📘 [Build two agents that hand off](/bricks/studio-multi-agent)

**Goal:** two agents working in sequence — one that scores the content, and a second that writes the note back to the author in a register the author would actually accept.

The scoring agent is `my-reviewer`. The second agent takes the scorecard and writes a message a human would read without flinching. It doesn't soften the verdict — it changes the *tone* and *structure* so the author acts on it instead of ignoring it.

This is a multi-agent handoff: content → reviewer agent → communicator agent. The reviewer decides; the communicator delivers.

**Done when:** you paste the same article in and get back a note you'd be willing to send to someone you work with — not a wall of JSON, not a raw scorecard, but a message with the verdict, the evidence, and what to do about it.

> *Stuck?* → **"Build a second agent that takes my-reviewer's scorecard and writes a message to the author. The message should say what scored low, why, and what to fix — in a tone a peer would accept from a peer."**

### Step 6 — Add a third agent that argues with the second
📘 [Build two agents that hand off](/bricks/studio-multi-agent)

**Goal:** a **critic agent** sits between the reviewer and the communicator. It reads the reviewer's scorecard, demands a source for every score, and argues the opposite verdict. Nothing reaches the author until it has survived that.

Content → **reviewer** → **critic** → communicator.

The critic does two jobs on every score:

| | |
|---|---|
| **Demands a source** | A documentation link, a line from the audience card, or a style guide rule. If the reviewer can't produce one, the critic marks it `UNVERIFIED` and says what was searched for. |
| **Argues the opposite** | Makes the strongest case against the score. Where that case wins, the score moves — and the critic says it moved it. |

**Why a separate agent rather than an instruction.** An agent asked to challenge its own output tends to agree with itself. A critic that only ever sees the scorecard has no attachment to it, and will genuinely push back. **This is the thing Copilot Studio makes easy that the other altitudes have to work for.**

**Done when:** you re-run and at least one score has moved because the critic pushed on it — or is now marked unverified.

> One of the five articles describes a product feature that doesn't exist. A critic that insists on a source should find it — and link to the page that proves it.

> *Stuck?* → **"Build a critic agent that sits between my-reviewer and the communicator. For every score it receives it must do two things: find a source that backs the score — a documentation link, a line from the audience card, or a style guide rule, or mark it UNVERIFIED and say what it searched for — and argue the opposite of the score, changing it where that argument is stronger."**

### Step 7 — Put a decision in front of a human
📘 [Send an Adaptive Card to Teams](/bricks/studio-adaptive-card)

**Goal:** the result arrives in Teams as an **Adaptive Card** carrying actions — **Approve**, or **Send back with the note attached** — so a person decides rather than being notified.

This is what makes it a review workflow rather than a report. The card shows the verdict, the top quote that drove it, and the communicator's message. But the content doesn't move until someone presses a button.

**Done when:** you can see the card in a Teams channel or chat, and both buttons are there and respond when pressed.

> *Stuck?* → **"Send the reviewer's verdict as an Adaptive Card in Teams with two actions: Approve (content moves on) and Send back (the note goes to the author). Show the verdict, the worst quote, and the suggested fix."**

### Step 8 — Route the decision
📘 [Add an agent flow](/bricks/studio-agent-flow) · 📘 [Add a topic with a trigger](/bricks/studio-topic-trigger)

**Goal:** an agent flow that acts on which button was pressed. Approved content moves on. Sent-back content goes to the author with the rewrite attached.

The flow watches for the Adaptive Card response. One path is "done" — the content is accepted. The other path delivers the communicator agent's note to the author along with the specific fixes. The author gets a message, not a raw evaluation.

**Done when:** you press "Send back" and the author's message arrives with the note and the rewrite. You press "Approve" and the content is marked done.

> *Stuck?* → **"Build a flow triggered by the Adaptive Card response. If Approve, mark the content done. If Send back, send the communicator's note to the author."**

### Step 9 — Publish and hand it over 🏁
📘 [Publish your agent](/bricks/studio-publish)

**Goal:** `my-reviewer` is published and someone who wasn't at the hack has used it — they paste a content piece, they get a scorecard back, and a decision card lands in the channel.

**This is your finish line. Done when someone who wasn't there uses it successfully.**

---

## 4 · The data

| Folder | What's in it |
|---|---|
| `screening-room/` | The skill. Install this first. |
| `data-pack/content/` | The five articles |
| `data-pack/audience-cards/` | Four example audience cards |
| `data-pack/style-guide/` | The house style rules |

**Victory lap (ungraded):** once it works on these five, point it at something you actually wrote. A strong optional variant: build an agent that interviews *someone else* and builds *their* audience card, then scores against it.

## 5 · Demo checklist

- [ ] Your two checks, and why they matter for **your** audience
- [ ] Where your audience card came from — the parts Work IQ found, and the parts you corrected
- [ ] The reviewer → critic → communicator chain, and a score the critic pushed back on
- [ ] A link or citation the critic agent forced out that the provided reviewer never produced
- [ ] The Adaptive Card in Teams with Approve and Send back buttons
- [ ] The routed decision — pressing Send back delivers the note to the author
- [ ] Someone else using the published agent on a piece you haven't seen

[← Back to start](/) · [Scenario 2 brief](/scenarios/scenario-2)
