from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from player import PlayerReader, PlayerStats

def plyer_table(season, nationally, players):
    table = Table(title=f"Season {season} players form {nationally}")
    table.add_column("Player", style="cyan", no_wrap=True)
    table.add_column("teams", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.goals + player.assists),
        )

    console = Console()
    console.print(table)

def main():
    seasons = ["2018-19","2019-20","2020-21","2021-22","2022-23","2023-24","2024-25","2025-26"]
    nationalities = [
        "USA","FIN","CAN","SWE","CZE","RUS","SLO",
        "FRA","GBR","SVK","DEN","NED","AUT","BLR",
        "GER","SUI","NOR","UZB","LAT","AUS"
    ]

    season = Prompt.ask("Season", choices=seasons, default="2024-25")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationally = Prompt.ask("Nationally", choices=nationalities, default="")
        players = stats.top_scorers_by_nationality(nationally)
        plyer_table(season, nationally, players)

if __name__ == "__main__":
    main()
