from instructor import Mode
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # IMAP
    IMAP_HOST: str
    IMAP_USERNAME: SecretStr
    IMAP_PASSWORD: SecretStr

    # LLM
    LLM_MODE: Mode = Mode.TOOLS
    LLM_MODEL: str
    LLM_TEMPERATURE: float = 0.25

settings = Settings()
