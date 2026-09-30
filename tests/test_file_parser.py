def test_imports():
    from app.services.file_parser import (
        SUPPORTED_EXTENSIONS,
        _PDF_MAGIC,
        _ZIP_MAGIC,
    )

    assert SUPPORTED_EXTENSIONS == {".pdf", ".docx"}
    assert _PDF_MAGIC == b"%PDF"
    assert _ZIP_MAGIC == b"PK"
import pytest
from app.exceptions import FileTooLargeError,UnsupportedFileTypeError
from app.services.file_parser import extract_text


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

