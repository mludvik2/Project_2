"""project_2.py: 
second project for Engeto Online Python Academy

Author: Michaela Papadimitriu Ludvikova
email: mludvik2@yahoo.com
"""
import random

print("Hi there!")
print("-" * 40)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-" * 40)

rand_num = random.randint(1000, 9999)
print(rand_num)


print("-" * 40)

tries = 0
while True:
    choice = input("Enter a number: ")
    print("-" * 40)
    
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please add numbers only.")
        print("-" * 40)
        continue
    tries += 1

    if choice == rand_num:
        print(f"Correct, you've guessed the right number in {tries} guesses!")
        print("-" * 40)
        print("That's amazing!")
        break
    elif choice < 1000 or choice > 9999:
        print("You have not chosen a 4 digit number.")
        print("-" * 40)
    else:
        cows = 0
        bulls = 0
        for number in range(4):
            if choice == rand_num:
                bull += 1
            elif choice in rand_num:
                cow += 1
        print(f"{bulls} bulls, {cows} cows")
        print("-" * 40)
    print(tries)

    

        

#Bulls = correct code, correct position. Cows = correct code, wrong position.

#def generate_number(length, ):
#Bulls = correct digit and correct position

#Cows = correct digit but wrong position

#Game ends when you guess the number exactly → all Bulls


