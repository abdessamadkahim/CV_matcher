from openai import OpenAI

from app.config import get_settings
from app.exceptions import LLMExtractionError
from app.schemas import JobDescriptionData


config = get_settings()

client = OpenAI(
    api_key=config.llm_api_key,
    base_url=config.llm_base_url,
)


SYSTEM_PROMPT = """
Tu es un extracteur d'offres d'emploi.

Ta tâche est de transformer le texte brut d'une offre d'emploi
en données structurées correspondant exactement au modèle
JobDescriptionData.

Règles importantes :

- Utilise uniquement les informations présentes dans l'offre.
- N'invente aucune information.
- Si une information est absente, utilise null ou [].
- Identifie correctement le titre du poste.
- Identifie l'entreprise si elle est mentionnée.
- Sépare les compétences obligatoires des compétences souhaitées.
- Identifie les compétences comportementales (soft skills).
- Identifie les responsabilités et missions.
- Identifie les exigences de formation.
- Identifie les mots-clés importants du domaine.
- Identifie le niveau de séniorité uniquement s'il est indiqué
  ou clairement identifiable dans l'offre.
- Ne transforme pas une compétence souhaitée en compétence obligatoire.
- Ne crée aucune compétence qui n'est pas présente dans l'offre.
"""


def parse_job_description(text: str) -> JobDescriptionData:
    """Transforme le texte d'une offre d'emploi en JobDescriptionData."""

    if not text.strip():
        return JobDescriptionData()

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
            text_format=JobDescriptionData,
            max_output_tokens=config.llm_max_tokens,
        )

        return response.output_parsed

    except Exception as exc:
        raise LLMExtractionError(
            f"Erreur lors de l'extraction de l'offre avec le LLM : {exc}"
        ) from exc