import random

yourScore = 0
opponentScore = 0

while True:
    selection = ["rock", "paper", "scissors"]

    opponent = random.choice(selection)
    player = None

    while player not in selection:
        player = input("rock, paper, scissors?: ").lower().strip()

    if player == opponent:
        print("Both players selected", player, ". It's a tie!")

    elif player == "rock":
        if opponent == "paper":
            print("You chose", player, ", computer chose", opponent)
            print("Paper covers rock! You lose.")
            opponentScore += 1

        elif opponent == "scissors":
            print("You chose", player, ", computer chose", opponent)
            print("Rock smashes scissors! You win.")
            yourScore += 1

    elif player == "paper":
        if opponent == "rock":
            print("You chose", player, ", computer chose", opponent)
            print("Paper covers rock! You win.")
            yourScore += 1
        elif opponent == "scissors":
            print("You chose", player, ", computer chose", opponent)
            print("Scissors cut paper! You lose.")
            opponentScore += 1
        
    elif player == "scissors":
        if opponent == "rock":
            print("You chose", player, ", computer chose", opponent)
            print("Rock smashes scissors! You lose.")
            opponentScore += 1

        elif opponent == "paper":
            print("You chose", player, ", computer chose", opponent)
            print("Scissors cut paper! You win.")
            yourScore += 1

    newGame = input("Play again? (y/n): ").lower()
    
    if newGame == "n":
        break

print("Final Scores:")
print("Computer:", opponentScore)
print("Player", yourScore)
