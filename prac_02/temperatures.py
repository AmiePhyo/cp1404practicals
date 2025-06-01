def main():
    menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(menu)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Enter Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} C is equal to {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Enter Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} F is equal to {celsius:.2f} C")
        else:
            print("Invalid choice")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you")

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

main()
