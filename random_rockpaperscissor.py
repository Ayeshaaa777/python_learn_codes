import random

choices = ["rock", "paper", "scissors"]

# Ask the user to make a choice
user_choice = input("Choose rock, paper, or scissors: ").lower()

# Generate a random choice for the computer
computer_choice = random.choice(choices)

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissors") or
    (user_choice == "paper" and computer_choice == "rock") or
    (user_choice == "scissors" and computer_choice == "paper")
):
    print("You win!")
else:
    print("Computer wins!")
