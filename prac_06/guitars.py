"""
Guitar collection program

Estimate: 20 minutes
Actual: 18 minutes
"""

from guitar import Guitar


def main():
    """Get guitar data from user and display formatted results."""
    print("My guitars!")
    guitars = []

    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $").replace(",", ""))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(2022) else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
