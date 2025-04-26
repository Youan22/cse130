# 1. Name: 
#    -Dioulo Rubinel Youan Bi-
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    This program lets a user guess a randomly generated number, tracks their guesses,
#    and lets them play again if they want.
# 4. What was the hardest part? Be as specific as possible.
#    Making sure the loop restarts properly after the game ends, and tracking guesses correctly.
# 5. How long did it take for you to complete the assignment?
#    About 1 hour and half.

import random

# Game introduction
print('This is the "guess a number" game.')
print("You try to guess a random number in the smallest number of attempts.")

# New main game loop
play_again = "y"

while play_again == "y":
    # Prompt the user for difficulty
    value_max = int(input("\nPick a positive integer: "))

    # Generate a random number
    value_random = random.randint(1, value_max)

    # Instructions
    print(f"Guess a number between 1 and {value_max}.")

    # Initialize guesses list and sentinel
    guesses = []
    found = False

    # Play the guessing game
    while not found:
        guess = int(input("Enter a number: "))
        guesses.append(guess)

        if guess < value_random:
            print("Too low.")
        elif guess > value_random:
            print("Too high.")
        else:
            found = True
            print("Yay, you got it!")

    # End of the game summary
    print(f"\nYou found the number in {len(guesses)} guesses.")
    print("Your guesses were:", guesses)

    # Ask if they want to play again
    play_again = input("\nDo you want to play again? (y/n): ").lower()

print("\nThanks for playing! Goodbye!")
