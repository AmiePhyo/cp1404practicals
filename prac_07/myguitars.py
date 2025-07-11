from guitar import Guitar

FILENAME = 'guitars.csv'
CURRENT_YEAR = 2025

def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()
    print("\nThese are my guitars sorted by year:")
    display_guitars(guitars)


def load_guitars(filename):
    """Load guitars from a CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    """Display the guitars sorted by year."""
    for i, guitar in enumerate(guitars, start=1):
        vintage_guitars = " (vintage)" if guitar.is_vintage(CURRENT_YEAR) else ""
        print(f"Guitar {i}: {guitar}{vintage_guitars}")



main()