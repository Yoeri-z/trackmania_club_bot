import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Configuration class to load and store credentials from environment variables.
    """
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    TRACKMANIA_API_USER = os.getenv("TRACKMANIA_API_USER")
    TRACKMANIA_API_PASSWORD = os.getenv("TRACKMANIA_API_PASSWORD")
    CLUB_ID = os.getenv("CLUB_ID")

    # Database configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///trackmania.db")

config = Config()
