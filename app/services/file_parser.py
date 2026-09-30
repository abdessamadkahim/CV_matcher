import io
from pathlib import Path

import pdfplumber
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

from app.exceptions import EmptyDocumentError, FileTooLargeError, UnsupportedFileTypeError

SUPPORTED_EXTENSIONS = {".pdf", ".docx"}
_PDF_MAGIC = b"%PDF"
_ZIP_MAGIC = b"PK"


def extract_text(filename:str,content:bytes,max_bytes:int)->str:
  if(len(content)>max_bytes):
    raise FileTooLargeError(f"Le fichier dépasse la limite de "
            f"{max_bytes // (1024 * 1024)} Mo.")
  ext = Path(filename or "").suffix.lower()

  if ext not in SUPPORTED_EXTENSIONS:
        raise UnsupportedFileTypeError(
            "Seuls les fichiers .pdf et .docx sont acceptés.")
  if ext==".pdf":
    if not content.startswith(_PDF_MAGIC):
      raise UnsupportedFileTypeError(
        "le fichier a l'extesnion .pdf mais il est pas vraiment un fichier  pdf"
      )
    
        
    
