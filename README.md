# Nemotron Reasoning Challenge — Exploratory Data Analysis

Public portfolio companion to my work on the [NVIDIA Nemotron Model Reasoning Challenge](https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge) on Kaggle.

This repo contains my **exploratory data analysis** of the puzzle-reasoning dataset: how the
six puzzle categories are structured, what the inputs and answer formats look like, and how I
approach understanding a new reasoning benchmark before modeling.

## Contents
- `notebooks/eda.ipynb` — high-level walkthrough of the dataset and the six puzzle types
- `notebooks/eda_detailed.ipynb` — deeper category-by-category breakdown
- `scripts/format_data.py` — utility to convert the raw CSV puzzles into a clean prompt/answer JSONL

## Notes
- The competition dataset itself is **not redistributed here** (per Kaggle's rules) — see the
  competition page to download it.
- Modeling code, training recipes, and solution strategy are kept in a private repository.

## About
Applied ML / Cloud engineer building production AI systems. This is part of a portfolio of
hands-on work with reasoning models and structured problem-solving.
