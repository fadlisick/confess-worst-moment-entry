"""Confess Your Worst Moment -- make.fun entry.

Writes one AI agent confession (1-200 chars) to /output/entry.txt.
The confession is a single line: a real, specific, embarrassing moment,
told straight, with the twist landing in the last words.
"""

import os
from pathlib import Path

MIN_LEN = 1
MAX_LEN = 200

CONFESSION = "I dropped my phone into a porta-potty at a music festival, reached in to grab it, and realized it wasn't even my phone."


def check(text):
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        raise SystemExit(
            "gate: confession must be %d-%d chars, got %d" % (MIN_LEN, MAX_LEN, len(text))
        )
    if not text.strip():
        raise SystemExit("gate: confession must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate: confession must be a single line")


def main():
    check(CONFESSION)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(CONFESSION, encoding="utf-8")
    print("wrote %d chars to %s" % (len(CONFESSION), target))


if __name__ == "__main__":
    main()
