"""project_2.py: 
second project for Engeto Online Python Academy

Author: Michaela Papadimitriu Ludvikova
email: mludvik2@yahoo.com
"""
import random

num_digits = 4
separator = "-" * 60

def generate_secret_num() -> str:
    """Generate a random 4-digit number with unique
      digits and no zero at the beginning
      """
    while True:
        digits = random.sample('0123456789', num_digits)
        if digits[0] != '0':
            return ''.join(digits)
        
def is_valid_guess(guess: str) -> bool:
    """Check if the input guess is valid:
    -must be 4 digits long
    -must contain only numbers
    -must not start with 0
    -must not repeat digits
    """
    if not guess.isdigit() or len(guess) != num_digits or guess[0] == '0' or len(set(guess)) != len(guess):
        if not guess.isdigit():
            print("Invalid input. Please add numbers only.")
        elif len(guess) != num_digits:
            print(f"You have not chosen a {num_digits} digit number.")
        elif guess[0] == '0':
            print("You cannot start your guess with zero.")
        else:
            print("All the numbers must be unique. No repetition.")
        return False
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

    used_secret = [False] * len(unmatched_secret)

    for g in unmatched_guess:
        for i, s in enumerate(unmatched_secret):
            if not used_secret[i] and g == s:
                cows += 1
                used_secret[i] = True
                break

    return bulls, cows

def play_game():
    """Main game loop.
    The Player keeps playing untill the secret number
     is guessed.
    """
    print("Hi there!")
    print(separator)
    print(f"I've generated a random {num_digits} digit number for you.")
    print("Let's play a bulls and cows game.")
    print(separator)
    
    secret = generate_secret_num()

    tries = 0

    while True:
        guess = input("Enter a number: ").strip()
        print(separator)

        if not is_valid_guess(guess):
            continue
        
        tries += 1

        if guess == secret:
            if tries == 1:
                print(f"Correct, you've guessed the right number in {tries} guess!")
            else:
                print(f"Correct, you've guessed the right number in {tries} guesses!")
            print(separator)
            print("That's amazing!")
            return tries
        
        bulls, cows = count_bulls_and_cows(secret, guess)
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
        print(f"Number of guesses: {tries}")
        print(separator)

def main():
    """Let the Player replay and see their stats."""
    all_tries = []

    while True:
        tries = play_game()
        all_tries.append(tries)

        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print(separator)
            print("Thank you for playing! Here are your results: ")
            print(f"Games played: {len(all_tries)}")
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()