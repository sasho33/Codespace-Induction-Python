import random
from turtle import goto

def Game(inputValue):
    #computer choise
    randC=random.randint(0,2)
    combinations=["Rock", "Paper", "Scissors"]
    compChoice = combinations[randC]
    
    playerChoice = None
# player choice
    if inputValue == "r":
        playerChoice=combinations[0]
    elif inputValue =="p":
        playerChoice=combinations[1]
    elif inputValue =="s":
        playerChoice=combinations[2]
    else:   
        print("Invalid input")
        moreGame=(input("One more game to play (Y or N)"))
        if moreGame == "y" or "Y":
            Game(input("Enter a choice (Rock(r), Paper(p), Scissors(s))"))
        else:
            exit()

# game logic
    if playerChoice == compChoice:
        print("Draw!")
    else:
        if playerChoice=="Rock" and compChoice=="Paper" or playerChoice=="Paper" and compChoice=="Scissors":
            print(f"You lost! Player choose {playerChoice}  and computer choose {compChoice}")
        else: 
            print(f"You Won! Player choose {playerChoice}  and computer choose {compChoice}")

    moreGame=(input("One more game to play (Y or N)"))
    if moreGame == "y" or "Y":
        Game(input("Enter a choice (Rock(r), Paper(p), Scissors(s))"))
    else:
        exit()

    
Game(input("Enter a choice (Rock(r), Paper(p), Scissors(s))"))
