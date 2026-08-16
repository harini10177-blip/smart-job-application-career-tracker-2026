def calculate_match(job_skills, user_skills):

    job_skills = [skill.strip().lower() for skill in job_skills]
    user_skills = [skill.strip().lower() for skill in user_skills]

    matched_skills = set(job_skills) & set(user_skills)

    if len(job_skills) == 0:
        return 0

    match_percentage = (len(matched_skills) / len(job_skills)) * 100

    return match_percentage


def recommend_jobs(jobs, user_skills):

    recommendations = []

    for job in jobs:
        job_skills = job["skills"].split()

        match_percentage = calculate_match(
            job_skills,
            user_skills
        )

        if match_percentage >= 50:
            recommendations.append(
                (job, match_percentage)
            )

    return recommendations