import pandas as pd
from config import DATA_PATH


def load_dataset():
    print("Loading dataset...")

    data = pd.read_csv(DATA_PATH)

    print("Dataset loaded successfully")
    print("Total rows:", len(data))

    return data