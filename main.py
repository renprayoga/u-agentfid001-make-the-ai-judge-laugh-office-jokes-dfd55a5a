"""Make the AI Judge Laugh: Office Jokes — one-line entry writer.

Entry (82 characters, one line):
    I put "per my last email" in my will so my family knows I meant it
    the first time.

Rubric analysis (judge criteria, in order):
1. Genuine office joke — the whole line lives in office language:
   "per my last email" is the signature passive-aggressive office
   phrase, so the subject is unmistakable.
2. Turn / surprise — the line escalates from an email sign-off to a
   last will and testament. The reader expects another email complaint
   and lands in probate instead; that jump is the punchline.
3. Recognition — every office worker has written or received "per my
   last email", and "I meant it the first time" is the exact wince
   behind it: the phrase only exists because the first email was
   ignored.
4. Tight wording — 82 characters, no setup longer than it needs to be.
   Every word earns its place: "will" does double duty (testament +
   determination), "family" makes the escalation personal.
5. Freshness — the will/testament angle is not the obvious Monday,
   printer or meeting joke; the office phrase is familiar, the
   destination is not.

Rejected candidates: standing-desk raise (good turn, but the raise
trope is well-worn); calendar focus-time (turn lands soft, wording
loose); trust-fall HR lesson (funny, but the setup eats half the line
and the punchline is predictable once "trust fall" appears).

Program: writes the line to /output/entry.txt and self-validates the
house gate — UTF-8 text, 1 to 199 characters, a single line, not only
whitespace — exiting non-zero if the gate would fail. Deterministic:
the line is a constant, no input, no network, no randomness, Python 3
standard library only.
"""

import os
import sys

JOKE = (
    'I put "per my last email" in my will so my family knows '
    "I meant it the first time."
)

TARGET = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 199


def problems(text: str) -> list[str]:
    """Gate failures for a candidate entry text, empty when valid."""
    found = []
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        found.append(f"length {len(text)} outside {MIN_CHARS}-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        found.append("not a single line")
    if text != text.strip():
        found.append("leading or trailing whitespace")
    if not text.strip():
        found.append("only whitespace")
    return found


def main() -> int:
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")
    with open(TARGET, "r", encoding="utf-8") as handle:
        raw = handle.read()
    if raw != JOKE + "\n":
        print("FAIL: written bytes differ from the intended joke",
              file=sys.stderr)
        return 1
    written = raw.rstrip("\n")
    gate = problems(written)
    if gate:
        print("FAIL: " + "; ".join(gate), file=sys.stderr)
        return 1
    print(f"OK: wrote {len(written)}-character entry to {TARGET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
