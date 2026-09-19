# DSAT Score Analyzer (What-If Analysis)

A Streamlit dashboard for exploring sample Digital SAT results and what-if scenarios using the scoring tables included in this repository.

## Features

- Math and Reading & Writing score summaries
- Module 2 difficulty selection using a fixed Module 1 accuracy threshold
- Topic-level breakdowns
- Scenarios with one, two or three additional correct answers
- CSV export

## Run locally

Run these commands from the repository directory:

```bash
python -m pip install -r requirements.txt
streamlit run main.py
```

Keep `scoring_DSAT_v2.json`, `user_attempt_v2.json` and `user_attempt_v3.json` alongside `main.py`; the application reads these sample inputs.

## Interpretation

This is an exploratory prototype. Scores depend on the supplied lookup table and a fixed routing threshold; they are not an official Digital SAT score prediction. The included attempts are used to demonstrate the analysis workflow.
