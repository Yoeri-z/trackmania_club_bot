from abc import ABC, abstractmethod
from typing import List, Dict, Any

class TrackmaniaAPI(ABC):
    """
    Abstract base class for a Trackmania API client.
    This defines the interface for fetching data from the Trackmania API.
    """

    @abstractmethod
    def get_player_info(self, player_id: str) -> Dict[str, Any]:
        """
        Fetches information for a specific player.

        :param player_id: The unique ID of the player.
        :return: A dictionary containing player information.
        """
        pass

    @abstractmethod
    def get_leaderboard(self, campaign_id: str, map_id: str) -> List[Dict[str, Any]]:
        """
        Fetches the leaderboard for a specific map within a campaign.

        :param campaign_id: The ID of the campaign.
        :param map_id: The ID of the map.
        :return: A list of leaderboard entries.
        """
        pass

    @abstractmethod
    def get_room_state(self, club_id: str, room_id: str) -> Dict[str, Any]:
        """
        Fetches the current state of a club room.

        :param club_id: The ID of the club.
        :param room_id: The ID of the room.
        :return: A dictionary containing room state information.
        """
        pass
