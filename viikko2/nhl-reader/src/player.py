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
