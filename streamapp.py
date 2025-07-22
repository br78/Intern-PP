import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load trained model
model = joblib.load('fraud_model.pkl')

# Define the input features
features = [
    'Tot_Clms', 'Tot_Drug_Cst','Gnrc_Tot_Drug_Cst', 'Brnd_Tot_Drug_Cst', 'Opioid_Tot_Drug_Cst', 
    'Bene_Avg_Age', 'Bene_Feml_Cnt', 'Bene_Male_Cnt'
]

st.title(" Medicare Fraud Detection App")
st.markdown("Enter the values to check if a claim is potentially fraudulent.")

# Create user inputs
input_data = {}
for feature in features:
    input_data[feature] = st.number_input(f"{feature.replace('_', ' ')}", min_value=0.0)

# Predict on button click
if st.button("Detect Fraud"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    prediction_proba = model.predict_proba(input_df)[0][1]

    if prediction:
        st.error(f"Fraud Detected! (Probability: {prediction_proba:.2f})")
    else:
        st.success(f"No Fraud Detected. (Probability: {prediction_proba:.2f})")

    st.subheader("Input Summary:")
    st.write(input_df)
