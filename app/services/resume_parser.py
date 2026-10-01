from app.schemas import ResumeData


def parse_resume(text: str) -> ResumeData:
    """Transforme le texte d'un CV en données structurées."""

    if not text.strip():
        return ResumeData()

    # Pour le moment, extraction simple.
    # L'appel au LLM sera ajouté apres les tests de structure retourne.

    return ResumeData()