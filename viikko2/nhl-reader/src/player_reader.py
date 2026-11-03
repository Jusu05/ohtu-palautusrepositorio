import requests
from player import Player

class PlayerReader:
    def __init__(self, url: str) -> None:
        self._players = self._load_players(url)

    def __repr__(self) -> str:
        return f"PlayerReader(_players={type(self._players)})"

    def _load_players(self, url: str) -> list[Player]:
        response = requests.get(url, timeout=250).json()
        return [Player(player_dict) for player_dict in response]

    def get_players(self) -> list[Player]:
        return self._players
