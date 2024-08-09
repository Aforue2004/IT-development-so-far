from hangman import select_word, displaying_word, hangman_game, logo

print(logo)
print()

print()
print("-----------------------------------------")
print("\t\tGAME MENU")
print("-----------------------------------------")
print()


# The Main Menu of the game
# choose a category
def play_hangman():
    while True:
        print("Welcome to Hangman Game!🚀🚀")
        print("Please select a category to play:")
        print("1. DC characters🦸")
        print("2. Marvel characters🦸")
        print("3. Nigerian Name📃")
        print("Press 'Q' to Quit")
        # this handles the option to quit
        choice = input("Enter your choice (1-3): ").strip()
        if choice.lower() == 'q':
            print("Thank you for playing!")
            break
        # this handles the error of invalid option
        if choice not in ['1', '2', '3']:
            print()
            print("Invalid choice! Please enter a number between 1 and 3.")
            print()
            continue

        category = {
            '1': "DC characters",
            '2': "Marvel characters",
            '3': "Nigerian Name",
        }[choice]

        word = select_word(category)
        print()
        print(f"Category: {category}")
        print("Guess the Word:", displaying_word(word, []))
        print()
        hangman_game(word)


# runs the game on the terminal
if __name__ == '__main__':
    play_hangman()
