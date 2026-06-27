from flask import Flask, render_template, request
import joblib
from config import get_config

config = get_config()

app = Flask(__name__)
app.config["SECRET_KEY"] = config.SECRET_KEY

model = joblib.load(config.MODEL_PATH)
vectorizer = joblib.load(config.VECTORIZER_PATH)


def analyze_message(message):
    """
    Predict whether the message is Spam or Safe
    and return AI analysis details.
    """

    vector = vectorizer.transform([message])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)[0]

    confidence = round(max(probability) * 100, 2)

    if prediction == 1:
        result = "SPAM EMAIL"
        icon = "🚫"
        color = "danger"
        risk = "HIGH"

        explanation = (
            "The AI model detected linguistic patterns commonly "
            "associated with spam messages, such as promotional "
            "or suspicious wording."
        )

        recommendation = (
            "Avoid clicking unknown links or sharing personal information."
        )

    else:
        result = "SAFE EMAIL"
        icon = "✅"
        color = "success"
        risk = "LOW"

        explanation = (
            "The AI model found the message to be consistent "
            "with legitimate communication."
        )

        recommendation = (
            "This message appears safe."
        )

    return {
        "prediction": result,
        "icon": icon,
        "color": color,
        "confidence": confidence,
        "risk": risk,
        "explanation": explanation,
        "recommendation": recommendation
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    message = request.form.get("message", "").strip()

    if message == "":
        return render_template(
            "index.html",
            error="Please enter an email or SMS message."
        )

    result = analyze_message(message)

    return render_template(
        "index.html",
        message=message,
        **result
    )


if __name__ == "__main__":
    app.run(debug=True)
