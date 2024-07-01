import random                         #You set up the random choice key

options = ("rock","paper","scissors") #List out your options
player = None                         #Player is user & they don't have nothing atm
computer = random.choice(options)     #Set up the computer into picking random choices

player = input("Enter a choice (rock, paper, scissors): ")  #This is where the player will be able to choose

print(f"Player: {player}")           #This will be displayed & the user will be making their decision

print(f"Computer: {computer}")       #This will be displayed & the computer is making their decesion

