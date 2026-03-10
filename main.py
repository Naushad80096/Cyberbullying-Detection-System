from data_loader import load_dataset
from preprocessing import preprocess_dataset
from feature_extraction import tfidf_features
from train_models import train_models
from evaluation import evaluate_models
from visualization import plot_accuracy
from config import DATA_PATH

import joblib


def main():

    print("Starting Cyberbullying Detection Project")

    data = load_dataset()

    data = preprocess_dataset(data)

    X, vectorizer = tfidf_features(data["clean_text"])

    y = data["class"]

    models, X_test, y_test = train_models(X, y)

    results = evaluate_models(models, X_test, y_test)

    plot_accuracy(results)

    best_model = models["Logistic Regression"]

    joblib.dump(best_model, "models/cyberbullying_model.pkl")

    print("Project Finished Successfully")


if __name__ == "__main__":
    main()