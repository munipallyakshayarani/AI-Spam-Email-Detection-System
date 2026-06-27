import joblib

from config import get_config

config = get_config()

print("Loading trained model...")

model = joblib.load(config.MODEL_PATH)
vectorizer = joblib.load(config.VECTORIZER_PATH)

print("Model loaded successfully!")
print()

def predict_spam(message):

    message_vector = vectorizer.transform([message])

    prediction = model.predict(message_vector)

    if prediction[0] == 1:
        return "SPAM"
    else:
        return "NOT SPAM"

while True:

    print("=" * 50)
    print("Spam Email Detector")
    print("=" * 50)

    message = input("Enter your message:\n")

    result = predict_spam(message)

    print("\nPrediction:", result)

    choice = input("\nCheck another message? (yes/no): ")

    if choice.lower() != "yes":
        break

print("\nThank you for using Spam Email Detector!")