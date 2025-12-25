This project is still under development and not ready for use yet.

# Trackmania Club Discord Bot

Welcome! This project is a Discord bot designed specifically for Trackmania clubs. It helps you keep your Discord community engaged by providing real-time leaderboard updates, player information, and club room status directly in your server.

Even if you're new to coding, this guide will walk you through setting it up step-by-step.

## Core Features

- **Leaderboard Tracking:** Automatically fetches leaderboard data and posts notifications for new personal bests in your club.
- **Room Status:** Displays the number of players currently active in your club's online room.
- **Player Info:** Lets you look up stats and information about any Trackmania player.
- **Discord Slash Commands:** All interactions are done through easy-to-use slash commands in Discord.

---

## Getting Started

Before you begin, you need to decide how you want to run the bot. There are four options, ordered from easiest to most advanced:

1.  **Managed Hosting:** The easiest, hands-off option.
2.  **Run with a Public Docker Image:** The simplest self-hosted option. No code required!
3.  **Run with Python:** A great way to learn the basics of running a code project on your own computer.
4.  **Run with Docker (Build from source):** A more advanced method that lets you build the Docker image yourself.

---

### Option 1: Managed Hosting (The Easy Way)

If you don't want to deal with code, terminals, or servers, I can host and manage the bot for you! In return for a small fee to cover server costs and my time, I'll handle the entire setup, configuration, and maintenance.

**Interested?** Just send me a message on Discord! `Bonjoeri`

---

### Option 2: Run with Docker

This is the simplest way to run the bot on your own hardware. It pulls a pre-built, public image from Docker Hub, so you don't have to interact with the source code.

#### Prerequisites

- **[Docker](https://www.docker.com/get-started)**: You'll need Docker installed to run the image.

#### Step-by-Step Guide

1.  **Create a Directory and `.env` file:**
    Create a folder anywhere on your computer. Inside that folder, create the `.env` file with your configuration. Follow the [**Configuration Guide**](#-configuration-guide) to fill it out.

2.  **Run the Bot:**
    Open a terminal and `cd` into the directory where you created your `.env` file. Then, run the following command:

    ```bash
    docker run -d --env-file .env --name my-trackmania-bot --restart always yoeriz/trackmania-club-bot:latest
    ```

    - `-d`: Runs the container in the background.
    - `--env-file .env`: Loads your secret credentials from the `.env` file.
    - `--name my-trackmania-bot`: Gives your container a memorable name.
    - `--restart always`: Ensures the bot restarts automatically if it stops or if you reboot your computer.

    The bot is now running!

3.  **Managing the Bot:**
    - **To check logs:** `docker logs my-trackmania-bot`
    - **To stop the bot:** `docker stop my-trackmania-bot`
    - **To remove the container:** `docker rm my-trackmania-bot`

---

### Option 3: Run with Python

This option is great if you want to run the bot on your own server or computer.

#### Prerequisites

Before you start, make sure you have the following software installed:

- **[Git](https://git-scm.com/downloads)**: A tool for downloading code from repositories like GitHub.
- **[Python 3.10+](https://www.python.org/downloads/)**: The programming language the bot is written in. Make sure to check the box that says "Add Python to PATH" during installation.

#### Step-by-Step Guide

1.  **Download the Code:**
    Open a terminal (like Command Prompt, PowerShell, or Terminal on Mac) and run this command to download the project into a folder named `myclub_bot`:

    ```bash
    git clone https://github.com/Yoeri-z/trackmania_club_bot.git ./myclub_bot
    ```

2.  **Navigate into the Project Folder:**

    ```bash
    cd myclub_bot
    ```

3.  **Set Up a Virtual Environment (Recommended):**
    This creates an isolated space for the bot's Python packages.

    ```bash
    python -m venv venv
    ```

    Activate it:

    - **Windows:** `.\venv\Scripts\activate`
    - **Mac/Linux:** `source venv/bin/activate`

4.  **Install Dependencies:**
    This command reads the `requirements.txt` file and installs all the necessary Python packages.

    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure Your Bot:**
    You'll need to create a `.env` file to store your secret credentials. See the [**Configuration Guide**](#-configuration-guide) below for detailed instructions on how to get these values.

6.  **Run the Bot!**
    Once your `.env` file is ready, start the bot with this command:
    ```bash
    python main.py
    ```
    If everything is set up correctly, you'll see messages in the terminal indicating the bot is online and connected to your server.

---

## Configuration(`.env` File)

Your bot needs a few secret keys and IDs to connect to Discord and Trackmania. The best practice is to store these in a file called `.env` in the root of your project folder.

**Never share this file or commit it to GitHub!**

Create the `.env` file and add the following, replacing the placeholders with your actual values:

```env
# Your Discord Bot Token
DISCORD_TOKEN=your_discord_bot_token_here

# The ID of your Discord server
GUILD_ID=your_guild_id_here

# Your Trackmania login credentials (for Ubisoft Connect)
# It's highly recommended to create a new, free Ubisoft account for this
TRACKMANIA_API_USER=your_ubisoft_email
TRACKMANIA_API_PASSWORD=your_ubisoft_password

# Your Trackmania Club ID
CLUB_ID=your_club_id_here
```

### How to Find These Values:

- **`DISCORD_TOKEN`**:

  1.  Go to the [Discord Developer Portal](https://discord.com/developers/applications).
  2.  Click "New Application". Give it a name and agree to the terms.
  3.  Go to the "Bot" tab. Click "Add Bot", then "Yes, do it!".
  4.  Under the bot's username, click "Reset Token" to reveal your token. **Treat this like a password!**

- **`GUILD_ID`** (Your Server ID):

  1.  In the Discord app, go to User Settings > Advanced.
  2.  Turn on **Developer Mode**.
  3.  Right-click on your server's icon on the left and choose "Copy Server ID".

- **`TRACKMANIA_API_USER` & `PASSWORD`**:

  - It is **strongly recommended** to create a brand new, free-tier Trackmania account for the bot. Do not use your personal account. This account is only used to make API requests.

- **`CLUB_ID`**:
  1.  Go to the Trackmania website and log in.
  2.  Navigate to your club's page.
  3.  The URL will look something like `https://www.trackmania.com/clubs/12345`.
  4.  The number at the end is your `CLUB_ID`. In this example, it would be `12345`.
