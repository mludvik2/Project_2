"""project_2.py: 
second project for Engeto Online Python Academy

Author: Michaela Papadimitriu Ludvikova
email: mludvik2@yahoo.com
"""
import random

def generate_secret_num() -> str:
    """Generate a random 4-digit number with unique
      numbers and no zero at the beginning
      """
    while True:
        num = random.sample('0123456789',4)
        if num[0] != '0':
            number = ''.join(num)
            return number
        
def is_valid_guess(guess):
    """Check if the input guess is valid:
    -must be 4 digits long
    -must contain only numbers
    -must not start with 0
    -must not repeat digits
    """
    if not guess.isdigit():
        print("Invalid input. Please add numbers only.")
        return False
    if len(guess) != 4:
        print("You have not chosen a 4 digit number.")
        return False
    if guess[0] == '0':
        print("You cannot start your guess with zero.")
        return False
    digit_collection = []
    for digit in guess:
        if digit in digit_collection:
            print("All the numbers must be unique. No repetition.")
            return False
        digit_collection.append(digit)
    return True

def count_bulls_and_cows(secret, guess):
    """Counting Bulls and Cows.
    Bulls: correct digit and correct position
    Cows: correct digit but wrong position (not counting bulls)
    """
    cows = 0
    bulls = 0
    counted_secret_positions = []
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
            counted_secret_positions.append(i)
    for i in range(4):
        if guess[i] != secret[i]:
            for j in range(4):
                if j not in counted_secret_positions and guess[i] == secret[j]:
                    cows += 1
                    counted_secret_positions.append(j)
                    break
    return bulls, cows

def play_game():
    """Main game loop.
    The Player keeps playing untill the secret number
     is guessed.
    """
    print("Hi there!")
    print("-" * 40)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 40)
    
    secret = generate_secret_num()
    print(secret)   ### remove afterwards

    tries = 0

    while True:
        guess = input("Enter a number: ").strip() ##To remove any spaces from the Player's input
        print("-" * 40)

        if not is_valid_guess(guess):
            print("-" * 40)
            continue
        
        tries += 1

        if guess == secret:
            if tries == 1:
                print(f"Correct, you've guessed the right number in {tries} guess!")
            else:
                print(f"Correct, you've guessed the right number in {tries} guesses!")
            print("-" * 40)
            print("That's amazing!")
            break
        
        bulls, cows = count_bulls_and_cows(secret, guess)
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        print(f"Number of guesses: {tries}")
        print("-" * 40)

play_game()