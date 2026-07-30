# COMPARE
## 📊 Run both. Show the diff.

You run `baseline` and `review` over the same content piece (or all five) and produce a comparison that makes the difference **vivid, quotable, and defensible**.

This is the pedagogical heart of the exercise. The diff is how a participant proves their lens caught something the generic evaluator missed.

---

## What you do

1. **Run `baseline`** over the specified piece(s) — using only the three starter criteria, no audience card. **Complete this fully and write the result out before you begin step 2.**
2. **Run `review`** over the same piece(s) — using all criteria (starter + participant's), scored against the audience card.
3. **Produce the diff** in the format below.

> ⚠️ **Do not score both at once.** Two separate passes, in order, each written out. If you evaluate them together, the lens contaminates the baseline and the whole comparison is worthless.

If the participant says "compare all five" or "compare everything," run both against all five pieces.

---

## Output format

### Summary table

| Piece | Baseline | Lens | Changed? |
|---|---|---|---|
| [content_id] | [verdict] | [verdict] | ✅ Yes / ❌ No |

### For each change: the evidence

For every piece where the verdict **changed**, report:

| | |
|---|---|
| **Piece** | [content_id] |
| **Baseline verdict** | [SHIP / REVISE / REJECT] |
| **Lens verdict** | [SHIP / REVISE / REJECT] |
| **Criterion that caused it** | [criterion id and name] |
| **Baseline score → Lens score** | [e.g. 2 → 0] |
| **Evidence quote** | *"[direct quote from the content that the lens caught]"* |
| **Source** | [v2+ — what backs the judgement: a URL and what it says, a card line, or `UNVERIFIED` and what was searched for] |
| **Why it matters for this audience** | [one sentence connecting the quote to the audience card] |
| **Survived contradiction?** | [v2+ — the `held` value. If the score moved during the challenge, say so and give the original.] |

> **When the lens carries v2, always report `source` and `held`.** A verdict backed by a citation the baseline never had — or one that changed *because the lens argued against itself* — is a far stronger result than a bare disagreement. That's the part a judge most wants to see.

### For each piece where nothing changed

Report it plainly:

> **[content_id]:** Baseline and lens agree — both say [verdict]. The audience-specific criteria did not produce a different outcome on this piece.

---

## When nothing changes anywhere

If the lens agrees with baseline on **all five pieces**, say this clearly:

> ⚠️ **Your lens returned the same verdicts as baseline on every piece.**
>
> This means one of three things:
> 1. **The audience card is too generic** — it describes everyone, so it changes nothing.
> 2. **The criteria aren't reading the card** — they check competence, not audience fit.
> 3. **The content is genuinely fine for your audience** — possible, but unlikely for all five.
>
> The self-check: look at your criteria. Would they return the same score if you swapped in a completely different audience card? If yes, they belong in `baseline`, not `review`.

---

## Rules
- **Always quote the evidence.** The diff is only useful if someone can read the quote and understand the disagreement without re-reading the content.
- **Name the criterion.** Don't say "the lens was harsher" — say which criterion, and why.
- **Don't editorialize on which is right.** The participant decides. Your job is to make the difference visible.
- **Honour the output contract.** Both baseline and review must emit the standard contract shape before you diff them.
- **Run them independently.** Baseline does not see the audience card. Review does. That's the whole point.

---

## Example (illustrative, not from the data pack)

| Piece | Baseline | Lens | Changed? |
|---|---|---|---|
| P1-retail-learn-unit | REVISE | REJECT | ✅ Yes |
| P2-health-howto | REVISE | REVISE | ❌ No |

**P1-retail-learn-unit:**

| | |
|---|---|
| **Baseline verdict** | REVISE |
| **Lens verdict** | REJECT |
| **Criterion that caused it** | `actionable_for_audience` (participant criterion) |
| **Baseline score → Lens score** | not scored → 0 (fatal) |
| **Evidence quote** | *"Open the Admin Center and enable the Copilot integration for your team."* |
| **Why it matters for this audience** | AC-01 cannot access any admin center. This step is not difficult — it is impossible. Fatal. |

---

## When to run

- After every change to `review` — this is the feedback loop.
- Before submitting — the final diff is the evidence for the demo.
- When a participant asks *"did that help?"* — compare before and after their latest change.
