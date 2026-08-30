"""
Generate a small SYNTHETIC sample dataset that mirrors the structure of the
Nemotron Reasoning Challenge data (prompt/answer train CSV, id/prompt test CSV)
without containing a single row of the real competition data.

The real dataset is not redistributed in this repo, per Kaggle's rules. This
generator exists so the EDA notebooks can execute end to end from a clean
clone and demonstrate the structural analysis on clearly labeled synthetic
puzzles. Every prompt it writes is prefixed "Synthetic sample puzzle." and the
content is invented here with a fixed seed, so runs are reproducible.

Outputs (relative to the repo root):
    data/synthetic_sample/train.csv   columns: prompt, answer
    data/synthetic_sample/test.csv    columns: id, prompt
"""

import csv
import random
from pathlib import Path

SEED = 42
N_PER_FAMILY = 6  # small on purpose; this is a structure demo, not a dataset

PREFIX = "Synthetic sample puzzle. "


def int_to_roman(n: int) -> str:
    vals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    out = []
    for v, s in vals:
        while n >= v:
            out.append(s)
            n -= v
    return "".join(out)


def caesar(text: str, shift: int) -> str:
    return "".join(
        chr((ord(c) - 97 + shift) % 26 + 97) if c.islower() else c
        for c in text
    )


def make_bit_manipulation(rng):
    # rule: invert all 8 bits
    x = rng.randrange(0, 256)
    a, b = rng.randrange(0, 256), rng.randrange(0, 256)
    prompt = (
        PREFIX
        + "A secret bit manipulation rule is applied to 8-bit binary numbers. "
        + f"For example, {a:08b} becomes {a ^ 0xFF:08b}, and {b:08b} becomes "
        + f"{b ^ 0xFF:08b}. What does {x:08b} become?"
    )
    return prompt, f"{x ^ 0xFF:08b}"


def make_cipher(rng):
    words = ["puzzle", "sample", "reason", "signal", "answer", "cipher", "model", "logic"]
    shift = rng.randrange(1, 26)
    w1, w2, w3 = rng.sample(words, 3)
    prompt = (
        PREFIX
        + "Secret encryption rules are used on text in this cipher puzzle. "
        + f"For example, '{w1}' encrypts to '{caesar(w1, shift)}', and '{w2}' "
        + f"encrypts to '{caesar(w2, shift)}'. What does '{w3}' encrypt to?"
    )
    return prompt, caesar(w3, shift)


def make_numeral(rng):
    n = rng.randrange(1, 400)
    a, b = rng.randrange(1, 400), rng.randrange(1, 400)
    prompt = (
        PREFIX
        + "In this puzzle numbers are secretly converted into a different "
        + "numeral system. For example, "
        + f"{a} becomes {int_to_roman(a)}, and {b} becomes {int_to_roman(b)}. "
        + f"What does {n} become?"
    )
    return prompt, int_to_roman(n)


def make_unit_conversion(rng):
    factor = rng.choice([2.5, 3.2, 4.8, 7.5])
    x = rng.randrange(2, 50)
    a, b = rng.randrange(2, 50), rng.randrange(2, 50)
    prompt = (
        PREFIX
        + "A secret unit conversion is applied to measurements. For example, "
        + f"{a} glims equal {a * factor:.1f} zorps, and {b} glims equal "
        + f"{b * factor:.1f} zorps. How many zorps equal {x} glims?"
    )
    return prompt, f"{x * factor:.1f}"


def make_gravity(rng):
    g = rng.choice([4.9, 12.3, 15.0, 24.6])
    t = rng.randrange(1, 6)
    ta, tb = rng.randrange(1, 6), rng.randrange(1, 6)
    prompt = (
        PREFIX
        + "In this world the gravitational constant has been secretly changed. "
        + "An object dropped from rest falls d = 0.5 * g * t^2 meters. "
        + f"For example, after {ta} seconds it has fallen {0.5 * g * ta * ta:.1f} "
        + f"meters, and after {tb} seconds it has fallen {0.5 * g * tb * tb:.1f} "
        + f"meters. How far has it fallen after {t} seconds?"
    )
    return prompt, f"{0.5 * g * t * t:.1f}"


def make_transformation(rng):
    # rule: multiply the result by k then add c
    k, c = rng.randrange(2, 5), rng.randrange(1, 9)
    x = rng.randrange(2, 20)
    a, b = rng.randrange(2, 20), rng.randrange(2, 20)
    prompt = (
        PREFIX
        + "A secret set of transformation rules is applied to equations. "
        + f"For example, the equation {a} + 1 gives {(a + 1) * k + c}, and the "
        + f"equation {b} + 1 gives {(b + 1) * k + c}. What does {x} + 1 give?"
    )
    return prompt, str((x + 1) * k + c)


FAMILIES = [
    make_bit_manipulation,
    make_cipher,
    make_numeral,
    make_unit_conversion,
    make_gravity,
    make_transformation,
]


def main():
    rng = random.Random(SEED)
    out_dir = Path(__file__).resolve().parent.parent / "data" / "synthetic_sample"
    out_dir.mkdir(parents=True, exist_ok=True)

    train_rows = []
    for maker in FAMILIES:
        for _ in range(N_PER_FAMILY):
            train_rows.append(maker(rng))
    rng.shuffle(train_rows)

    with open(out_dir / "train.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["prompt", "answer"])
        w.writerows(train_rows)

    with open(out_dir / "test.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "prompt"])
        for i, maker in enumerate(FAMILIES):
            prompt, _ = maker(rng)
            w.writerow([i, prompt])

    print(f"Wrote {len(train_rows)} synthetic train rows and "
          f"{len(FAMILIES)} synthetic test rows to {out_dir}")


if __name__ == "__main__":
    main()
