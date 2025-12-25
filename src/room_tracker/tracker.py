import asyncio
from discord.ext import tasks
from src.storage.database import SessionLocal
from src.storage.repository import RoomInfoRepository
import src.discord_bot.bot as bot


class RoomTracker:
    def __init__(self):
        self.db_session = SessionLocal()
        self.room_repo = RoomInfoRepository(self.db_session)

    def start(self):
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

        active_players = random.randint(0, 32)  # Placeholder

        print(f"Room {room_id} has {active_players} players.")

        # 3. Update the database
        if room_info:
            self.room_repo.update(room_id, active_players=active_players)
        else:
            # First time running, create the entry
            room_info = self.room_repo.create(
                id=room_id, name="Club Room", active_players=active_players
            )

        await bot.send_room_update(room_info)

    @check_room_status.before_loop
    async def before_check(self):
        await bot.instance.wait_until_ready()
        print("Room tracker is ready.")
