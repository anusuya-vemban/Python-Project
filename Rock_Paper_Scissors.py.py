'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import random
 
emojis = {'r': '🗿', 'p': '📜', 's': '✂️'}
choices = ('r','p','s')

while True:
    user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid input")

    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie")
    elif(
        (user_choice == "r" and computer_choice == "s") or 
        (user_choice == "p" and computer_choice == "r") or 
        (user_choice == "s" and computer_choice == "p")):
         print("You win and Computer lose")
    else:
        print("Computer win and You lose")
    should_continue = input("Yes or No? (y/n): ").lower()
    if should_continue == "y":
        continue
    else:
        print("Thanks for playing")
        break