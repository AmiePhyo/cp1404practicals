"""
Guitar class tester for CP1404/CP5632 Practical

Estimate: 15 minutes
Actual: 20 minutes
"""

from guitar import Guitar

CURRENT_YEAR = 2022

def main():

    my_guitar = Guitar("Gibson L-5 CES",1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1000.40)

    # Test get_age()
    print(f"{my_guitar.name} get_age() - Expected 100. Got {my_guitar.get_age(CURRENT_YEAR)}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age(CURRENT_YEAR)}")

    # Test is_vintage()
    print(f"{my_guitar.name} is_vintage() - Expected True. Got {my_guitar.is_vintage(CURRENT_YEAR)}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage(CURRENT_YEAR)}")

main()