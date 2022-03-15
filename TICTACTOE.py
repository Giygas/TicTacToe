# Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.

# Here are the requirements:

# * 2 players should be able to play the game (both sitting at the same computer)
# * The board should be printed out every time a player makes a move
# * You should be able to accept input of the player position and then place a symbol on the board

# TODO  reprint the board everytime someone makes a move
#       make the board an array so it will be easier to reprint
#       O and X

import os
import time

def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

#defining disponible options
ol = ["1","2","3","4","5","6","7","8","9"]

#choices of every player
p1choices = list()
p2choices = list()

clrscr()

def printwelcome():
    print("*"*80)
    print("{0:<10}{1:^60}{2:>10}".format("*","Welcome to TIC TAC TOE", "*"))
    print("*"*80)
    print("{0:<10}{1:^60}{2:>10}".format("*","For two players, first one to make a line wins!","*"))
    print("{0:<10}{1:^60}{2:>10}".format("*","You will be prompted wich square you want to play","*"))
    print("{0:<10}{1:^60}{2:>10}".format("*","And then it's the next player turn","*"))
    print("{0:<10}{1:^60}{2:>10}".format("*","Good Luck !","*"))
    print("*"*80)

def printmatrix(): #Display matrix creation
    mt =[
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|", "-", "-", "-", "-", "-" "-", "-", "-", "-", "-",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|", "-", "-", "-", "-", "-" "-", "-", "-", "-", "-",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " " " ", " ", " ", " ", " ",],
        ]
    #output formatting in string
    output = ""
    for i,row in enumerate(mt):
        for character in row:
            output += character
        print("{0:^50}".format(output))
        output =""

def printoptions():
    od = [1,2,3,4,5,6,7,8,9]
    print(" {} | {} | {} ".format(od[0],od[1],od[2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(od[3],od[4],od[5]))
    print("---|---|---")
    print(" {} | {} | {} ".format(od[6],od[7],od[8]))
    print("")


###
###Program Start
###

choicenumber = 0 # tracks the amount of choices made 

#Welcome 
printwelcome()

#Default selection to enter in the loop
pinput = ""
while pinput.isdigit() == False:
    printoptions()
    pinput = input("Choose a number: ")
    if pinput.isdigit() == False: 
        print("Must be a number. Please try again")
    if pinput not in ol:
        print("Sorry, but that choice it's not possible. Please try again.")
        time.sleep(2)
        clrscr()
    else:
        ol[int(pinput)+1] = " "
        continue