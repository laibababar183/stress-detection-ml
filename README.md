# Stress Detection ML App (HRV → Flask → Angular → GitHub CI/CD)

## Problem
3-class classification of stress condition (no stress / interruption / time pressure)
from heart-rate-variability features.

## Model
- Dataset: train.csv + test.csv (410,322 rows), target `condition`
- Input features (in order): MEAN_RR, SDRR, RMSSD
- Pipeline: StandardScaler + DecisionTreeClassifier (max_depth=12), 80/20 stratified split
- Results: Accuracy 0.9011, Precision 0.9005, Recall 0.9011, F1 0.9004
- Linear Regression was compared (F1 0.41) but rejected for classification.

## Versions
Python 3.12, Node (see docs/environment.txt), Angular CLI.

## Setup
    py -3.12 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r backend/requirements.txt
    python notebooks/train_export.py   (needs notebooks/train.csv and test.csv)

## Run locally
Terminal 1: `python backend\app.py`
Terminal 2: `cd frontend` then `ng serve --open --proxy-config proxy.conf.json`

## Tests
    python -m pytest -q backend\tests

## Links
- GitHub: https://github.com/laibababar183/stress-detection-ml
- Pages (static demo): https://laibababar183.github.io/stress-detection-ml/

## Limitations
GitHub Pages hosts only the static Angular UI. Predictions need Flask running locally.
Research/teaching prototype, not a medical or clinical diagnosis.