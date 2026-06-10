import streamlit as st
from src.analyzer import analyze_cv

st.title("CV Job Match Agent")

st.write("Paste your CV and job description below.")

cv_text = st.text_area("Paste your CV here", height=250)
job_description = st.text_area("Paste the job description here", height=250)

if st.button("Analyze"):
    if not cv_text or not job_description:
        st.warning("Please paste both your CV and the job description.")
    else:
        with st.spinner("Analyzing your CV..."):
            result = analyze_cv(cv_text, job_description)

        st.subheader("Analysis Result")
        st.write(result)