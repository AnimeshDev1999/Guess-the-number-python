## Import

import random

## Initalization

userChoice = "y"
rangeChoice = ""
rangeFrom = 0
rangeTo = 0
comChoice = 0
userGuess = 0
chances = 5

## Logic

while(userChoice == "y" or userChoice == "Y"):
    
## Messege for the user
    
    print("======== GUESS THE NUMBER ========")
    print("======== Made by Animesh Kumar on python3 ========")
    print()
    print("=== Range selection ===")
    print()

## Choosing the random number

    rangeChoice = input("Would you like to input the range yourself? (y/n): ")
    if(rangeChoice == "y" or rangeChoice == "Y"):
        print("Input your Custom range")
        rangeFrom = int(input("From: "))
        rangeTo = int(input("To: "))
        comChoice = random.randint(rangeFrom, rangeTo)
        if(rangeTo > 15):
            chances = 10
        print()
        print("[ Guess the number between", rangeFrom, "and", rangeTo, "]")
    elif(rangeChoice == "show"):
        print("Input your Custom range")
        rangeFrom = int(input("From: "))
        rangeTo = int(input("To: "))
        comChoice = random.randint(rangeFrom, rangeTo)
        if(rangeTo > 15):
            chances = 10
        print()
        print("The number is: ", comChoice)
        print("[ Guess the number between", rangeFrom, "and", rangeTo, "]")
    else:
        comChoice = random.randint(0,10)
        print()
        print("[ Guess the number between 0 and 10 ]")

## Guessing the number
    
    print()
    for x in range (chances):
        print("Guesses left: ", chances)
        userGuess = int(input("Your guess: "))
        if(userGuess == comChoice):
            print()
            print("=== Correct! ===")
            print("=== You won! ===")
            break
        else:
            chances = chances-1
            print()
            print("Incorrect! try again")
    if(chances == 0):
        print()
        print("=== Game over ===")
        print("=== You lost ===")

## Play again

    print()
    userChoice = input("Would you like to play again? (y/n): ")
    chances = 5
    print()
