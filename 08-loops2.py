import random

print("Welcome to the guessing game!")
print("the rules are simple, I'll think of a number and you try to guess it.")

isGuessRight = False

secretNumber = random.randint(0, 20)

while not isGuessRight:
    guess = int(input("enter a number "))
    if (guess == secretNumber):
        print("nice!")
        isGuessRight = True
    elif guess > secretNumber:
        print("the value is lower.")
    elif guess < secretNumber:
        print("the value is bigger")
