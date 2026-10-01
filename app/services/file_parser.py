import io
from pathlib import Path

import pdfplumber

from app.exceptions import EmptyDocumentError, FileTooLargeError, UnsupportedFileTypeError

SUPPORTED_EXTENSIONS = {".pdf"}
_PDF_MAGIC = b"%PDF"


def extract_text(filename:str,content:bytes,max_bytes:int)->str:
  if(len(content)>max_bytes):
    raise FileTooLargeError(f"Le fichier dépasse la limite de "
            f"{max_bytes // (1024 * 1024)} Mo.")
  ext = Path(filename or "").suffix.lower()

  if ext not in SUPPORTED_EXTENSIONS:
        raise UnsupportedFileTypeError(
            "Seuls les fichiers .pdf  est accepté.")
  if ext==".pdf":
    if not content.startswith(_PDF_MAGIC):
      raise UnsupportedFileTypeError(
        "le fichier a l'extesnion .pdf mais il est pas vraiment un fichier  pdf"
      )
    return _extract_pdf(content)
def _extract_pdf(content:bytes)->str:
    pages:list[str]=[]
    try:
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            for page in pdf.pages:
                pages.append(page.extract_text() or "")
    except Exception as exc:
        raise UnsupportedFileTypeError(
            f"Impossible de lire le PDF : {exc}"
        ) from exc
    text="\n\n".join(pages).strip()
    if not text:
        raise EmptyDocumentError("aucun text trouve ")
    text = clean_text(text)
    text = fix_pdf_encoding(text)
    return text
def clean_text(text: str) -> str:
    """Nettoie le texte extrait d'un document."""

    lines = []

    for line in text.splitlines():
        line = line.strip()

        if line:
            lines.append(line)

    return "\n".join(lines)
  


def fix_pdf_encoding(text: str) -> str:
    """Corrige certains caractères mal décodés lors de l'extraction PDF."""

    replacements = {
        "Ø": "é",
        "ø": "è",
        "Ł": "è",
        "Ø": "é",
        "˚": "°",
        "(cid:22)": "–",
        "(cid:136)": "•",
        "(cid:224)": "à",
        "(cid:247)": "œ",
        "(cid:201)": "É",
        "(cid:192)": "À",
        "(cid:231)": "ç",
        "(cid:244)": "ô",
        "(cid:232)": "è",
        "(cid:233)": "é",
        "(cid:234)": "ê",
        "(cid:235)": "ë",
        "(cid:238)": "î",
        "(cid:239)": "ï",
        "(cid:249)": "ù",
    }

    for wrong, correct in replacements.items():
        text = text.replace(wrong, correct)

    return text
        
    
