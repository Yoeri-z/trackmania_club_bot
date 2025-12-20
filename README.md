# Trackmania Discord Bot

This is a Discord bot for Trackmania clubs, providing real-time leaderboard updates, player information, and room status notifications.

## Features

- **Leaderboard Tracking:** Automatically tracks leaderboards and notifies on new personal bests.
- **Room Status:** Shows the number of active players in a club room.
- **Player Info:** Fetch information about players.
- **Discord Commands:** Interact with the bot using `!` commands.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Configuration

1.  Create a file named `.env` in the root of the project.
2.  Add the following environment variables to the `.env` file:

    ```env
    # Your Discord Bot Token
    DISCORD_TOKEN=your_discord_bot_token_here

    # Your Trackmania API credentials (for Ubisoft Connect)
    TRACKMANIA_API_USER=your_ubisoft_email
    TRACKMANIA_API_PASSWORD=your_ubisoft_password

    # Your Trackmania Club ID
    CLUB_ID=your_club_id_here

    # (Optional) The database URL. Defaults to a local SQLite database.
    # DATABASE_URL=sqlite:///trackmania.db
    # For PostgreSQL:
    # DATABASE_URL=postgresql://user:password@host:port/database

    # (Optional) Channel IDs for notifications
    # NOTIFICATION_CHANNEL_ID=your_channel_id_for_pbs
    # ROOM_STATUS_CHANNEL_ID=your_channel_id_for_room_status
    ```

### Running the Bot

Once you have configured your `.env` file, you can run the bot using Docker Compose:

```bash
docker-compose up --build
```

To run the bot in the background, use the `-d` flag:

```bash
docker-compose up --build -d
```

To stop the bot:

```bash
docker-compose down
```

## Project Structure

- `src/`: Main source code directory.
  - `api/`: Trackmania API client interface.
  - `config.py`: Configuration loader.
  - `discord/`: Discord bot, commands, and UI.
  - `leaderboard_tracker/`: Logic for tracking leaderboards.
  - `main.py`: Application entry point.
  - `room_tracker/`: Logic for tracking club rooms.
  - `storage/`: Database models, session management, and repositories.
- `Dockerfile`: Defines the Docker container for the application.
- `docker-compose.yml`: Docker Compose configuration.
- `requirements.txt`: Python dependencies.
- `TODO.md`: Development checklist.
- `PRD.md`: Product Requirements Document.

This project is still under development. The core structure is in place, but many features are currently placeholders.
