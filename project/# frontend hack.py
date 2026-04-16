# frontend.py
import streamlit as st
import requests

st.title("🎓 Student Performance Predictor")

study = st.slider("Study Hours", 0, 10)
sleep = st.slider("Sleep Hours", 0, 10)
attendance = st.slider("Attendance %", 0, 100)

if st.button("Predict"):
    response = requests.post(
        "http://localhost:5000/predict",
        json={
            "study_hours": study,
            "sleep_hours": sleep,
            "attendance": attendance
        }
    )

    result = response.json()

    st.write("### Result")
    st.write("Pass" if result["prediction"] == 1 else "Fail")
    st.write("Probability:", result["probability"])
    st.write("Explanation:", result["explanation"])