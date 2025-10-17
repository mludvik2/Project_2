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
        print("You have not guessed the number!")
        print("-" * 40)
    print(tries)



#elif choice == rand_num:
    #print(f"Correct, you've guessed the right number in {sum(incorrect_num)} guesses!")
#else:
    #print("Try again.")
    #incorrect_num += choice
    #print(incorrect_num)

#else:

    #print("Try again.")
    #loop through

#def generate_number(length, ):



