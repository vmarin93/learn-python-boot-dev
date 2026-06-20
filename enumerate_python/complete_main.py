def display_damage_meter(players_dps: list[dict]) -> None:
    for rank, player in enumerate(players_dps, start=1):
        print(f"{rank}. {player['name']} - {player['dps']} dps")
