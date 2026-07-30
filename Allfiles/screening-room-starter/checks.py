"""
Deterministic checks — the countable half of a hybrid eval.

Two working examples are below. Add two of your own, drawn from your audience card.

You are not expected to hand-write these. Describe the check you want to your
coding assistant and have it write the function — then TEST IT AGAINST CONTENT
YOU KNOW SHOULD FAIL. A check that silently passes everything is worse than no
check at all.

Every check returns:
    (passed: bool, detail: str)

`detail` is what ends up in the reviewer's output, so make it specific enough
to act on. "Too long" is useless. "1,240 words against a 5 minute budget
(~750 words)" is a finding.
"""

import re

WORDS_PER_MINUTE = 150


def check_reading_time(content: str, card: dict):
    """Is this within the time this audience actually has?

    Reads the time budget off the audience card rather than hardcoding it,
    so the same check behaves differently for different readers. That is the
    point — a deterministic check can still be audience-specific.
    """
    minutes = card.get("time_budget_minutes")
    if not minutes:
        return True, "No time budget on the audience card — skipped."

    words = len(content.split())
    budget = minutes * WORDS_PER_MINUTE

    if words > budget:
        over = round((words / budget - 1) * 100)
        return False, (
            f"{words:,} words against a {minutes} minute budget "
            f"(~{budget:,} words). {over}% over."
        )
    return True, f"{words:,} words, within a {minutes} minute budget."


def check_banned_terms(content: str, card: dict):
    """Does it use words this reader stops reading at?

    Pulls the terms from the audience card and the style guide instead of a
    fixed list. A word that is fine for one audience is a wall for another.
    """
    banned = card.get("stop_reading_words", []) + card.get("banned_terms", [])
    if not banned:
        return True, "No banned terms defined for this audience — skipped."

    found = []
    for term in banned:
        for match in re.finditer(rf"\b{re.escape(term)}\b", content, re.IGNORECASE):
            line = content[: match.start()].count("\n") + 1
            found.append(f'"{term}" (line {line})')

    if found:
        return False, "Found: " + ", ".join(found[:5]) + (
            f" and {len(found) - 5} more" if len(found) > 5 else ""
        )
    return True, f"None of the {len(banned)} banned terms appear."


# ─────────────────────────────────────────────────────────────────────
# YOUR CHECKS GO HERE
#
# Two of them, drawn from your audience card. Look for anything on the
# card that is countable — a number, a presence, an absence, a pattern.
#
# Some cards suggest their own:
#   "they're on a phone"                 → tables wider than N columns
#   "video must work with the sound off"  → a script with no on-screen text
#   "never enter patient identifiers"     → identifier-shaped patterns
#   "English is their second language"    → idioms, or sentences over N words
#   "they can't install anything"         → instructions containing "install"
#
# Ask your coding assistant to write it. Then test it on content you KNOW
# should fail. If it passes everything on the first run, it is broken —
# find out why before you trust it.
# ─────────────────────────────────────────────────────────────────────


CHECKS = [
    ("reading_time", check_reading_time),
    ("banned_terms", check_banned_terms),
    # ("your_check", check_your_thing),
]


def run_all(content: str, card: dict):
    """Run every check and return a list of results."""
    return [
        {"check": name, "passed": passed, "detail": detail}
        for name, fn in CHECKS
        for passed, detail in [fn(content, card)]
    ]


if __name__ == "__main__":
    example_card = {
        "time_budget_minutes": 5,
        "stop_reading_words": ["provision", "tenant", "endpoint"],
    }
    example_content = "You will need to provision a tenant before you begin. " * 5

    for result in run_all(example_content, example_card):
        mark = "PASS" if result["passed"] else "FAIL"
        print(f"[{mark}] {result['check']}: {result['detail']}")
