import random

def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

def is_valid_guess(guess, guesses):
    return guess in guesses

def evaluate_guess(guess, word):
    str = ""

    for i in range(5):
        if guess[i] == word[i]:
            str += "\033[32m" + guess[i]
        else:
            if guess[i] in word:
                str += "\033[33m" + guess[i]
            else:
                str += "\033[0m" + guess[i]
    
    return str + "\033[0m"

def wordle(guesses, answers):
    print()
    print()
    print()
    print()
    print()
    print("Welcome to Wordle! Get 6 chances to guess a 5-letter word.")
    secret_word = random.choice(answers)

    attempts = 1
    max_attempts = 6

    while attempts <= max_attempts:
        guess = input("Enter Guess #" + str(attempts) + ": ").lower()
        if not is_valid_guess(guess, guesses):
            print("Invalid guess. Please enter an English word with 5 letters.")
            continue
        if guess == secret_word:
            print("Congratulations! You guessed the word: ", secret_word)
            break

        attempts += 1
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)
    
    if attempts > max_attempts:
        print("Game over. The secret word was: ", secret_word)

guesses = load_dictionary("guesses.txt")
answers = load_dictionary("answers.txt")

# wordle(guesses, answers)

str = "\t" + "\033[33m" + "A" + "\033[0m" + "UDIO"
str += "\n\t" + "SLEP" + "\033[32m" + "T"
str += "\n\t" + "\033[33m" + "RA" + "\033[0m" + "N" + "\033[33m" + "CH"
str += "\n\t" + "\033[32m" + "CHART" + "\033[0m"

print()
print()
print()
print()
print("   Welcome to Wordle!")
print()
print(str)
print()
print("    Congratulations!\n      You guessed \n    the word: " + "\033[32m" + "CHART")
print()
print()
print()