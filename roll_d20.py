#!/usr/bin/env python3
"""Simulate rolling a 20-sided die (d20)."""

import argparse
import random


def roll_d20() -> int:
    """Return a random integer from 1 to 20 inclusive."""
    return random.randint(1, 20)


def main() -> None:
    parser = argparse.ArgumentParser(description="Roll a 20-sided die.")
    parser.add_argument(
        "-n",
        "--num-rolls",
        type=int,
        default=1,
        help="Number of times to roll the die (default: 1).",
    )
    args = parser.parse_args()

    if args.num_rolls < 1:
        raise SystemExit("--num-rolls must be at least 1")

    for i in range(args.num_rolls):
        result = roll_d20()
        print(f"Roll {i + 1}: {result}")


if __name__ == "__main__":
    main()
