def main():
    score = get_valid_score()
    choice = ""
    while choice != "Q":
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result for score {score}: {result}")
        elif choice == "S":
            print("*" * score)
        elif choice == "Q":
            print("Thank you.")
        else:
            print("Invalid choice.")

def print_menu():
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def get_valid_score():
    score = int(input("Enter a valid score (0–100): "))
    while score < 0 or score > 100:
        print("Invalid score.")
        score = int(input("Enter a valid score (0–100): "))
    return score

def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Pass"
    else:
        return "Bad"

main()
