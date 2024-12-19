import os

# Example configuration file for environment variables
class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
