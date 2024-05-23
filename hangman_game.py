import random

def print_hangman(wrong):
    hangman_stages = [
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """
    ]
    print(hangman_stages[wrong])

def print_word(guessed_word):
    display = ""
    right_characters = 0
    for char in random_word:
        if char in guessed_word:
            display += char + " "
            right_characters += 1
        else:
            display += "_ "
    print(display.strip())
    return right_characters

def play_hangman():
    print("Welcome to Hangman")
    print("--------------------------------------")
    word_dictionary = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
    global random_word
    random_word = random.choice(word_dictionary)

    print("_ " * len(random_word))
    length_of_word_to_guess = len(random_word)
    amount_of_wrong_guesses = 0
    current_character_guessed = []
    current_letters_right = 0

    while amount_of_wrong_guesses < 6:
        guess = input("Guess a letter: ").lower()
        if guess in random_word:
            if guess not in current_character_guessed:
                current_character_guessed.append(guess)
                current_letters_right = print_word(current_character_guessed)
                if current_letters_right == length_of_word_to_guess:
                    print("You win!")
                    break
                else:
                    print(f"You have {6 - amount_of_wrong_guesses} attempts left")
            else:
                print("You already guessed that letter.")
        else:
            amount_of_wrong_guesses += 1
            print(f"You have {6 - amount_of_wrong_guesses} attempts left")
            print_hangman(amount_of_wrong_guesses)
            print_word(current_character_guessed)
            if amount_of_wrong_guesses == 6:
                print("You lose.")
                print(f"The word was '{random_word}'")
                break

if __name__ == "__main__":
    play_hangman()
