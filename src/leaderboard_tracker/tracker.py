from discord.ext import tasks
from src.storage.database import SessionLocal
from src.storage.repository import LeaderboardRepository, MapRepository
from src.storage.models import LeaderboardEntry, Map
import src.discord_bot.bot as bot


class LeaderboardTracker:

    def __init__(self):
        self.db_session = SessionLocal()
        self.leaderboard_repo = LeaderboardRepository(self.db_session)
        self.map_repo = MapRepository(self.db_session)
        self.current_map_index = 0

    def start(self):
        self.check_leaderboards.start()

    @tasks.loop(seconds=20)
    async def check_leaderboards(self):
        tracked_maps = self.map_repo.get_tracked()
        if not tracked_maps or tracked_maps == []:
            print("No maps are being tracked.")
            return

        if self.current_map_index >= len(tracked_maps):
            self.current_map_index = 0

        map_data = tracked_maps[self.current_map_index]

        # TODO: replace this with api call
        leaderboard_data = self._get_mock_leaderboard_data(map_data.id)

        if leaderboard_data:
            new_pbs = self._compare_leaderboards(leaderboard_data)

        self.current_map_index += 1

    @check_leaderboards.before_loop
    async def before_check(self):
        await bot.instance.wait_until_ready()
        print("Leaderboard tracker is ready.")

    def _compare_leaderboards(self, entries: list[LeaderboardEntry]):
        for entry in entries:
            new_entry, old_entry = self.leaderboard_repo.compare(entry)
            if new_entry:
                bot.send_position_update(entry.map.channel_id, entry, old_entry)

    def _get_mock_leaderboard_data(self, map_id) -> list[LeaderboardEntry]:
        # Returns some fake data for demonstration
        return [
            {"player_id": "player1", "score": 45000},
            {"player_id": "player2", "score": 46000},
        ]
