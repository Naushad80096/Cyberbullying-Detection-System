import matplotlib.pyplot as plt


def plot_accuracy(results):

    names = list(results.keys())

    values = list(results.values())

    plt.figure(figsize=(8,5))

    plt.bar(names, values)

    plt.title("Model Accuracy Comparison")

    plt.ylabel("Accuracy")

    plt.xlabel("Models")

    plt.savefig("results/model_accuracy.png")

    plt.show()