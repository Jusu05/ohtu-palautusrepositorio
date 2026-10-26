import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Kurri")

        assert player.name == "Kurri"
        assert player.team == "EDM"
        assert player.goals == 37
        assert player.assists == 53
        assert player.points == 90

    def test_search_none_with_none_existing_player(self):
        player = self.stats.search("Player")
        assert player is None
        
    def test_search_team(self):
        team = self.stats.team("PIT")
        assert len(team) == 1
        assert team[0].name == "Lemieux"

    def test_top_teams_works(self):
        top = self.stats.top(1)
        
        assert top[0].name == "Gretzky"
        assert top[0].team == "EDM"
        assert top[0].goals == 35
        assert top[0].assists == 89
        assert top[0].points == 124
       
    
    

            