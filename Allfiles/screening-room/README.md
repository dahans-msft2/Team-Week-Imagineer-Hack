# The Screening Room
## Content Health — the audience lens

**One skill. Five modes. Build a reviewer that knows who the content is for.**

---

## What this is

The baseline eval checks whether content is accurate, clear, and pitched at the right level. **It passes almost everything.** It has no idea who the reader is — and competent content aimed at the wrong reader passes every time.

Your job: teach it. Build a lens that knows your audience — their industry, their constraints, how they actually learn — and prove it catches what the baseline cannot.

---

## What's in the folder

| File | | |
|---|---|---|
| `SKILL.md` | The skill itself — routes to a mode, carries the rules | |
| **`YOUR-LENS.md`** | 🔍 **Your work product.** Every feature you add lands here. | ✏️ **you edit this** |
| `reference/next.md` | 🧭 What to do now, whether you're done, what to submit | |
| `reference/interview.md` | 🎤 Asks you questions, writes your audience card | |
| `reference/baseline.md` | ⚖️ The old evaluator — three generic criteria, already scored | ⛔ **never edit** |
| `reference/compare.md` | 📊 Runs both over the same piece, shows where they disagree | |

**You only ever edit one file.** Just talk to the skill for everything else — it loads what it needs.

---

## The one rule

> ### ⛔ Never edit `baseline`. Build yours in `YOUR-LENS.md`, next to it.
>
> It's a before/after. If you change `baseline`, you've moved both sides of the comparison and you can't prove your lens caught anything. Keep it untouched and you get to say: *"the old eval said REVISE. Mine says REJECT. Here's the quote."*

---

## Say this to start

> *"Interview me about my audience."*

That's it. The skill takes it from there. If you're ever unsure, ask **"what do I do next?"**

---

## Install

| Path | Action |
|---|---|
| 🟢 **Base** — Cowork | Drop the `screening-room` folder into your skills. One skill, not five. |
| 🔵 **Builder** — Copilot Studio | `SKILL.md` and `YOUR-LENS.md` become instructions; the `reference/` files and the data pack become knowledge sources |
| 🟣 **Advanced** — Scout · VS Code | Drop the folder in your workspace. Scout picks it up as a skill; or load the files from your own code. |

After install, say **"interview me about my audience"** — or ask **"what do I do next?"** if you'd rather be walked through it.

---

## The loop

```
➕ Add a feature to your lens
    ↓
▶️ Re-run all five pieces
    ↓
📊 compare — what changed, and why?
    ↓
🔧 Refine
    ↓
(back to top)
```

**Every version ends with a re-run and a diff.** That diff is the learning, the evidence, and the demo.

---

## What's in the data pack

| | |
|---|---|
| **5 content pieces** | Learn unit · docs how-to · blog announcement · exec summary · quickstart |
| **4 audience cards** | 🛒 Retail · 🏦 Financial · 🏥 Health · 🏭 Manufacturing |
| **Style guide** | One page — the voice and rules the content was written under |
| **Baseline scores** | Already run. This is the number to beat. |

---

## The build-out — same rungs, three paths

| | Feature | Skill it teaches |
|:---:|---|---|
| **v1** | **The lens** — `interview` writes the card → turn it into criteria with anchors | Elicitation · few-shot · artifact→artifact |
| **v2** | **Self-critique** — *"argue the opposite verdict"*, abstain when unsure | Adversarial prompting · grounding |
| **v3** | **Adaptation** — rewrite for this audience, in the format they'd finish | Closing the eval→generation loop |
| **v4** | **Automate** — runs without you, result lands where people are | Triggers · unattended runs |
| **v5** | **Share** — someone who wasn't here uses it | Reusable artifacts · agents that produce agents |
| **v6** | **Batch** — the whole content set in one pass, ranked | Orchestration · structured output |
| **v7** | **Gate** — nothing ships until it passes | Integration · publish-time blocking |

### Finish lines

| | Finish line | The sentence you get to say |
|---|---|---|
| 🟢 **Base** | v4 — automate | *"It runs every morning and drops a digest in our channel."* |
| 🔵 **Builder** | v5 — publish + flow | *"My teammate used it on Monday and I wasn't in the room."* |
| 🟣 **Advanced** | v7 — the gate | *"A pull request went red because the content wasn't good enough."* |

**v1–v3 is the assignment at every level.** Everything above it is the tail.

---

## Quick reference

| I want to… | Say |
|---|---|
| Know what to do next | `next` |
| Build my audience card | `interview` |
| See how the baseline scores a piece | `baseline` — run it against any piece |
| Score with my lens | `review` — run it against any piece |
| See what my lens changed | `compare` |
| Know if I'm done | `next` — ask "am I done?" |
