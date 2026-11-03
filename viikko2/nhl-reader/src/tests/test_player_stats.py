import os
import sys

# Ensure src is on path so we can import modules under test
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from player_stats import PlayerStats
from player import Player


class StubReader:
    """Simple reader stub that returns a fixed list of Player objects.

    This avoids network access and mirrors the interface used by PlayerStats.
    """

    def __init__(self, players):
        self._players = players

    def get_players(self):
        return self._players


def make_player(name, nationality, goals, assists, team="T", games=1):
    return Player({
        'name': name,
        'nationality': nationality,
        'assists': assists,
        'goals': goals,
        'team': team,
        'games': games,
    })


def test_top_goal_scorers_returns_top_n():
    p1 = make_player('A', 'FIN', 10, 0)
    p2 = make_player('B', 'SWE', 5, 0)
    p3 = make_player('C', 'CAN', 7, 0)

    reader = StubReader([p1, p2, p3])
    stats = PlayerStats(reader)

    top2 = stats.top_goal_scorers(2)

    # Expect players with 10 and 7 goals in that order
    assert top2 == [p1, p3]


def test_top_goal_scorers_when_how_many_exceeds_players():
    p1 = make_player('A', 'FIN', 3, 1)
    reader = StubReader([p1])
    stats = PlayerStats(reader)

    top5 = stats.top_goal_scorers(5)
    # Should simply return all available players
    assert top5 == [p1]


def test_top_scorers_by_nationality_filters_and_sorts():
    # Two Finnish players and one Swedish player
    p1 = make_player('Finn1', 'FIN', 4, 6)   # total 10
    p2 = make_player('Finn2', 'FIN', 5, 2)   # total 7
    p3 = make_player('Swe1', 'SWE', 10, 0)   # total 10

    reader = StubReader([p1, p2, p3])
    stats = PlayerStats(reader)

    top_fin = stats.top_scorers_by_nationality('FIN')

    # Expect only FIN players sorted by (goals + assists) descending
    assert top_fin == [p1, p2]
