
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)

model = joblib.load("diabetes_logistic_regression.pkl")

st.title("🩺 Diabetes Prediction System")
st.write("Logistic Regression based educational prediction application")

st.warning(
    "Educational project only. This tool is not a medical "
    "diagnostic system. Do not use its output for medical decisions."
)

st.subheader("Enter the input details")

gender = st.selectbox("Gender", ["Female", "Male", "Other"])

age = st.number_input(
    "Age",
    min_value=0.08,
    max_value=80.0,
    value=30.0
)

hypertension = st.selectbox(
    "Hypertension",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

heart_disease = st.selectbox(
    "Heart Disease",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

smoking_history = st.selectbox(
    "Smoking History",
    ["No Info", "never", "former", "current", "not current", "ever"]
)

bmi = st.number_input(
    "BMI",
    min_value=10.01,
    max_value=95.69,
    value=25.0
)

hba1c = st.number_input(
    "HbA1c Level",
    min_value=3.5,
    max_value=9.0,
    value=5.5
)

glucose = st.number_input(
    "Blood Glucose Level",
    min_value=80,
    max_value=300,
    value=100
)

if st.button("Predict"):

    input_data = pd.DataFrame([{
        "gender": gender,
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "smoking_history": smoking_history,
        "bmi": bmi,
        "HbA1c_level": hba1c,
        "blood_glucose_level": glucose
    }])

    probability = model.predict_proba(input_data)[0][1]
    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    st.write(f"Estimated model probability: {probability * 100:.2f}%")

    if prediction == 1:
        st.error("Model prediction: Diabetic class")
    else:
        st.success("Model prediction: Non-Diabetic class")

    st.caption(
        "This is a machine-learning estimate, not a diagnosis. "
        "Consult a qualified healthcare professional for medical advice."
    )
