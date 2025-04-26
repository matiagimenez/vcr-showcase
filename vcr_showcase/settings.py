from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    API_URL: str = "https://dummyjson.com"


Settings = _Settings()
