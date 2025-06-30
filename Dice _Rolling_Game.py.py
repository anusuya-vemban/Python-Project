'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import random 

while True:
    choice = input("Do you roll the dice? (Y/N): ").lower()
    if choice == 'y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f'{dice1}, {dice2}')
    elif choice == 'n':
        print("Thanks for playing")
        break
    else:
        print("Invalid input")