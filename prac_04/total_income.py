"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    income_report(incomes)

def income_report(incomes):
    # This function will print income report
    print("\nIncome Report\n-------------")
    total = 0
    for i in range(len(incomes)):
        income = incomes[i]
        total += income
        print(f"Month {i + 1:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
