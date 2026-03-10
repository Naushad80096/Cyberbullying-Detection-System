from sklearn.feature_extraction.text import TfidfVectorizer


def tfidf_features(text):

    print("Extracting TF-IDF features...")

    vectorizer = TfidfVectorizer(
        max_features=5000,
        stop_words="english"
    )

    X = vectorizer.fit_transform(text)

    return X, vectorizer