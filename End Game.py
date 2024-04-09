import random

replay = "y"                                             
while replay.casefold() == "y":                                               # Loop start
    x = input(" Which one do you choose? Rock, Paper, or Scissors? ")         # User input
    complist = ["Rock", "Paper", "Scissors"]                                  # List for computer to choose from
    y = random.choice(complist)                                               # Computers choice

    if x.casefold() == "rock" and y == "Scissors":                            # Logic
        print ("You Win! Computer chose " + y)
    elif x.casefold() == "paper" and y == "Rock":
        print ("You Win! Computer chose " + y)
    elif x.casefold() == "scissors" and y == "Paper":
        print ("You Win! Computer chose " + y)
    elif x.casefold() == y.casefold():
        print ("You both Draw! Computer chose " + y)
    else: 
        print ("You Lose! Computer chose " + y) 

    replay = input("play again? Y/N ")                                        # Loop end