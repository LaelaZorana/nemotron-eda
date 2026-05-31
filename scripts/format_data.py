"""
Convert train.csv to instruction-tuning format for LoRA fine-tuning.
Outputs: data/train_formatted.jsonl
"""

import csv
import json
import random
from pathlib import Path

SYSTEM_PROMPT = (
    "You are a precise reasoning assistant. Solve the given puzzle step by step, "
    "then place your final answer inside \\boxed{} at the end."
)

def format_example(prompt: str, answer: str) -> dict:
    return {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt.strip()},
            {"role": "assistant", "content": f"The answer is \\boxed{{{answer.strip()}}}"},
        ]
    }

def main():
    data_dir = Path(__file__).parent.parent / "data"
    rows = list(csv.DictReader(open(data_dir / "train.csv")))
    random.seed(42)
    random.shuffle(rows)

    split = int(len(rows) * 0.95)
    train_rows, val_rows = rows[:split], rows[split:]

    for split_name, split_rows in [("train_formatted", train_rows), ("val_formatted", val_rows)]:
        out_path = data_dir / f"{split_name}.jsonl"
        with open(out_path, "w") as f:
            for r in split_rows:
                f.write(json.dumps(format_example(r["prompt"], r["answer"])) + "\n")
        print(f"Wrote {len(split_rows)} examples to {out_path}")

if __name__ == "__main__":
    main()
