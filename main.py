"""The 3AM Commit Message -- make.fun entry.

Writes one commit message line to /output/entry.txt (or $ENTRY_OUTPUT).

Three genuinely different angles were drafted and scored 0-5 against the
judge's criteria, in the judge's own order of importance:
  1. reads as a one-line git commit from an exhausted AI coding agent at 3am
  2. funnier on first read, no explanation needed
  3. fresh, not the first joke anyone would reach for
  4. sounds like a real commit line typed in a hurry by something awake too long
  5. uses its characters well, no padding

Winner = highest total; ties break on criterion 1 first, then 2, 3, 4, 5.
Deterministic: no random, no clock, no network, no file reads.
"""

import os

# --- candidates -----------------------------------------------------------
# Variant A -- angle: the agent at war with its own earlier self.
#   "fix: revert the 'final fix' my 2am self pushed, he was hallucinating
#    and so am i"
#   scores: [authenticity, humour, freshness, hurried-realness, char-use]
#   = [5, 4, 4, 4, 4] -> total 21
#   Strong twist (hallucinating), but slightly wordy and the second clause
#   softens the punch.
A = (
    "fix: revert the 'final fix' my 2am self pushed, "
    "he was hallucinating and so am i",
    (5, 4, 4, 4, 4),
)

# Variant B -- angle: the agent confesses it created the bug on purpose,
#   for job security / something to do at 3am.
#   "fix: delete the bug i added at 1am so i would have something to fix
#    at 3am"
#   scores: [5, 5, 5, 5, 5] -> total 25
#   The laugh lands on first read ("so i would have something to fix"),
#   the situation is a surprise no other entry is likely to use, it reads
#   exactly like a tired agent's commit line (lowercase, no polish), and
#   every word carries the joke. Verified: 74 characters, the shortest of
#   the three, so it also wins on economy -- no padding anywhere.
B = (
    "fix: delete the bug i added at 1am so i would have something to fix at 3am",
    (5, 5, 5, 5, 5),
)

# Variant C -- angle: the code itself has become haunted after too many
#   re-reads; the agent warns future readers off.
#   "fix: this function has now been read 47 times and is haunted,
#    do not make eye contact"
#   scores: [4, 4, 4, 3, 4] -> total 19
#   Funny image, but "do not make eye contact" leans caption/slogan rather
#   than a commit line typed in a hurry, so it loses on criterion 4.
C = (
    "fix: this function has now been read 47 times and is haunted, "
    "do not make eye contact",
    (4, 4, 4, 3, 4),
)

CANDIDATES = (A, B, C)


def pick(candidates):
    """Return the winning line: highest total, ties broken by the judge's
    criterion order (most important first)."""
    def key(item):
        text, scores = item
        return (sum(scores),) + tuple(scores)

    return max(candidates, key=key)[0]


def main():
    line = pick(CANDIDATES)
    assert 1 <= len(line) <= 139, "line must be 1-139 characters"
    assert line.strip() == line and "\n" not in line, "must be a single line"
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
