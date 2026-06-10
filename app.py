import streamlit as st
from src.cv_agent import run_cv_agent
from src.save_result import save_analysis_result

st.title("CV Job Match Agent")

st.write("Paste or upload your CV, then paste the job description below.")

uploaded_cv = st.file_uploader("Upload your CV as a .txt file", type=["txt"])

if uploaded_cv is not None:
    cv_text = uploaded_cv.read().decode("utf-8")
    st.text_area("CV text from uploaded file", value=cv_text, height=250)
else:
    cv_text = st.text_area("Paste your CV here", height=250)

job_description = st.text_area("Paste the job description here", height=250)

if st.button("Analyze"):
    if not cv_text or not job_description:
        st.warning("Please paste or upload your CV and paste the job description.")
    else:
        with st.spinner("Analyzing your CV..."):
            result = run_cv_agent(cv_text, job_description)

        st.subheader("Analysis Result")
        st.write(result)

        saved_path = save_analysis_result(result)
        st.success(f"Analysis saved to: {saved_path}")