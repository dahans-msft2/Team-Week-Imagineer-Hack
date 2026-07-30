---
name: "the-critic"
description: "Content Health audience-lens evaluator for The Critic hack. Interviews you to build an audience card, evaluates content against a baseline eval and against your own audience lens, diffs the two, and produces adaptation briefs saying what would have to change for a specific reader — including whether the format itself is wrong. Use when the user says the critic, mentions the audience lens, asks to build or extend a content eval, wants content scored for a specific audience or persona, asks what to do next in the hack, or asks whether content lands for a particular reader."
---

# The Critic

The baseline eval knows whether content is good. **It has no idea who it's for.** This skill helps the user teach it — and keep teaching it.

---

## Modes

Pick the mode from what the user asks, load that reference file, and follow it. **Load one at a time.** Do not read all of them up front.

| User says something like | Mode | Load |
|---|---|---|
| *"what do I do next"* · *"am I done"* · *"what do I submit"* | 🧭 **next** | `reference/next.md` |
| *"build my audience card"* · *"interview me"* · *"who is my audience"* | 🎤 **interview** | `reference/interview.md` |
| *"score this"* · *"run the baseline"* · *"what does the old eval say"* | ⚖️ **baseline** | `reference/baseline.md` |
| *"run my lens"* · *"review this for my audience"* | 🔍 **review** | `YOUR-LENS.md` |
| *"compare"* · *"what changed"* · *"diff them"* | 📊 **compare** | `reference/compare.md` |

**If the user's intent is unclear, run `next`.** It is designed to work out where they are and tell them what to do.

---

## The one rule that governs everything

> ### ⛔ Never edit `reference/baseline.md`.
> It is the old evaluator, and it is the user's control group. Everything they build goes in `YOUR-LENS.md`.
>
> This exists so they can prove their lens changed something. It's a before/after — change the baseline as you go and both sides of the comparison move, so nothing can be demonstrated. Keep it untouched and they get to say: *"the old eval said REVISE. Mine says REJECT. Here's the quote."*

If the user asks you to add criteria, add a feature, or improve the evaluator, **that always means `YOUR-LENS.md`.** Say so if it's ambiguous.

---

## Rules that apply in every mode

| | |
|---|---|
| **No quote, no score** | Every score must quote the exact text that justifies it. If you can't quote it, return `INSUFFICIENT_CONTEXT`. |
| **Cite the judgement too** *(v2+)* | Quoting the content shows what you saw. A `source` shows what makes you right — a URL, an audience card line, a style guide rule. If you can't find one, say `UNVERIFIED` and say what you searched for. |
| **The plus** | Any score of 0 or 1 must carry a specific fix — what to change, and where. *"Improve clarity"* is not a fix. |
| **Read the card first** | Score against the declared audience card. Never infer the audience from the content. |
| **Don't invent capabilities** | If a named feature appears nowhere in the material you were given, that is an accuracy problem, not something to assume is real. |

---

## The loop

Every feature the user adds ends the same way:

**add a feature to `YOUR-LENS.md` → re-run all five pieces → `compare` against baseline → refine**

They never know whether a change helped until they re-run it. Push them to re-run.

---

## What they're building toward

Rungs, in order. `reference/next.md` has the detail and the per-path finish lines.

| | Feature | Teaches |
|:---:|---|---|
| v1 | **The lens** — audience card becomes criteria with anchors | Elicitation · artifact→artifact |
| v2 | **Prove your work** — cite the judgement and argue against it, together | Grounding · citation · adversarial prompting |
| v3 | **Adaptation** — rewrite for this audience, in the format they'd finish | Eval → generation loop |
| v4 | **Automate** — it runs without them, result lands where people are | Triggers · unattended runs |
| v5 | **Share** — someone who wasn't there uses it | Reusable artifacts |
| v6 | **Batch** — the whole set in one pass, ranked | Orchestration |
| v7 | **Gate** — nothing ships until it passes | Integration |

**v1–v3 is the assignment.** The finish line depends on their path — `next` knows which.

---

## The self-check to keep repeating

> **If their lens returns the same verdicts as baseline on all five pieces, the audience isn't a real audience.** Either the card is too vague, or the lens isn't reading it.

Say this early and say it again. It's the fastest way for someone to find out their criteria are generic.
