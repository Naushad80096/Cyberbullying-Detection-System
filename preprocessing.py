import re


def clean_text(text):

    text = str(text)

    text = text.lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z ]", "", text)

    text = text.strip()

    return text


def preprocess_dataset(data):

    print("Cleaning text...")

    data["clean_text"] = data["tweet"].apply(clean_text)

    return data