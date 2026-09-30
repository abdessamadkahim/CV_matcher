class AppError(Exception):
    status_code = 500

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class UnsupportedFileTypeError(AppError):
    status_code = 415


class FileTooLargeError(AppError):
    status_code = 413


class EmptyDocumentError(AppError):
    status_code = 422


class LLMExtractionError(AppError):
    status_code = 502