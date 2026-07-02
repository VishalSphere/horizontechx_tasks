import random

# List of predefined words
word_list = ["python", "computer", "keyboard", "program", "hangman"]

# Select a random word
secret_word = random.choice(word_list)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("=" * 40)
print("        WELCOME TO HANGMAN")
print("=" * 40)

while incorrect_guesses < max_incorrect:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print(f"Incorrect Guesses Left: {max_incorrect - incorrect_guesses}")

    # Check if player has guessed all letters
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly.")
        break

    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong Guess!")

else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")