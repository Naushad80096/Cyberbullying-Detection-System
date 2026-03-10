from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


def evaluate_models(models, X_test, y_test):

    results = {}

    for name, model in models.items():

        predictions = model.predict(X_test)

        acc = accuracy_score(y_test, predictions)

        print("\nModel:", name)

        print("Accuracy:", acc)

        print(classification_report(y_test, predictions))

        results[name] = acc

    return results