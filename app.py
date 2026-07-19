import streamlit as st
import pandas as pd
import pickle

with open("student_performance_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Performance Prediction")
st.write("Enter the student's details below.")

studied_credits = st.number_input(
    "Studied Credits",
    min_value=0,
    max_value=250,
    value=120
)

total_clicks = st.number_input(
    "Total Clicks",
    min_value=0,
    max_value=5000,
    value=1500
)

avg_score = st.number_input(
    "Average Score",
    min_value=0.0,
    max_value=100.0,
    value=65.0
)

engagement = st.selectbox(
    "Engagement Level",
    ["Low", "Medium", "High"]
)

risk = st.selectbox(
    "Risk Level",
    ["Low", "Medium", "High"]
)

engagement_map = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

risk_map = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

new_student = pd.DataFrame({

    "studied_credits":[studied_credits],
    "total_clicks":[total_clicks],
    "avg_score":[avg_score],
    "engagement_level":[engagement_map[engagement]],
    "risk_level":[risk_map[risk]]

})

if st.button("Predict"):

    prediction = model.predict(new_student)

    st.success(f"Predicted Performance : {prediction[0]}")

if prediction[0] == "Excellent":

    st.balloons()

elif prediction[0] == "Good":

    st.info("Good performance. Keep practicing.")

elif prediction[0] == "Average":

    st.warning("Needs more practice.")

else:

    st.error("Student is at high academic risk.")    
