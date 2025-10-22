"""project_2.py: 
second project for Engeto Online Python Academy

Author: Michaela Papadimitriu Ludvikova
email: mludvik2@yahoo.com
"""
import random

def generate_secret_num() -> str:
    """Generate a random 4-digit number with unique
      digits and no zero at the beginning
      """
    while True:
        digits = random.sample('0123456789', 4)
        if digits[0] != '0':
            return ''.join(digits)
        
def is_valid_guess(guess: str) -> bool:
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

def count_bulls_and_cows(secret: str, guess: str) -> tuple [int, int]:
    """Counting Bulls and Cows.
    Bulls: correct position
    Cows: correct digit but wrong position
    """
    cows = 0
    bulls = 0
    
    unmatched_secret = []
    unmatched_guess = []

    for s, g in zip(secret, guess):
        if s == g:
            bulls += 1
        else:
            unmatched_secret.append(s)
            unmatched_guess.append(g)
    for g in unmatched_guess:
        if g in unmatched_secret:
            cows += 1
            unmatched_secret.remove(g)
    return bulls, cows

def play_game():
    """Main game loop.
    The Player keeps playing untill the secret number
     is guessed.
    """
    print("Hi there!")
    print("-" * 60)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 60)
    
    secret = generate_secret_num()
    print(secret)   ### remove afterwards

    tries = 0

    while True:
        guess = input("Enter a number: ").strip()
        print("-" * 60)

        if not is_valid_guess(guess):
            print("-" * 60)
            continue
        
        tries += 1

        if guess == secret:
            if tries == 1:
                print(f"Correct, you've guessed the right number in {tries} guess!")
            else:
                print(f"Correct, you've guessed the right number in {tries} guesses!")
            print("-" * 60)
            print("That's amazing!")
            print("-" * 60)
            return tries
        
        bulls, cows = count_bulls_and_cows(secret, guess)
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        print(f"Number of guesses: {tries}")
        print("-" * 60)

def main():
    """Let the Player replay and see their stats."""
    all_tries = []

    while True:
        tries = play_game()
        all_tries.append(tries)

        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("-" * 60)
            print("Thank you for playing! Here are your results: ")
            print(f"Games played: {len(all_tries)}")
            print("Goodbye!")
            print("-" * 60)
            break

main()



#remove comment and print of secret number

