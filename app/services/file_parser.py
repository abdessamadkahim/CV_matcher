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