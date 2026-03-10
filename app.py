import streamlit as st
import joblib
import re

st.title("Cyberbullying Detection System")

st.write("Enter a social media comment to detect cyberbullying.")

model = joblib.load("models/cyberbullying_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text


text = st.text_area("Enter comment")

if st.button("Predict"):

    if text.strip() == "":
        st.warning("Please enter a comment")

    else:

        text = clean_text(text)

        text_vector = vectorizer.transform([text])

        prediction = model.predict(text_vector)

        if prediction[0] == 1:
            st.error("Cyberbullying Detected")
        else:
            st.success("Normal Comment")