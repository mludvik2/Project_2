# Cows and Bulls Game

**Author:** Michaela Papadimitriu Ludvikova  
**Email:** mludvik2@yahoo.com  
**Course:** Engeto Online Python Academy — Project 2  

## Description  

This is a simple console-based **Bulls and Cows** game written in Python. The computer generates a **random 4-digit number** with unique digits, and your goal is to guess it.
- Each digit is unique.
- The number does **not** start with zero.
After each guess, the program gives feedback:
- **Bulls** – number of digits that are correct **and in the correct position.**
- **Cows** – number of digits that are correct but **in the wrong position.**

The game continues until you guess the secret number correctly. The program also tracks the number of attempts and allows you to play multiple rounds.

**How to Play**
1. Run the game:
```
python main.py
```
2. The program will greet you and generate a secret 4-digit number.
3. Enter a valid 4-digit guess. Rules for guesses:
 - Must be **exactly 4 digits long.**
 - Must contain **only numbers.**
 - Cannot start with **0.**
 - All digits must be **unique.**
4. After each guess, the program will display:
 - Number of **bulls** (correct digits in the correct place)
 - Number of **cows** (correct digits in the wrong place)
 - Total number of guesses so far
5. Repeat guessing until you find the correct number.
6. After each game, you can choose to play again or exit. The program will summarize your stats at the end.