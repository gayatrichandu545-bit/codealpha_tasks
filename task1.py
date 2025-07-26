import random

# Predefined list of 5 words
word_list = ["apple", "grape", "mango", "peach", "berry"]

# Randomly select a word from the list
word_to_guess = random.choice(word_list)
guessed_letters = []
attempts_left = 6

# Create a display version of the word (e.g., "_ _ _ _ _")
display_word = ["_" for _ in word_to_guess]

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Game loop
while attempts_left > 0 and "_" in display_word:
    print("Word: ", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabetic character.\n")
        continue

    if guess in guessed_letters:
        print("🔁 You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!\n")
        # Reveal the guessed letter(s) in display_word
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[i] = guess
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts_left}\n")

# Check win or lose
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("😢 Out of attempts! The word was:", word_to_guess)
