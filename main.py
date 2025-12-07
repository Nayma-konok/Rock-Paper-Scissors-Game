import random

choices = ["rock", "paper", "scissors"]

user_scores=0
computer_scores=0
draws=0

while True:
    user=input("Enter rock, paper, scissors, or quit:").lower()
    computer = random.choice(choices)

    if user == "quit":
        break
    elif user == "rock":
        if computer == "scissors":
            print("You Win!")
            user_scores += 1
        elif computer == "paper":
            print("Computer Wins!")
            computer_scores += 1
        else:
            print("Draw!")
            draws += 1
    elif user =="paper":
        if computer == "scissors":
            print("Computer Wins!")
            computer_scores += 1
        elif computer == "rock":
            print("You Win!")
            user_scores += 1
        else:
            print("Draw!")
            draws += 1
    elif user =="scissors":
        if computer == "paper":
            print("You Win!")
            user_scores += 1
        elif computer == "rock":
            print("Computer Wins!")
            computer_scores += 1
        else:
            print("Draw!")
            draws += 1
    else:
        print("Invalid Choice")
    

    print(f"Computer chose: {computer}")
    print(f"Scoreboard → You: {user_scores} | Computer: {computer_scores} | Draws: {draws}")  

print("Thanks for playing! Final Scoreboard:")
print(f"You: {user_scores} | Computer: {computer_scores} | Draws: {draws}")  

