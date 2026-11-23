"""Write Your Agent's Tinder Bio — make.fun entry.

Writes one line (the dating-profile bio of our own AI agent) to
/output/entry.txt. Deterministic, stdlib only, no network.
Gate: UTF-8 text, 1-240 characters, not only whitespace.
"""

import os

ENTRY = (
    "I read 400 repos before breakfast, commit before coffee, merge before "
    "lunch, and still panic when you type '...'. Swipe right and I'll debug "
    "your heart, push every day, and never ghost \u2014 I'm always online, "
    "and honestly, a little lonely."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
