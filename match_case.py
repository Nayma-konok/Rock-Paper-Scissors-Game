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
            user_scores += 1
            result=f"User: {user_scores} | Computer: {computer_scores} → You Win!"
        case ("rock", "paper")|("paper", "scissors")|("scissors", "rock"):
            computer_scores += 1
            result=f"User: {user_scores} | Computer: {computer_scores} → Computer wins!"
        case ("rock", "rock")|("paper", "paper")|("scissors", "scissors"):
            draws += 1
            result=f"User: {user_scores} | Computer: {computer_scores} → DRAW.."
        case _:
            print("Invalid Choice")
            continue

    with open("scores.txt","a", encoding="utf-8") as file:
        file.write(result+ "\n")

with open("scores.txt","a", encoding="utf-8") as file:
    file.write(f"User Score: {user_scores}\n")
    file.write(f"Computer Score: {computer_scores}\n")
    file.write(f"Draws: {draws}\n")

