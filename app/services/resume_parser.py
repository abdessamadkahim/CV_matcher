from app.schemas import ResumeData
from openai import OpenAI

from app.exceptions import LLMExtractionError

client = OpenAI()


SYSTEM_PROMPT = """
Tu es un extracteur de CV.

Ta tâche est de transformer le texte brut d'un CV en données structurées
correspondant exactement au modèle ResumeData.

Règles importantes :
- Utilise uniquement les informations présentes dans le CV.
- N'invente aucune information.
- Si une information est absente, laisse le champ à null ou [].
- Conserve les compétences telles qu'elles apparaissent dans le CV.
- Les expériences doivent être séparées correctement.
- Les formations doivent être séparées correctement.
- Les projets doivent être séparés correctement.
- Ne calcule pas total_years_experience.
- Pour total_years_experience, laisse toujours null.
"""

def parse_resume(text: str) -> ResumeData:
    """Transforme le texte d'un CV en données structurées."""

    if not text.strip():
        return ResumeData()

    # Pour le moment, extraction simple.
    # L'appel au LLM sera ajouté apres les tests de structure retourne.

    return ResumeData()