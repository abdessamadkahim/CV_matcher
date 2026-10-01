from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- Connexion à l'IA (lues depuis le fichier .env) ---
    llm_base_url: str = "https://api.groq.com/openai/v1"
    llm_api_key: str = ""
    llm_model: str = "openai/gpt-oss-120b"
    llm_max_tokens: int = 8192
    llm_max_attempts: int = 2

    # --- Limites de sécurité ---
    max_upload_mb: int = 5
    max_input_chars: int = 30_000
    min_input_chars: int = 50

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
