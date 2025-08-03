import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    wikipedia.set_lang("en")
    user_input = input("Enter page title: ")
    while user_input != "":
        try:
            page = wikipedia.page(user_input, auto_suggest=False)
            print(f"{page.title}")
            print(f"{page.summary}")
            print(f"{page.url}")
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{user_input}" does not match any pages. Try another id!')
        user_input = input("Enter page title: ")
    print("Thank you.")

main()
