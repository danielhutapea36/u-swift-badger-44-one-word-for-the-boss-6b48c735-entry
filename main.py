#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes exactly one word to /output/entry.txt: "Thumbsupper".

The word: the boss whose whole management style is a single thumbs-up
reaction. You send a careful update, a question, a problem — back comes
a lone thumbs-up, and nothing is ever actually decided. Funny because
everyone has met this boss; true because the thumbs-up is doing the job
of an answer, a decision and a performance review all at once.

Deterministic and self-contained: standard library only, no input, no
network, no randomness, no clock. Every run writes the same bytes.
"""

import os

WORD = "Thumbsupper"

# The sealed gate the grader applies to /output/entry.txt: UTF-8 text of
# 1 to 30 characters, not only white space. Refuse to write anything that
# would fail it, so a future word change can never silently ship an
# invalid entry.
MAX_CHARS = 30


def validate(word):
    if not 1 <= len(word) <= MAX_CHARS:
        raise SystemExit("word must be 1 to 30 characters, got %d" % len(word))
    if len(word.split()) != 1:
        raise SystemExit("word must be a single word with no whitespace")
    if not word.strip():
        raise SystemExit("word must not be only white space")
    word.encode("utf-8")


def main():
    validate(WORD)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
