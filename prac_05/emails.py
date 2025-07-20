"""
emails
Estimate: 30 minutes
Actual: 25 minutes
"""

def main():
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        guessed_name = extract_name_from_email(email)
        confirmation = input(f"Is your name {guessed_name}? (Y/n) ").strip().lower()

        if confirmation in ('', 'y', 'yes'):
            name = guessed_name
        else:
            name = input("Name: ").strip()

        email_to_name[email] = name

        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name_from_email(email):
    parts = email.split('@')[0]
    words = parts.replace('.', ' ').split()
    return ' '.join(words).title()

main()