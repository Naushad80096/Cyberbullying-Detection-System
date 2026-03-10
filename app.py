import streamlit as st
import joblib
import pandas as pd

st.title("Cyberbullying Detection System")

st.write("Enter a social media comment to detect cyberbullying.")

model = joblib.load("models/cyberbullying_model.pkl")

text = st.text_area("Enter comment")

if st.button("Predict"):

    prediction = model.predict([text])

    if prediction[0] == 1:
        st.error("Cyberbullying Detected")
    else:
        st.success("Normal Comment")