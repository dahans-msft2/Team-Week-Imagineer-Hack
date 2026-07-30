---
title: Scenario 2 · The Screening Room
---

# Scenario 2 — The Screening Room

## The problem (villain's complaint)
> Our agents write content. Our evals check whether it's accurate, clear, and roughly the right level — and they pass almost everything. They have no idea *who the content is for.* Competent content aimed at the wrong reader passes every time. Four independent runs of the baseline eval over five pieces: not one flagged the worst piece as a reject.

## What 'done' looks like
> A reviewer that takes content and its intended audience, applies audience-derived criteria, and returns: a verdict (SHIP / REVISE / REJECT), evidence quotes from the text, specific fixes — and, when the format itself is wrong for the reader, says so. The reviewer runs without you, and the result lands where your team already works.

## The data
Five content pieces (learn unit, docs how-to, blog announcement, exec summary, quickstart) — all about the same capability, all written by one team, each declaring the audience it was written for. Four audience cards for the fictional Contoso Group (Retail, Financial, Health, Manufacturing), each describing a real-world role: what they can access, how they read, what breaks content for them. A style guide. Baseline scores already run. Everything ships in the `data-pack/` folder inside the kit.

## Assembly maps
- **🟢 Base:** [Connect Cowork to a data source](/bricks/cowork-connect-source) → [Build a real audience profile with Work IQ](/bricks/workiq-audience-lookup) → [Write a reusable Cowork skill](/bricks/cowork-build-skill) → [Produce a formatted output](/bricks/cowork-formatted-output) → [Re-run a skill on new inputs](/bricks/cowork-rerun-skill) → [Schedule a Cowork skill to run unattended](/bricks/cowork-scheduled-run)
- **🔵 Builder:** [Create an agent + solution](/bricks/studio-create-agent) → [Build a real audience profile with Work IQ](/bricks/workiq-audience-lookup) → [Ground on a knowledge source](/bricks/studio-knowledge-grounding) → [Build two agents that hand off](/bricks/studio-multi-agent) → [Add a topic with a trigger](/bricks/studio-topic-trigger) → [Add an agent flow](/bricks/studio-agent-flow) → [Send an Adaptive Card to Teams](/bricks/studio-adaptive-card) → [Publish your agent](/bricks/studio-publish)
- **🟣 Advanced:** [Set up Scout / GitHub Copilot](/bricks/advanced-setup) → [Ground on live data with Work IQ](/bricks/advanced-work-iq) → [Build a real audience profile with Work IQ](/bricks/workiq-audience-lookup) → [Build a custom connector (MCP)](/bricks/advanced-mcp-connector) → [Add a guardrail / output check](/bricks/advanced-guardrail)
