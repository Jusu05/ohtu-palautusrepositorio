import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']

    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals} + {self.assists} = {self.goals+self.assists}"

class PlayerReader:
    def __init__(self, url: str) -> None:
        self._players = self._load_players(url)

    def _load_players(self, url: str) -> list[Player]:
        response = requests.get(url).json()
        return [Player(player_dict) for player_dict in response]

    def get_players(self) -> list[Player]:
        return self._players

class PlayerStats:
    def __init__(self, reader) -> None:
        self.reader = reader

    def top_scorers_by_nationality(self, nationally: str) -> list[Player]:
        players = self.reader.get_players()
        players = filter(lambda p: p == nationally, players)
        return list(sorted(players, key=lambda p: p.goals + p.assists))
