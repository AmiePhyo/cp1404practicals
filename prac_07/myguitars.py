from guitar import Guitar

FILENAME = 'guitars.csv'
CURRENT_YEAR = 2025

def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()
    print("\nThese are my guitars sorted by year:")
    display_guitars(guitars)

    new_guitars = get_new_guitars()
    guitars.extend(new_guitars)

    save_guitars(FILENAME, guitars)


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

def get_new_guitars():
    """Get new guitars from the user"""
    print("\nNew guitars:")
    new_guitars = []
    name = input("Enter guitar name: ")
    while name != "":
        try:
            year = input("Enter guitar year: ")
            cost = input("Enter guitar cost: ")
            new_guitars.append(Guitar(name, int(year), float(cost)))
            print("New guitar is added.")
        except ValueError:
            print("Invalid input.")
        name = input("Enter guitar name: ")
    return new_guitars

def save_guitars(filename, guitars):
    """Save all guitars to the CSV file"""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

main()