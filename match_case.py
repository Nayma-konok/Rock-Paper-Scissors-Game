import random

choices = ["rock", "paper", "scissors"]

user_scores=0
computer_scores=0
draws=0

while True:
    user=input("Enter rock, paper, scissors, or quit:").lower()

    if user == "quit":
        break

    computer = random.choice(choices)


    match (user, computer):
        case ("rock", "scissors")|("paper", "rock")|("scissors", "paper"): 
            print("You win!")
            user_scores += 1
        case ("rock", "paper")|("paper", "scissors")|("scissors", "rock"):
            print("Computer wins!")
            computer_scores += 1
        case ("rock", "rock")|("paper", "paper")|("scissors", "scissors"):
            print("Draw")
            draws += 1
        case _:
            print("Invalid Choice")
        

    print(f"Computer chose: {computer}")
    print(f"Scoreboard → You: {user_scores} | Computer: {computer_scores} | Draws: {draws}")  

print("Thanks for playing! Final Scoreboard:")
print(f"You: {user_scores} | Computer: {computer_scores} | Draws: {draws}")  
