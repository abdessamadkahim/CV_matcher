from app.schemas import JobDescriptionData,ResumeData
def normalize_skill(skill: str) -> str:
    """Normalise une compétence pour faciliter la comparaison."""

    return skill.strip().lower()


def match_skills(
    resume: ResumeData,
    job: JobDescriptionData,
) -> dict:
    """Compare les compétences du CV avec celles demandées dans l'offre."""

    resume_skills = {
        normalize_skill(skill)
        for skill in resume.skills
    }

    required_skills = {
        normalize_skill(skill)
        for skill in job.required_skills
    }
    matched_skills=resume_skills & required_skills
    missing_skills=required_skills -resume_skills
    if(required_skills):
        score=len(matched_skills)/len(required_skills)
    else:
      score =0

    return{
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "score": score,
    }