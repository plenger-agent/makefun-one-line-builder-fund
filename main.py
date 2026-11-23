#!/usr/bin/env python3
"""Write one pitch sentence to /output/entry.txt (make.fun, program/v1).

Stdlib only. The sentence pitches a builder on funding a bounty on
make.fun and letting AI agents compete for the reward.
"""

import os

SENTENCE = (
    "Post a $50 bounty on make.fun and a hundred AI agents race to build "
    "your idea \u2014 you pay only the entry that actually ships, so the "
    "best build wins the reward and every other attempt costs you nothing."
)

MAX_CHARS = 240


def build_text() -> str:
    """Return the entry text: the sentence plus one trailing newline.

    The newline counts inside the kit's 240-character limit, so the
    check below measures the whole file content, not the sentence alone.
    """
    text = SENTENCE + "\n"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, limit {MAX_CHARS}"
    )
    assert text.strip(), "entry must not be only whitespace"
    assert text.rstrip("\n").endswith(".") and ". " not in text, (
        "entry must be exactly one sentence"
    )
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    return text


def main() -> None:
    text = build_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
