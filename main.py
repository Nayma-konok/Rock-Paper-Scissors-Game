import random

user=input("Enter rock, paper, scissors, or quit:")

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

if user == "rock":
    if computer == "scissors":
        print("You Win!")
    elif computer == "paper":
        print("Computer Wins!")
    else:
        print("Draw!")
elif user =="paper":
    if computer == "scissors":
        print("Computer Wins!")
    elif computer == "rock":
        print("You Win!")
    else:
        print("Draw!")
elif user =="scissors":
    if computer == "paper":
        print("You Win!")
    elif computer == "rock":
        print("Computer Wins!")
    else:
        print("Draw!")
else:
    print("Quit")