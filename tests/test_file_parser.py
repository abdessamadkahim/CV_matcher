def test_imports():
    from app.services.file_parser import (
        SUPPORTED_EXTENSIONS,
        _PDF_MAGIC,
    )

    assert SUPPORTED_EXTENSIONS == {".pdf"}
    assert _PDF_MAGIC == b"%PDF"
import pytest
from app.exceptions import FileTooLargeError,UnsupportedFileTypeError,EmptyDocumentError
from app.services.file_parser import (
    extract_text,
    clean_text,
    fix_pdf_encoding,
)


def test_fichier_trop_gros():
    with pytest.raises(FileTooLargeError):
        extract_text(
            "cv.pdf",
            b"123456",
            max_bytes=5,
        )
def test_extension_non_supportee():
    with pytest.raises(UnsupportedFileTypeError):
        extract_text(
            "cv.txt",
            b"bonjour",
            5 * 1024 * 1024,
        )
def test_extension_qui_ment():
    with pytest.raises(UnsupportedFileTypeError):
        extract_text( "cv.pdf",
            b"ceci n'est pas un pdf",
            5 * 1024 * 1024,)


def test_vrai_pdf():
    with open("samples/sara martin.pdf", "rb") as f:
        contenu = f.read()

    texte = extract_text(
        "sara martin.pdf",
        contenu,
        5 * 1024 * 1024
    )

    print("\n--- TEXTE EXTRAIT ---")
    print(texte)

    assert texte
def test_clean_text():
    text= """
    Sara Martin


    Développeuse Python

    
    FORMATION
    ISIMA"""
    resultat=clean_text(text)
    print("\n -----------texte nettoyé---------")
    print(resultat)
    assert resultat==(
        "Sara Martin\n"
        "Développeuse Python\n"
        "FORMATION\n"
        "ISIMA"
    )
    

from app.schemas import (
    Contact,
    EducationItem,
    ResumeData,
)


def test_resume_data():
    resume = ResumeData(
        contact=Contact(
            name="Sara Martin",
            email="sara@example.com",
        ),
        summary="Développeuse Python",
        skills=["Python", "SQL", "Git"],
        education=[
            EducationItem(
                institution="ISIMA",
                degree="Diplôme d'ingénieur",
                field_of_study="Informatique",
                start_date="2023",
                end_date="2026",
            )
        ],
    )

    assert resume.contact.name == "Sara Martin"
    assert resume.contact.email == "sara@example.com"
    assert "Python" in resume.skills
    assert resume.education[0].institution == "ISIMA"


def test_fix_pdf_encoding():
    texte = "(cid:201)tudiant IngØnieur en informatique"

    resultat = fix_pdf_encoding(texte)

    print("\n========== ENCODAGE ==========")
    print("Avant :", texte)
    print("Après :", resultat)
    print("==============================")

    assert "Étudiant" in resultat