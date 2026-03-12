import random

choices = ["rock", "paper", "scissors"]

def play_game():
    computer = random.choice(choices)

    print("Rock, Paper, Scissors Game")
    player = input("Enter rock, paper, or scissors: ").lower()

    if player not in choices:
        print("Invalid choice!")
        return

    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("🎉 You win!")

    else:
        print("💻 Computer wins!")

from game import play_game

def main():
    while True:
        play_game()

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()       