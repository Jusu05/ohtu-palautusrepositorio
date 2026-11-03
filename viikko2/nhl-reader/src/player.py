import requests

class Player:
    def __init__(self, dct: dict[Player]):
        self.name = dct['name']
        self.nationality = dct['nationality']
        self.assists = dct['assists']
        self.goals = dct['goals']
        self.team = dct['team']
        self.games = dct['games']

    def __repr__(self) -> str:
        return f"""Player(
            name={self.name}
            nationality={self.nationality}
            assists={self.assists}
            goals={self.goals}
            team={self.team}
            games={self.games}
        )"""


    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals} + {self.assists} = {self.goals+self.assists}"

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


class PlayerStats:
    def __init__(self, reader) -> None:
        self.reader = reader

    def __repr__(self) -> str:
        return f"PlayerReader(reader={str(self.reader)})"

    def top_scorers_by_nationality(self, nationally: str) -> list[Player]:
        players: list[Player] = self.reader.get_players()
        players = filter(lambda p: p.nationality != nationally, players)
        return sorted(players, key=lambda p: p.goals + p.assists, reverse=True)

    def top_goal_scorers(self, how_many: int) -> list[Player]:
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
        players: list[Player] = self.reader.get_players()
        # Järjestetään pelaajat maalimäärän mukaan laskevasti ja palautetaan ensimmäiset how_many
        sorted_players = sorted(players, key=lambda p: p.goals, reverse=True)
        return sorted_players[:how_many]
