import discord
from discord.ext import commands
from src.config import config
from src.storage.database import SessionLocal
from src.storage.repository import PlayerRepository
from src.leaderboard_tracker.tracker import LeaderboardTracker
from src.room_tracker.tracker import RoomTracker

class TrackmaniaBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True  # Required to read message content
        super().__init__(command_prefix='!', intents=intents)
        self.leaderboard_tracker = None
        self.room_tracker = None

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        print('Bot is ready to receive commands.')

    async def setup_hook(self) -> None:
        # This is where you would load your cogs (extensions)
        # For now, we will add commands directly for simplicity
        self.add_command(player)
        self.add_command(leaderboard)
        
        # Start the trackers
        self.leaderboard_tracker = LeaderboardTracker(self)
        self.room_tracker = RoomTracker(self)


bot_instance = TrackmaniaBot()

@commands.command(name='player')
async def player(ctx, *, player_name: str):
    """
    Fetches information about a Trackmania player.
    
    Usage: !player <player_name>
    """
    # In a real implementation, you would use the Trackmania API
    # and the database to get player information.
    # For now, this is a placeholder.
    
    db_session = SessionLocal()
    player_repo = PlayerRepository(db_session)
    
    # This is a mock search. You'd need a way to find a player by name.
    # For now, we'll just pretend we found one.
    # found_player = player_repo.get(player_name) # This would need a lookup by name
    
    embed = discord.Embed(
        title=f"Player Information: {player_name}",
        description=f"Showing information for player '{player_name}'.",
        color=discord.Color.blue()
    )
    # embed.add_field(name="ID", value=found_player.id if found_player else "N/A", inline=False)
    # embed.add_field(name="Last Seen", value=found_player.last_updated if found_player else "N/A", inline=False)
    embed.add_field(name="Note", value="This is placeholder data.", inline=False)
    
    await ctx.send(embed=embed)
    db_session.close()

@commands.command(name='leaderboard')
async def leaderboard(ctx, map_name: str = "Default Map"):
    """
    Shows the leaderboard for a specific map.

    Usage: !leaderboard [map_name]
    """
    # Placeholder for leaderboard command
    embed = discord.Embed(
        title=f"Leaderboard: {map_name}",
        description="Top 10 Players",
        color=discord.Color.green()
    )
    
    # Mock data
    for i in range(1, 11):
        embed.add_field(name=f"#{i} Player {i}", value=f"Time: 00:45.{i:03}", inline=False)
        
    await ctx.send(embed=embed)


def run_bot():
    if not config.DISCORD_TOKEN:
        print("DISCORD_TOKEN is not set. Please check your .env file or environment variables.")
        return
    
    bot_instance.run(config.DISCORD_TOKEN)
