from src.ai_client import ask_ai

def analyze_cv(cv_text, job_description):
    prompt = f"""
You are a CV improvement assistant.

Compare the CV with the job description and give practical improvement suggestions.

CV:
{cv_text}

Job description:
{job_description}

Return the answer in this format:

Match score:
Missing skills:
Keywords to add:
Weak areas:
Suggested rewritten CV bullets:
Final checklist:
"""

    return ask_ai(prompt)