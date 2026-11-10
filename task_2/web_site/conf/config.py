from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    engine:str
    name:str
    user:str
    password:int
    host:str
    port:int
    secret_key:str
    email_host:str
    email_port:int
    email_host_user:str
    email_host_password:str
    
    class Config:
        env_file=BASE_DIR / ".env",
        env_file_encoding = "utf-8"


settings = Settings()