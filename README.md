# Nemotron Reasoning Challenge: Exploratory Data Analysis

This is the public companion to my work on the [NVIDIA Nemotron Model Reasoning Challenge](https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge) on Kaggle, where the task is to teach a large reasoning model to solve structured logic puzzles reliably.

It sits alongside the rest of my reasoning-model work (see also my ARC-AGI experiments), and it captures the part I think matters most but people usually skip: actually understanding the data before touching a model.

## Why this repo exists

When I pick up a new reasoning benchmark, I do not start by fine-tuning. I start by reading the data until I understand exactly what the model is being asked to do, where the easy wins are, and where the real difficulty is hiding. That habit has saved me more compute than any clever training trick, so I wanted to write it down.

This repo is that first pass: a from-scratch look at the puzzle dataset, the six puzzle families, how their inputs and answers are shaped, and which ones are genuinely hard versus just unfamiliar.

## What is inside

- `notebooks/eda.ipynb` is the high-level walkthrough. It buckets prompts into puzzle families, then charts family counts, answer formats, answer lengths and prompt lengths.
- `notebooks/eda_detailed.ipynb` is the same idea in plain standard-library Python, category by category, plus a look at the test file.
- `scripts/format_data.py` is a small utility that turns the raw CSV puzzles into a clean prompt and answer JSONL, which is the format I use for fine-tuning downstream.
- `scripts/make_synthetic_sample.py` generates a tiny synthetic dataset with the same file structure, using a fixed seed. Not one row of it comes from the competition data.

## Running the notebooks

The competition data cannot be redistributed here, so the notebooks resolve their input in three steps. They first check the `NEMOTRON_DATA_DIR` environment variable for a local copy, then the `/kaggle/input` mount when running on Kaggle, and otherwise they generate the synthetic sample and run on that.

The outputs committed in this repo come from the synthetic fallback, and every chart and table is labeled synthetic sample. So what you see here is the structure of the analysis proven end to end on invented rows. The real distributions and counts only appear when you run the notebooks with the actual dataset from the competition page.

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
