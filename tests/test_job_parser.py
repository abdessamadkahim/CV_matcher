from app.schemas import JobDescriptionData
from app.services.job_parser import parse_job_description


def test_parse_job_description():

    texte = """
    Data Analyst

    Nous recherchons un Data Analyst pour rejoindre notre équipe.

    Missions :
    - Analyser les données commerciales.
    - Créer des dashboards avec Power BI.
    - Produire des rapports et indicateurs.
    - Travailler avec les équipes métier.

    Compétences requises :
    - Python
    - SQL
    - Power BI
    - Statistiques

    Compétences appréciées :
    - Tableau
    - Excel

    Profil :
    Bac+4/5 en informatique, data science ou statistiques.
    Une première expérience en analyse de données est appréciée.

    Qualités :
    - Esprit analytique
    - Travail en équipe
    - Autonomie
    """

    job = parse_job_description(texte)

    print("\n")
    print("========== JOB DATA ==========")
    print(job)

    print("\n")
    print("========== REQUIRED SKILLS ==========")
    print(job.required_skills)

    print("\n")
    print("========== NICE TO HAVE ==========")
    print(job.nice_to_have_skills)

    print("\n")
    print("========== RESPONSIBILITIES ==========")
    print(job.responsibilities)

    print("\n")
    print("=================================")

    assert isinstance(job, JobDescriptionData)