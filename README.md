# Rock-Paper-Scissors Game

This project has **two versions** of a Rock-Paper-Scissors game in Python:

1. **main.py**  
   - Uses `if-else` statements to decide the winner.  
   - No score or round data is stored.  
   - Prints the result of each round to the console only.

2. **match_case.py**  
   - Uses `match-case` statements to decide the winner.  
   - Keeps track of user wins, computer wins, and draws.  
   - Saves each round and the final summary to `scores.txt`.  
   - Supports Unicode characters like arrows (→) in the logs.

---

## Features

- Play multiple rounds against the computer.  
- Tracks scores: user wins, computer wins, draws.  
- Saves each round and final summary to a text file.  
- Handles invalid inputs.

---

## Requirements

- Python 3.10 or higher (because it uses `match-case`)  
- No extra libraries needed

---

## How to Play

### For `main.py` (simple if-else version)
Run the script:  
```bash
python main.py
```
- Enter rock, paper, or scissors when prompted.  
- Type quit to exit.  
- Only the result of the round will be shown; no data is saved.   

### For `match_case.py` (data storage version)
Run the script:  
```bash
python match_case.py
```
- Enter rock, paper, or scissors when prompted.
- Type quit to exit.
- Each round’s result and the final score summary will be saved to scores.txt.

---

## Example Output
### For main.py
Enter rock, paper, scissors, or quit: rock  
Computer chose: scissors   
You Win!  
Scoreboard → You: 1 | Computer: 0 | Draws: 0  
  
Enter rock, paper, scissors, or quit: quit  
Thanks for playing! Final Scoreboard:  
You: 1 | Computer: 0 | Draws: 0  

### For match_case.py
Enter rock, paper, scissors, or quit: rock  
User: 1 | Computer: 0 → You Win!  
Enter rock, paper, scissors, or quit: paper  
User: 1 | Computer: 1 → Computer wins!  
Enter rock, paper, scissors, or quit: quit  
User Score: 1  
Computer Score: 1  
Draws: 0  

---

## License  
This project is free to use and open-source.
