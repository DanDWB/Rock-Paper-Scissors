import random # had to import this to get the random choice selector
# PLANNING

# To start this project I need to have a game idea/function planned: rock, paper, scissors

# From here, I'm going to makesure I have the programming language that I will be using installed
# on my system, then find a reliable source for the syntax, such as variables, strings, loops, etc
# here I used w3schools.com 

# With these in mind, I can start the project

# PSEUDUCODE

# Here I come I write the basic logic in psedo code in order to break the project down step by step,
# but to also ensure it's in a readable format, so If I need to debug the logic far easier 
# than If i tried to debug once I wrote everything in Python


# 1) Take a users input, and store this as x, values can only be rock, paper, or scissors

# 2) computer chooses random string between three options (Scissors, Rock, Paper) and stores as y

# 3) Now here's the fun bit I need to build

# If x = rock and y = scissors
# or if x = paper and y = rock
# or if x = scissors and y = paper

# then print you win! Computer chose y

# else if x == y then print, you draw, computer also chose y

# else print, you lose, computer chose y

# Give user option to replay 

# THE PROGRAM 

x = input("Which one do you choose? Rock, Paper, or Scissors? ") # for this, I literally didn't search anything, I knew I wanted
# user input, so I went down to the python user input section on w3 schools, but now, I want 
# AFTER THIS I WANT THE USER TO ONLY BE ABLE TO CHOOSE ONE OF THE THREE, i DON'T WANT PROGRAM STORING EVERYTHING
# I just scrolled passed the check string function in python, maybe i will return and try that for line 40 comment


# I struggled to find this just by scrolling through w3 school, so typed this into google:
# "how to get the computer to choose a random string in python", coincidence the first choice
# was a w3 schools article showing the python random choice method

complist = ["Rock", "Paper", "Scissors"] 

y = random.choice(complist)

# before continuing, I tested the output to makesure this worked, breaking up the program further
# It's way easier to debug in steps.

if x == "Rock" and y == "Scissors": 
    print ("You Win! Computer chose " + y)
if x == "Paper" and y == "Rock": 
    print ("You Win! Computer chose " + y)
    if x == "Scissors" and y == "Paper": 
        print ("You Win! Computer chose " + y)
    elif x == y: 
        print ("You both Draw! Computer chose " + y)
    else: 
        print ("You Lose! Computer chose " + y)       # this is my first attempt, I will keep this 
# here for visibility even if this is completely wrong. to get to this point
# I scrolled to the if else portion of w3 schools and noticed 

# i realized the first time all of this wasn't working as I was missing the ":" that should go after the if and other statements. 