"""
Wimbledon
Estimate: 30 minutes
Actual:   45 minutes
"""

FILENAME = "wimbledon.csv"

def main():
    data = read_wimbledon(FILENAME)

    champions_to_wins = get_champion_win_counts(data)
    print("Wimbledon Champions:")
    for champion, wins in champions_to_wins.items():
        print(f"{champion:20} {wins}")

    countries = get_countries_of_champions(data)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

def read_wimbledon(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()
        return [line.strip().split(",") for line in file]

def get_champion_win_counts(records):
    win_counts = {}
    for record in records:
        champion = record[2]
        win_counts[champion] = win_counts.get(champion, 0) + 1
    return win_counts

def get_countries_of_champions(data):
    countries = {record[1] for record in data}
    return sorted(countries)

main()