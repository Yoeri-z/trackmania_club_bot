# main.py
from src.config import config
import src.discord_bot.bot as bot
from src.storage.database import init_db
from src.leaderboard_tracker.tracker import LeaderboardTracker
from src.room_tracker.tracker import RoomTracker


def main():
    """
    Main function to initialize and run the Trackmania Discord Bot.
    """
    print("Bot starting...")

    # Check for required configuration
    if not all([config.DISCORD_TOKEN]):
        print(
            "DISCORD_TOKEN is not set. Please check your .env file or environment variables."
        )
        return

    print("Configuration loaded successfully.")

    # Initialize the database
    print("Initializing database...")
    init_db()
    print("Database initialized.")

    # Run the bot
    bot.start()

    leaderboard_tracker = LeaderboardTracker()
    room_tracker = RoomTracker()

    leaderboard_tracker.start()
    room_tracker.start()

    print("Bot stopped.")


if __name__ == "__main__":
    main()
