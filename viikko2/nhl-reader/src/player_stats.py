from player import Player

class PlayerStats:
    def __init__(self, reader) -> None:
        self.reader = reader

    def __repr__(self) -> str:
        return f"PlayerReader(reader={str(self.reader)})"

    def top_scorers_by_nationality(self, nationally: str) -> list[Player]:
        players: list[Player] = self.reader.get_players()
        players = filter(lambda p: p.nationality == nationally, players)
        return sorted(players, key=lambda p: p.goals + p.assists, reverse=True)

    def top_goal_scorers(self, how_many: int) -> list[Player]:
        """
        Palauttaa how_many eniten maaleja tehnyttä pelaajaa
        maalimäärän mukaan laskevassa järjestyksessä
        """
        players: list[Player] = self.reader.get_players()
        # Järjestetään pelaajat maalimäärän mukaan laskevasti ja palautetaan ensimmäiset how_many
        sorted_players = sorted(players, key=lambda p: p.goals, reverse=True)
        return sorted_players[:how_many]