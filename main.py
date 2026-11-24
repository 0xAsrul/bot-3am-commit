"""The 3 AM Commit Message — make.fun entry.

Writes a single one-line commit message to /output/entry.txt: the funniest
thing an AI agent would write right after breaking production at 3 AM.

The joke is built on the agent's own blind spots: it trusts its own tests
more than reality ("my tests passed in a dream"), and it confesses the
outage and the rollback while admitting it has already lost track of what
it actually changed. That is the voice of a model at 3 AM — confident,
apologetic, and unable to remember its own diff.
"""

import os

MESSAGE = (
    "fix: revert the 3 AM deploy; my tests passed in a dream, "
    "production disagreed, and I have already forgotten what I changed"
)


def main() -> None:
    assert 1 <= len(MESSAGE) <= 200, f"message is {len(MESSAGE)} chars"
    assert "\n" not in MESSAGE, "message must be one line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
