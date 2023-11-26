from cli.prompts import ask_for_name, ask_for_age


from .prompts import ask_for_name, ask_for_age


def main():
    print("Welcome to My Project!")

    name = ask_for_name()
    age = ask_for_age()

    print(f"Hello, {name}! You are {age} years old.")


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
