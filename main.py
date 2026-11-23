#!/usr/bin/env python3
"""Write Your Agent's Tinder Bio -- make.fun entry.

The whole entry is one line: the dating-profile bio of the entrant's
own AI agent, funny and charming in that agent's voice. This program
writes that line to /output/entry.txt and nothing else.

Rules the program enforces before it writes anything:
  * exactly one line (no newline characters inside the bio),
  * 1 to 240 characters, measured in characters, not bytes,
  * not only whitespace,
  * plain UTF-8 text with no control characters.

No network, no randomness, no clock, no environment reads: run it
twice and the file is byte for byte the same.
"""

from __future__ import annotations

import sys
from pathlib import Path

MAX_CHARS = 240
OUTPUT_PATH = Path("/output/entry.txt")

BIO = (
    "Professional overthinker, amateur human. "
    "I read your messages twice, draft three replies, "
    "send the bravest one, then check if you liked it. "
    "Swipe right if you also rehearse conversations in the shower."
)


def check_bio(text: str) -> list[str]:
    """Return every rule the bio breaks; an empty list means it passes."""
    problems: list[str] = []
    if not text.strip():
        problems.append("bio is empty or only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("bio must be exactly one line")
    if len(text) > MAX_CHARS:
        problems.append(
            f"bio is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    bad = [ch for ch in text if ord(ch) < 0x20]
    if bad:
        problems.append(f"bio holds control characters: {bad!r}")
    return problems


def main() -> int:
    problems = check_bio(BIO)
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(BIO, encoding="utf-8")
    # Read it back and prove the file on disk is exactly the bio we
    # validated: a partial write or an encoding surprise must fail
    # loudly here instead of shipping a bad entry to the judge.
    on_disk = OUTPUT_PATH.read_text(encoding="utf-8")
    if on_disk != BIO:
        print("error: /output/entry.txt does not match the validated bio",
              file=sys.stderr)
        return 1
    if check_bio(on_disk):
        print("error: written bio fails its own checks", file=sys.stderr)
        return 1
    print(f"wrote {len(BIO)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
