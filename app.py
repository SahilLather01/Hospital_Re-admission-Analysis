# app.py

import streamlit as st
import pandas as pd
import joblib

# Load model and features
model = joblib.load("readmission_model.pkl")
features = joblib.load("feature_names.pkl")

st.title("🏥 Hospital Readmission Predictor")

# Input form
user_input = {}
for feature in features:
    if feature in ['medical_specialty', 'diag_1', 'diag_2', 'diag_3', 'glucose_test', 'A1Ctest', 'change', 'diabetes_med']:
        user_input[feature] = st.selectbox(f"{feature}", options=[0, 1, 2])  # Simplified encoding
    else:
        user_input[feature] = st.number_input(f"{feature}", min_value=0.0)

# Predict button
if st.button("Predict Readmission"):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    st.success(f"🔍 Prediction: {'Readmitted' if prediction == 1 else 'Not Readmitted'}")
