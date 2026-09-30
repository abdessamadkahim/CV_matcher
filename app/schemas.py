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
    


class EducationItem(BaseModel):
    institution: str | None = Field(None, description="Nom de l'université / école.")
    degree: str | None = Field(None, description="Diplôme, ex: 'Licence', 'Master', 'B.Tech'.")
    field_of_study: str | None = Field(None, description="Spécialité / filière.")
    start_date: str | None = Field(None, description="'AAAA-MM' ou 'AAAA'.")
    end_date: str | None = Field(None, description="'AAAA-MM' ou 'AAAA' (une date prévue est acceptée).")
    gpa: str | None = Field(None, description="Moyenne / mention telle qu'écrite, si présente.")


class ProjectItem(BaseModel):
    name: str | None = Field(None, description="Titre du projet.")
    description: str | None = Field(None, description="Description en 1 ou 2 phrases, copiée du texte.")
    technologies: list[str] = Field(default_factory=list, description="Technologies listées pour ce projet.")
    bullets: list[str] = Field(default_factory=list, description="Points détaillés, tels quels.")
    link: str | None = Field(None, description="URL du projet, si présente.")


class ResumeData(BaseModel):
    """Représentation structurée d'UN CV complet."""

    contact: Contact = Field(default_factory=Contact)
    summary: str | None = Field(None, description="Paragraphe de profil / objectif, tel quel, s'il existe.")
    skills: list[str] = Field(
        default_factory=list,
        description=(
            "Liste de compétences individuelles (langages, outils, méthodes) explicitement écrites "
            "dans le CV. Une compétence par élément : 'Python, SQL' devient deux éléments. "
            "N'AJOUTE PAS de compétences non écrites."
        ),
    )
    experience: list[ExperienceItem] = Field(default_factory=list, description="Expériences pro, la plus récente d'abord.")
    education: list[EducationItem] = Field(default_factory=list)
    projects: list[ProjectItem] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list, description="Noms des certifications, tels qu'écrits.")
    # Calculé par notre code (pas par l'IA, qui se trompe souvent en calcul de dates).
    total_years_experience: float | None = Field(
        None, description="Toujours laisser vide. Calculé par l'application."
    )