import random

def start_game():
    number = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to Guess My Number!")
    print("I am thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("📉 Too low! Try again.")

        elif guess > number:
            print("📈 Too high! Try again.")

        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break
from game import start_game

def main():
    start_game()

if __name__ == "__main__":
    main()
