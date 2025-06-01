def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    password = input("Enter password: ")
    while len(password) < 5:
        password = input("Password too short. Enter again: ")
    return password

def print_asterisks(password):
    print('*' * len(password))

main()
