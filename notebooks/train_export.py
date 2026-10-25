from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

ROOT = Path(__file__).resolve().parent.parent
NB = ROOT / "notebooks"

df = pd.concat([pd.read_csv(NB / "train.csv"), pd.read_csv(NB / "test.csv")],
               ignore_index=True).dropna()

FEATURES = ["MEAN_RR", "SDRR", "RMSSD"]
X = df[FEATURES]
y = df["condition"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y)

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", DecisionTreeClassifier(max_depth=12, random_state=42)),
])
pipe.fit(X_train, y_train)

pred = pipe.predict(X_test)
print("Accuracy :", round(accuracy_score(y_test, pred), 4))
print("Precision:", round(precision_score(y_test, pred, average="weighted"), 4))
print("Recall   :", round(recall_score(y_test, pred, average="weighted"), 4))
print("F1-score :", round(f1_score(y_test, pred, average="weighted"), 4))
print("Classes  :", list(pipe.classes_))

bundle = {"pipeline": pipe, "features": FEATURES,
          "task": "classification", "model_version": "1.0"}
(ROOT / "backend/models").mkdir(parents=True, exist_ok=True)
joblib.dump(bundle, ROOT / "backend/models/model_bundle.joblib")

(ROOT / "data").mkdir(exist_ok=True)
X_test.head(1).to_csv(ROOT / "data/sample_inputs.csv", index=False)
print("Saved model_bundle.joblib and data/sample_inputs.csv")