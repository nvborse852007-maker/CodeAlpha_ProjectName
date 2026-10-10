import random

# List of 5 predefined words
words = ["python", "apple", " tiger", "school", "computer"]

# Randomly select a word
word = random.choice(words).strip()
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6
print("Welcome to Hangman!")
print("_ " * len(word))

# Game loop
while incorrect_guesses < max_attempts:
    # Display the current word progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)

    # Check if the player has guessed the word
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    # Get the player's guess
    guess = input("Guess a letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Display the final result
if incorrect_guesses == max_attempts:
    print("\nGame over! The word was:", word)