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

#list containing all possible winning possibilities
winninglist = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (7,5,3)]

#choices of every player
p1choices = list()
p2choices = list()

#winner found
winner = False

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
    print("\n"*1)

def printend():
    print("\n")
    print("*"*80)
    print("{0:<10}{1:^60}{2:>10}".format("**","THE GAME HAS ENDED", "**"))
    if winner == False:
        print("{0:<10}{1:^60}{2:>10}".format("**","Unfortunately, noone has won","**"))
    else:
        print(("{0:<10}{1:^60}{2:>10}".format("**","THE WINNER IS: "+winner,"**")))
    print("*"*80)
    print("\n"*3)


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
    print(" {} | {} | {} ".format(ol[0],ol[1],ol[2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(ol[3],ol[4],ol[5]))
    print("---|---|---")
    print(" {} | {} | {} ".format(ol[6],ol[7],ol[8]))
    print("")

#Checks if there's a winner. Takes as input the choices and number of the player. 
#Sets the global variable winner to the number of the winning player
def checkwinner(choices,pnumber):
    global winner

    for element in winninglist:
        result = all(elem in choices for elem in element)
        if result:
            winner = "Player "+ str(pnumber)


###
###Program Start
###

choicenumber = 0 # tracks the amount of choices made 

#Welcome 
printwelcome()

#Default selection to enter in the loop
pinput = ""

while choicenumber < 9 and winner == False:
    printoptions()

    #Printing player number
    if choicenumber%2==0:
        print("Player 1")
    else: 
        print("Player 2")

    #take user input
    pinput = input("Choose a number: ")

    #First control if it's a number
    if pinput.isdigit() == True: 
        #Check if the number is in the list of available numbers
        if pinput not in ol:
            print("Sorry, but that choice it's not possible. Please try again.")
            time.sleep(2)
            clrscr()
        else:
            #remove from the options disponible list the number chosen
            x = int(pinput) - 1
            ol[x] = " "
            #increase the number of choices made
            if choicenumber%2==0:
                p1choices.append(int(pinput))
                checkwinner(p1choices, 1)
            else:
                p2choices.append(int(pinput))
                checkwinner(p2choices, 2)
            choicenumber +=1
    else:
        print("Must be a number. Please try again")
        time.sleep(2)
        clrscr()

printend()
time.sleep(5)