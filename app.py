from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# -------- Load trained models if they exist --------
# Ensure we map features in the exact expected 2D shape. Models were trained on 8 features.
try:
    cardiac_model = joblib.load("model/cardiac_model.pkl")
    obesity_model = joblib.load("model/obesity_model.pkl")
    cancer_model = joblib.load("model/cancer_model.pkl")
    MODELS_LOADED = True
except Exception as e:
    MODELS_LOADED = False
    print("Warning: Models not loaded. Please ensure train.py was run.")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if not MODELS_LOADED:
            return "Models are not loaded. Run train.py first.", 500

        data = [
            float(request.form["age"]),
            float(request.form["height"]),
            float(request.form["weight"]),
            float(request.form["sleep_hours"]),
            float(request.form["exercise_days"]),
            float(request.form["junk_food"]),
            float(request.form["sugar_intake"]),
            float(request.form["screen_time"])
        ]

        # Machine learning takes 2D Array
        X = np.array([data])

        cardiac = cardiac_model.predict(X)[0]
        obesity = obesity_model.predict(X)[0]
        cancer = cancer_model.predict(X)[0]

        # Calculate a pseudo score using data logic
        bmi = data[2] / (data[1] ** 2)

        junk = data[5]
        sugar = data[6]
        screen = data[7]

        score = max(
            100 - (junk*7 + sugar*7 + screen*3 + abs(bmi - 22)*1.5),
            30
        )

        return render_template(
            "result.html",
            cardiac=cardiac,
            obesity=obesity,
            cancer=cancer,
            score=int(score)
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
