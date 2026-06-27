import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from config import get_config


config = get_config()


print("Loading dataset...")

df = pd.read_csv(config.DATASET_PATH, encoding="latin-1")

df = df[["v1", "v2"]]

df.columns = ["label", "message"]

print("Dataset loaded successfully!")
print("Total Messages:", len(df))
print()


df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})



X = df["message"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=config.TEST_SIZE,
    random_state=config.RANDOM_STATE
)

print("Training Messages :", len(X_train))
print("Testing Messages  :", len(X_test))
print()

print("Creating TF-IDF Vectorizer...")

vectorizer = TfidfVectorizer(
    max_features=config.TFIDF_MAX_FEATURES,
    ngram_range=config.TFIDF_NGRAM_RANGE,
    min_df=config.TFIDF_MIN_DF
)

X_train_vector = vectorizer.fit_transform(X_train)
X_test_vector = vectorizer.transform(X_test)

print("Vectorization completed!")
print()


print("Training Naive Bayes Model...")

model = MultinomialNB(alpha=config.NB_ALPHA)

model.fit(X_train_vector, y_train)

print("Training completed!")
print()

print("Testing Model...")

predictions = model.predict(X_test_vector)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", round(accuracy * 100, 2), "%")
print()

print("Classification Report")
print(classification_report(y_test, predictions))

print("Confusion Matrix")
print(confusion_matrix(y_test, predictions))


print()
print("Saving model...")

joblib.dump(model, config.MODEL_PATH)
joblib.dump(vectorizer, config.VECTORIZER_PATH)

print("Model saved to:")
print(config.MODEL_PATH)

print()

print("Vectorizer saved to:")
print(config.VECTORIZER_PATH)

print()

print("Training Finished Successfully!")