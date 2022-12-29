import random

# source: https://inventwithpython.com/bigbookpython/project1.html

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f"I am thinking of a {NUM_DIGITS} number w/ no repeated digits")

    while True:
        secretNum = getSecretNum()
        print("I have a number to guess")
        print(f"You have {MAX_GUESSES} guesses to get it")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess {numGuesses}")
                guess = input(">")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses")
                print(f"The answer was {secretNum}")

        print("Do you want to play again? (y/n)")
        if not input(">").lower().startswith("y"):
            break
    print("Thanks for playing")


def getSecretNum():
    numbers = list("0123456789")
    random.shuffle(numbers)

    secretNum
