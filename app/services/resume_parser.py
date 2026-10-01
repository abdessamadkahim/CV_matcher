from openai import OpenAI

from app.config import get_settings
from app.exceptions import LLMExtractionError
from app.schemas import ResumeData


config = get_settings()

client = OpenAI(
    api_key=config.llm_api_key,
    base_url=config.llm_base_url,
)


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
    """Transforme le texte brut d'un CV en ResumeData avec un LLM."""

    if not text.strip():
        return ResumeData()

    try:
        response = client.responses.parse(
            model=config.llm_model,
            input=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
            text_format=ResumeData,
            max_output_tokens=config.llm_max_tokens,
        )

        return response.output_parsed

    except Exception as exc:
        raise LLMExtractionError(
            f"Erreur lors de l'extraction du CV avec le LLM : {exc}"
        ) from exc