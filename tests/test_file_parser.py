def test_imports():
    from app.services.file_parser import (
        SUPPORTED_EXTENSIONS,
        _PDF_MAGIC,
        _ZIP_MAGIC,
    )

    assert SUPPORTED_EXTENSIONS == {".pdf", ".docx"}
    assert _PDF_MAGIC == b"%PDF"
    assert _ZIP_MAGIC == b"PK"
