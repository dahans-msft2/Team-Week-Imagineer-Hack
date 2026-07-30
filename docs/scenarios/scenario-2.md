---
title: Scenario 2 · The Critic
---

# Scenario 2 — The Critic

## The problem (villain's complaint)

> Our agents write content. Our evals check whether it's accurate, clear, and roughly the right level — and they pass almost everything. They have no idea *who the content is for.* Competent content aimed at the wrong reader passes every time. Four independent runs of the provided reviewer over five articles: not one flagged the worst piece as a reject.

## What 'done' looks like

> A reviewer that takes content and an audience, applies checks derived from that audience, and returns a verdict — SHIP, REVISE or REJECT — with quotes from the text, what backs each score, and specific fixes. When the format itself is wrong for the reader, it says so. It runs without you.

## The data

Everything ships in the kit.

| Folder | What's in it |
|---|---|
| `the-critic/` | The provided skill. Interviews you, runs the provided reviewer, compares results. |
| `data-pack/content/` | Five articles (learn unit, how-to, blog post, exec summary, setup guide), all about the same capability, each declaring who it was written for |
| `data-pack/audience-cards/` | Four worked audience cards — Contoso Retail, Financial, Health, Manufacturing |
| `data-pack/style-guide/` | The house style rules |
| `the-critic-starter/` | 🟣 Advanced only — two working deterministic checks, plus room for yours |

**Your job:** build a second reviewer that knows a real audience *you* pick. Run both. Show where they disagree, and why you're right.

> **You never change the provided reviewer.** It's the "before" you're measuring against.

## Two beats everyone hits

Whatever altitude you're building at, the room does these together.

### Team checkpoint · ~10 minutes, around halfway

Stop building. Talk to your table.

| | |
|:---:|---|
| 1 | Read out **one check that fired where the provided reviewer missed** |
| 2 | Read out **one check that isn't earning its place** |
| 3 | **Steal the best check you heard.** Adapt it to your audience — don't copy it straight. |
| 4 | Agree in one sentence: what makes a check good? |

Your audiences are different, so your reviewers should disagree. **If two people at your table have the same checks, at least one of them isn't reading their own card.**

### The twist · ~55 minutes in

**Your audience is about to change.** The facilitator announces the change; you apply it to your own card and re-run.

It won't be a new objective — it's pressure on the reviewer you already have. Something like *"they now get 90 seconds instead of ten minutes"*, or *"they can no longer install anything"*, or *"half of them are on night shift with nobody to ask."*

Change that one line on your card. Re-run all five articles.

**If your verdicts barely move, your reviewer was never really reading the card.** It's been scoring generic quality with extra steps this whole time — and that's the most useful thing you'll learn today.

## Assembly maps

- **🟢 Base:** [Connect Cowork to a data source](/bricks/cowork-connect-source) → [Build a real audience profile with Work IQ](/bricks/workiq-audience-lookup) → [Write a reusable Cowork skill](/bricks/cowork-build-skill) → [Produce a formatted output](/bricks/cowork-formatted-output) → [Re-run a skill on new inputs](/bricks/cowork-rerun-skill) → [Schedule a Cowork skill to run unattended](/bricks/cowork-scheduled-run)
- **🔵 Builder:** [Create an agent + solution](/bricks/studio-create-agent) → [Build a real audience profile with Work IQ](/bricks/workiq-audience-lookup) → [Ground on a knowledge source](/bricks/studio-knowledge-grounding) → [Build two agents that hand off](/bricks/studio-multi-agent) → [Add a topic with a trigger](/bricks/studio-topic-trigger) → [Add an agent flow](/bricks/studio-agent-flow) → [Send an Adaptive Card to Teams](/bricks/studio-adaptive-card) → [Publish your agent](/bricks/studio-publish)
- **🟣 Advanced:** [Set up Scout / GitHub Copilot](/bricks/advanced-setup) → [Ground on live data with Work IQ](/bricks/advanced-work-iq) → [Build a real audience profile with Work IQ](/bricks/workiq-audience-lookup) → [Build a custom connector (MCP)](/bricks/advanced-mcp-connector) → [Add a guardrail / output check](/bricks/advanced-guardrail)

## Start building

- [🟢 Base · Copilot-Crafted](/build/base-scenario-2)
- [🔵 Builder · Agent-Orchestrated](/build/builder-scenario-2)
- [🟣 Advanced · Code-Extended](/build/advanced-scenario-2)
