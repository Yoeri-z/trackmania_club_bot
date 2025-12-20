import asyncio
from discord.ext import tasks
from src.storage.database import SessionLocal
from src.storage.repository import RoomInfoRepository
from src.discord.bot import bot_instance # Import the bot instance to send messages
import discord

class RoomTracker:
    def __init__(self, bot):
        self.bot = bot
        self.db_session = SessionLocal()
        self.room_repo = RoomInfoRepository(self.db_session)
        self.message = None
        self.check_room_status.start()

    @tasks.loop(minutes=1)  # Run every minute
    async def check_room_status(self):
        print("Checking room status...")

        # 1. Get the room to track (for simplicity, we assume one room)
        # In a real app, you might get this from config or a database
        room_id = "your_club_room_id" 
        room_info = self.room_repo.get(room_id)

        # 2. Fetch new room state from the API (placeholder)
        # active_players = self.api_client.get_room_state(config.CLUB_ID, room_id)['active_players']
        import random
        active_players = random.randint(0, 32) # Placeholder
        
        print(f"Room {room_id} has {active_players} players.")

        # 3. Update the database
        if room_info:
            self.room_repo.update(room_id, active_players=active_players)
        else:
            # First time running, create the entry
            room_info = self.room_repo.create(id=room_id, name="Club Room", active_players=active_players)

        # 4. Update the Discord message
        await self._update_discord_message(room_info)


    @check_room_status.before_loop
    async def before_check(self):
        await self.bot.wait_until_ready()
        print("Room tracker is ready.")


    async def _update_discord_message(self, room_info):
        # You would get the channel ID from config
        # channel_id = int(config.ROOM_STATUS_CHANNEL_ID)
        # channel = self.bot.get_channel(channel_id)
        # if not channel:
        #     print("Room status channel not found.")
        #     return
        
        # For now, we don't send a message to avoid needing a channel ID
        print("Updating room status message (placeholder).")
        
        embed = discord.Embed(
            title="Club Room Status",
            description=f"**{room_info.active_players}** players online.",
            color=discord.Color.purple()
        )
        embed.set_footer(text=f"Last updated: {room_info.last_updated.strftime('%Y-%m-%d %H:%M:%S')}")

        # if self.message:
        #     await self.message.edit(embed=embed)
        # else:
        #     self.message = await channel.send(embed=embed)


# To start the tracker, you would instantiate it in your main bot file
# and pass the bot instance to it.
# e.g., room_tracker = RoomTracker(bot_instance)
