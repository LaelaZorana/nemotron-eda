# Nemotron Reasoning Challenge: Exploratory Data Analysis

This is the public companion to my work on the [NVIDIA Nemotron Model Reasoning Challenge](https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge) on Kaggle, where the task is to teach a large reasoning model to solve structured logic puzzles reliably.

It sits alongside the rest of my reasoning-model work (see also my ARC-AGI experiments), and it captures the part I think matters most but people usually skip: actually understanding the data before touching a model.

## Why this repo exists

When I pick up a new reasoning benchmark, I do not start by fine-tuning. I start by reading the data until I understand exactly what the model is being asked to do, where the easy wins are, and where the real difficulty is hiding. That habit has saved me more compute than any clever training trick, so I wanted to write it down.

This repo is that first pass: a from-scratch look at the puzzle dataset, the six puzzle families, how their inputs and answers are shaped, and which ones are genuinely hard versus just unfamiliar.

## What is inside

- `notebooks/eda.ipynb` is the high-level walkthrough. I go through the dataset the way I would explain it to a teammate: what the puzzles are, how the prompts and answers are formatted, and what I would look at next.
- `notebooks/eda_detailed.ipynb` is the deeper pass, category by category. This is where I break down each puzzle type, look at the answer formats, and form a view on which families reward careful data work and which do not.
- `scripts/format_data.py` is a small utility that turns the raw CSV puzzles into a clean prompt and answer JSONL, which is the format I use for fine-tuning downstream.

## How I work

A few things you will see reflected here that carry across all my projects:

- Evidence over assumption. I try to make every claim something I measured, not something I guessed. When I am unsure, I say so.
- Understand the scoring before the modeling. How a benchmark grades you usually tells you where the points actually are.
- Keep the easy categories easy. A lot of "improvements" break things that already worked without anyone noticing, so I check.

## Notes

- The competition dataset is not redistributed here, in line with Kaggle's rules. You can download it from the competition page.
- The modeling code, training recipes, and competition strategy live in a private repo while the competition is active. This repo is deliberately just the analysis.

## About me

I build and fine-tune AI systems, with a focus on reasoning models and the data and infrastructure around them. More of my work, including content-automation pipelines and my portfolio, is linked from my GitHub profile.
