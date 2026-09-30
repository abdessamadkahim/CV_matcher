from typing import Literal

from pydantic import BaseModel, Field

class Contact(BaseModel):
    name: str | None = Field(None, description="Nom complet du candidat, tel qu'écrit.")
    email: str | None = Field(None, description="Adresse email, si présente.")
    phone: str | None = Field(None, description="Numéro de téléphone tel qu'écrit, si présent.")
    location: str | None = Field(None, description="Ville / pays tel qu'écrit, si présent.")
    links: list[str] = Field(
        default_factory=list,
        description="URLs (LinkedIn, GitHub, portfolio) présentes dans le texte uniquement.",
    )


class ExperienceItem(BaseModel):
    company: str | None = Field(None, description="Nom de l'entreprise.")
    title: str | None = Field(None, description="Intitulé du poste.")
    start_date: str | None = Field(
        None, description="Date de début au format 'AAAA-MM' (ou 'AAAA' si le mois est inconnu)."
    )
    end_date: str | None = Field(
        None,
        description="Date de fin au format 'AAAA-MM' (ou 'AAAA'). null si le poste est en cours.",
    )
    is_current: bool = Field(False, description="True seulement si le CV dit que le poste est en cours.")
    location: str | None = Field(None, description="Lieu du poste, si indiqué.")
    bullets: list[str] = Field(
        default_factory=list,
        description="Missions/réalisations, copiées TELLES QUELLES, une chaîne par ligne.",
    )