import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

# ---------------- LOAD DATASET ----------------
DATASET_PATH = "dataset/health_data.csv"
print(f"Using dataset: {DATASET_PATH}")

df = pd.read_csv(DATASET_PATH)
df.columns = df.columns.str.strip().str.lower()

print("Available columns:", df.columns.tolist())

# ---------------- FEATURES ----------------
FEATURES = [
    "age",
    "height",
    "weight",
    "sleep_hours",
    "exercise_days",
    "junk_food",
    "sugar_intake",
    "screen_time"
]

X = df[FEATURES]

# ---------------- TARGETS ----------------
TARGETS = {
    "cardiac_risk": "cardiac_model.pkl",
    "obesity_risk": "obesity_model.pkl",
    "cancer_risk": "cancer_model.pkl"
}

os.makedirs("model", exist_ok=True)

# ---------------- TRAIN MODELS ----------------
for target, model_file in TARGETS.items():
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Note: Accuracy is just an evaluative measure. Since the dataset is extremely small, we may just train it purely for educational purposes and let it work.
    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"DONE: {target} model trained | Accuracy: {acc:.2f}")

    joblib.dump(model, f"model/{model_file}")

print("All models trained and saved successfully!")
