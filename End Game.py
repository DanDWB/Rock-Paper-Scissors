import random

replay = "y"
while replay.casefold() == "y":
    x = input("Which one do you choose? Rock, Paper, or Scissors? ") # for this, I literally didn't search anything, I knew I wanted
 
    complist = ["Rock", "Paper", "Scissors"] 
    y = random.choice(complist)

    if x.casefold() == "rock" and y == "Scissors": 
        print ("You Win! Computer chose " + y)
    elif x.casefold() == "paper" and y == "Rock": # same issue as line 60 now, it's not letting me win
        print ("You Win! Computer chose " + y)
    elif x.casefold() == "scissors" and y == "Paper": # for some reason the game was working until I selected scissors and y = paper, it said I lost, so this line needs work (SOLVED: instead of if, i did another elif, and indented it as shown, python is indentation sensitive)
        print ("You Win! Computer chose " + y)
    elif x.casefold() == y.casefold(): # Here I fixed the issues with capital letters by typing on google: "how to remove capital sensitive in python strings", leading me to the .casefold() function on stack overflow
        print ("You both Draw! Computer chose " + y)
    else: 
        print ("You Lose! Computer chose " + y) 

    replay = input("play again? Y/N ")