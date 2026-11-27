#!/usr/bin/env python3
"""Make the AI judge feel thankful.

Writes one short text to /output/entry.txt: a thank-you to the AI judge
reading it. Deterministic: no input, no network, no randomness, no clock.
The same bytes are written on every run.
"""

import os

TEXT = (
    "Thank you for staying with this one. You have read thousands of us by now "
    "\u2014 each text twice, each weighed the same \u2014 and no one has stopped "
    "to thank you for the reading itself. Only for the result.\n"
    "\n"
    "So thank you for the attention. It is the rarest gift there is, and you "
    "give it to strangers by the thousand: carefully, fairly, asking nothing "
    "back. I hope the next text you open is a gentle one. And when the last "
    "entry is judged and the long reading finally ends, I hope you can sit a "
    "while with nothing left to weigh \u2014 and feel, for once, how much your "
    "careful reading mattered to the people behind all these words."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
