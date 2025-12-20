import asyncio
from discord.ext import tasks
from src.storage.database import SessionLocal
from src.storage.repository import LeaderboardRepository, MapRepository
from src.discord.bot import bot_instance # Import the bot instance to send messages

class LeaderboardTracker:
    def __init__(self, bot):
        self.bot = bot
        self.db_session = SessionLocal()
        self.leaderboard_repo = LeaderboardRepository(self.db_session)
        self.map_repo = MapRepository(self.db_session)
        self.check_leaderboards.start()

    @tasks.loop(minutes=5)  # Run every 5 minutes
    async def check_leaderboards(self):
        print("Checking for leaderboard updates...")

        # 1. Get all tracked maps from the database
        tracked_maps = self.map_repo.get_all()
        if not tracked_maps:
            print("No maps are being tracked.")
            return

        for map_data in tracked_maps:
            # 2. Fetch new leaderboard data from the API (placeholder)
            # new_leaderboard_data = self.api_client.get_leaderboard(map_data.campaign_id, map_data.id)
            print(f"Fetching leaderboard for map: {map_data.name}")
            new_leaderboard_data = self._get_mock_leaderboard_data(map_data.id) # Placeholder

            # 3. Get the last known leaderboard from our database
            last_leaderboard = self.leaderboard_repo.get_latest_for_map(map_data.id)

            # 4. Compare and find new personal bests (placeholder)
            if last_leaderboard:
                new_pbs = self._compare_leaderboards(last_leaderboard.entries, new_leaderboard_data)
                if new_pbs:
                    print(f"Found {len(new_pbs)} new personal bests for {map_data.name}!")
                    # 5. Send notifications
                    await self._send_pb_notifications(new_pbs, map_data)
            
            # 6. Store the new leaderboard snapshot
            # This is a simplified version. You'd create a new Leaderboard and LeaderboardEntry objects.
            # self.leaderboard_repo.create(...) 
            print(f"Stored new leaderboard snapshot for {map_data.name}")


    @check_leaderboards.before_loop
    async def before_check(self):
        await self.bot.wait_until_ready()
        print("Leaderboard tracker is ready.")

    def _compare_leaderboards(self, old_entries, new_entries_data):
        # Placeholder logic for comparison
        print("Comparing leaderboards...")
        # In a real scenario, you'd compare scores for each player
        # and return a list of a new personal bests.
        return [] # Return an empty list for now

    async def _send_pb_notifications(self, new_pbs, map_data):
        # Placeholder for sending messages to a channel
        # You'd need to get a channel ID from config
        # channel = self.bot.get_channel(int(config.NOTIFICATION_CHANNEL_ID))
        # if channel:
        #     for pb in new_pbs:
        #         embed = ... create embed ...
        #         await channel.send(embed=embed)
        print("Sending PB notifications...")
        pass
        
    def _get_mock_leaderboard_data(self, map_id):
        # Returns some fake data for demonstration
        return [
            {'player_id': 'player1', 'score': 45000},
            {'player_id': 'player2', 'score': 46000},
        ]

# To start the tracker, you would instantiate it in your main bot file
# and pass the bot instance to it.
# e.g., leaderboard_tracker = LeaderboardTracker(bot_instance)
