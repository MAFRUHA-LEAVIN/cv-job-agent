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
        result = analyze_cv(cv_text, job_description)

        st.subheader("Analysis Result")

        st.write(f"**Match score:** {result['match_score']}")

        st.write("**Missing skills:**")
        for skill in result["missing_skills"]:
            st.write(f"- {skill}")

        st.write("**Keywords to add:**")
        for keyword in result["keywords_to_add"]:
            st.write(f"- {keyword}")

        st.write("**Weak areas:**")
        for area in result["weak_areas"]:
            st.write(f"- {area}")

        st.write("**Suggested rewritten CV bullets:**")
        for bullet in result["rewritten_bullets"]:
            st.write(f"- {bullet}")

        st.write("**Final checklist:**")
        for item in result["checklist"]:
            st.write(f"- {item}")