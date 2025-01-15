from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:admin@localhost:3306/dev_data"
    
    class Config:
        env_file = f"{Path(__file__).resolve().parent.parent.parent}/.env"

settings = Settings()
