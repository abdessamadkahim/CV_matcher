from app.schemas import ResumeData
from app.services.resume_parser import parse_resume
from app.services.file_parser import extract_text


def test_parse_resume():

    texte = """
    Sara Martin
    Développeuse Python

    FORMATION
    ISIMA – École d'ingénieurs en informatique
    2023 – 2026

    COMPÉTENCES
    Python
    SQL
    Git
    Linux

    EXPÉRIENCE
    Stage développeuse Python
    Développement d'une application web.
    """

    resume = parse_resume(texte)

    print("\n")
    print("========== RESUME DATA ==========")
    print(resume)
    print("=================================")

    assert isinstance(resume, ResumeData)
def test_parse_resume_pdf():
    with open("samples/CV_Abdessamad_Kahim  (1).pdf", "rb") as f:
        contenu = f.read()

    texte = extract_text(
        "CV_Abdessamad_Kahim  (1).pdf",
        contenu,
        5 * 1024 * 1024,
    )

    resume = parse_resume(texte)

    print("\n")
    print("========== TEXTE EXTRAIT ==========")
    print(texte)

    print("\n")
    print("========== RESUME DATA ==========")
    print(resume)

    print("\n")
    print("========== COMPÉTENCES ==========")
    print(resume.skills)

    print("\n")
    print("========== EXPÉRIENCES ==========")
    print(resume.experience)

    print("\n")
    print("========== FORMATIONS ==========")
    print(resume.education)

    print("=================================")

    assert isinstance(resume, ResumeData)