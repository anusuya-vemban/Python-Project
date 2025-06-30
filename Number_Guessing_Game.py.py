'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import random
guess = random.randint(1,100)

while True:
    try:
        number = int(input("Guess the number: "))
        if number < guess:
            print("Too low")
        elif number > guess:
            print("Too high")
        else:
            print("Well done! You guessed the correct number.")
            break
    except ValueError:
        print("Enter a valid number.")