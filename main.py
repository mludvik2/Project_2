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
        num = random.sample('013456789',4)
        if num [0] != '0':
            number = ''.join(num)
            return number
        
def if_valid_guess(guess):
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
    Cows: correct digit but wrong position
    """
    cows = 0
    bulls = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
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
    
    secret = generate_secret_num
    print(secret)   ### remove afterwards

    tries = 0

    while True:
        guess = input("Enter a number: ").strip()
        """To remove any spaces from the 
        Player's input
        """
        if not if_valid_guess(guess):
            print("-" * 40)
            continue
        
        tries += 1

        if guess == secret:
            print(f"Correct, you've guessed the right number in {tries} guesses!")
            print("-" * 40)
            print("That's amazing!")
            break
        
        bulls, cows = count_bulls_and_cows(secret, guess)
        print(f"{bulls} bulls, {cows} cows")
        print(f"Number of guesses: {tries}")
        print("-" * 40)

play_game()













        
    cows = 0
    bulls = 0
    for i in range(4):
        if choice_str[i] == rand_num_str[i]:
            bulls += 1
        elif choice_str[i] in rand_num_str:
            cows += 1
    print(f"{bulls} bulls, {cows} cows")
    print(f"{tries}Guesses used.")## not working
    print("-" * 40)

    

        

#Bulls = correct code, correct position. Cows = correct code, wrong position.

#def generate_number(length, ):
#Bulls = correct digit and correct position

#Cows = correct digit but wrong position

#Game ends when you guess the number exactly → all Bulls

#sentence with tries not working


