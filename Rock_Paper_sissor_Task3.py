import random

options = ("rock", "paper", "scissors")
running = True

while running:
    while True:
        player = input("Enter a choice (rock, paper, scissors):")
        if player in options:
            break
        else:
            print("Invalid choice. Please choose from 'rock', 'paper', or 'scissors'.")

    computer = random.choice(options)

    print("Player:", player)
    print("Computer:", computer)

    if player == computer:
        print("It's a tie")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("You win")
    else:
        print("You lose")

    play = input("Want to play again? (y/n):").lower()
    if play != 'y':
        running = False

print("Thanks For Playing")
