from src.ollama_client import ask_ai

def analyze_cv(cv_text, job_description):
    prompt = f"""
You are a practical CV improvement assistant.

Your task:
Compare the CV against the job description and suggest improvements.

Important rules:
- Be honest.
- Do not invent fake experience.
- If a skill is missing, say it is missing.
- Rewritten CV bullets must be based only on the CV text.
- Keep suggestions clear and useful for a job applicant.

CV:
{cv_text}

Job description:
{job_description}

Return the answer in this exact format:

## Match score
Give a score out of 100 and one short reason.

## Missing skills
List skills from the job description that are missing or weak in the CV.

## Keywords to add
List important keywords the user can add only if they are truthful.

## Weak areas
Explain which CV sections need improvement.

## Suggested rewritten CV bullets
Rewrite 3-5 bullet points based only on the user's existing experience.

## Final checklist
Give a short checklist of what to improve before applying.
"""

    return ask_ai(prompt)