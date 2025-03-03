# Number Guessing Game

Welcome to the **Number Guessing Game**, a fun and interactive Python program where players guess a randomly generated number within a range. This game is perfect for practicing logical thinking and having fun at the same time!


## Features
- A random number is generated between 1 and 50 for each game.
- Players have **3 attempts** to guess the number correctly.
- Feedback is provided for each guess:
  - "The number is higher" or "The number is lower."
  - If all attempts are exhausted, the correct number is revealed.
- Option to replay the game after each round.

## How to Play
1. Try the game out on Google Colab by clicking this [link](https://tinyurl.com/gajinumguessinggame)
2. Clone or download this repository.
3. Open the `Number guessing game.ipynb` file in Jupyter Notebook or any compatible IDE.
4. Run the code and follow the prompts:
   - Enter your guess when prompted.
   - Receive feedback after each guess.
   - Try to guess the correct number within 3 attempts.
5. Decide whether to play again or exit.

## Requirements
- Python 3.6 or higher.
- Jupyter Notebook or a Python-compatible IDE.
- The `random` module (bundled with Python).

## Installation
1. Clone the repository using:
   ```bash
   git clone https://github.com/codewithgaji/Number-Guessing-Game.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Number-Guessing-Game
   ```
3. Open the `Number guessing game.ipynb` file in Jupyter Notebook or your preferred IDE.

## How It Works
1. The program generates a random number between 1 and 50 using the `random.randint()` function.
2. Players are prompted to guess the number.
3. The program provides feedback based on the player's input and counts the attempts.
4. If the player guesses correctly within 3 attempts, they win! Otherwise, the correct number is displayed.

## Sample Gameplay
```
Welcome to Gaji's Guessing Game :)
You get to choose a number between 1 and 50.
If the number is correct, you win. You have 3 attempts!
Choose a number between 1 & 50: 25
The number is higher, go higher!
Choose a number between 1 & 50: 40
The number is lower, go lower!
Choose a number between 1 & 50: 35
Congratulations, you win!
Would you like to play again? yes
```


