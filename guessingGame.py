import random
print("Number Guessing Game")
number = random.randint(2,48)
chances = 0
while chances < 5:
    guess = int(input("What number am I thinking of?"))

    if guess == number :
        print("You guessed it!")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
    chances += 1
if not chances <8:
    print("Incorrect! Sorry you've run out of guesses. The number was ", number)