def analyze_cv(cv_text, job_description):
    return {
        "match_score": "72%",
        "missing_skills": [
            "Python",
            "API development",
            "Cloud deployment"
        ],
        "keywords_to_add": [
            "REST API",
            "backend development",
            "deployment",
            "automation"
        ],
        "weak_areas": [
            "Your CV does not clearly show measurable impact.",
            "Some technical tools are missing or not visible enough."
        ],
        "rewritten_bullets": [
            "Developed and maintained backend features using Python and REST APIs.",
            "Improved application reliability by supporting testing, debugging, and deployment workflows."
        ],
        "checklist": [
            "Add 3–5 keywords from the job description.",
            "Rewrite at least 2 experience bullets.",
            "Mention tools clearly under each project or job."
        ]
    }