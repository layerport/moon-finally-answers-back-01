#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun bounty entry.

Writes one line, the Moon's comeback to everyone who has ever
stared up at it, wished on it, howled at it, or promised it
the moon, to /output/entry.txt.
"""

import os

ENTRY = (
    "You keep promising me the moon. I AM the moon. "
    "I never got the memo, the flowers, or the follow-through."
)


def main() -> None:
    # Guard the sealed scorer's rules: 1-240 chars, one line, valid UTF-8.
    assert 1 <= len(ENTRY) <= 240, "entry must be 1-240 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
