from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings. """ 

    # database
    postgres_database_url: str = "postgresql://localhost:5432/dexter"

    @property
    def database_url(self) -> str:
        #feel free to configure your db
        return self.postgres_database_url
    

settings = Settings()