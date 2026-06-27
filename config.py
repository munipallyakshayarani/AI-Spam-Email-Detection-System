import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:

    SECRET_KEY = "spam-email-classifier"

    DATA_DIR = BASE_DIR / "data"
    MODEL_DIR = BASE_DIR / "models"

    DATASET_PATH = DATA_DIR / "spam.csv"

    MODEL_PATH = MODEL_DIR / "naive_bayes_model.pkl"

    VECTORIZER_PATH = MODEL_DIR / "tfidf_vectorizer.pkl"

    TEST_SIZE = 0.2

    RANDOM_STATE = 42

    TFIDF_MAX_FEATURES = 5000

    TFIDF_NGRAM_RANGE = (1, 2)

    TFIDF_MIN_DF = 2

    NB_ALPHA = 0.1


def get_config():
    return Config()