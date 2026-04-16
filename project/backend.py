from flask import Flask, request, jsonify
import pickle

app = Flask(_name_)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = [[
        data["study_hours"],
        data["sleep_hours"],
        data["attendance"]
    ]]

    prediction = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1]

    explanation = ""
    if data["study_hours"] < 3:
        explanation += "Low study hours. "
    if data["attendance"] < 70:
        explanation += "Low attendance. "

    return jsonify({
        "prediction": int(prediction),
        "probability": float(prob),
        "explanation": explanation
    })

if _name_ == "_main_":
    app.run(debug=True)