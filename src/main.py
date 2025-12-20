# main.py
from src.config import config
from src.discord.bot import run_bot
from src.storage.database import init_db

def main():
    """
    Main function to initialize and run the Trackmania Discord Bot.
    """
    print("Bot starting...")

    # Check for required configuration
    if not all([config.DISCORD_TOKEN]):
        print("DISCORD_TOKEN is not set. Please check your .env file or environment variables.")
        return

    print("Configuration loaded successfully.")
    
    # Initialize the database
    print("Initializing database...")
    init_db()
    print("Database initialized.")

    # Run the bot
    run_bot()

    print("Bot stopped.")


if __name__ == "__main__":
    main()
