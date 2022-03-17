# Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.

# Here are the requirements:

# * 2 players should be able to play the game (both sitting at the same computer)
# * The board should be printed out every time a player makes a move
# * You should be able to accept input of the player position and then place a symbol on the board

# TODO  Print the selection matrix
#       Draw the symbols in the matrix

import os
import time

def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

#Display matrix
mt =[
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "|", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",],
        ]

#defining disponible options
ol = [1,2,3,4,5,6,7,8,9]

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

def printend():
    print("\n")
    print("*"*80)
    print("{0:<10}{1:^60}{2:>10}".format("**","THE GAME HAS ENDED", "**"))
    if winner == False:
        print("{0:<10}{1:^60}{2:>10}".format("**","Unfortunately, noone has won","**"))
    else:
        print(("{0:<10}{1:^60}{2:>10}".format("**","THE WINNER IS: "+winner,"**")))
        print(("{0:<10}{1:^60}{2:>10}".format("**","Congratulations!","**")))
    print("*"*80)


def printmatrix(): #Display matrix creation
    #output formatting in string
    output = ""
    for i,row in enumerate(mt):
        for character in row:
            output += character
        print("{0:^80}".format(output))
        output =""

def printoptions():
    print(" {:>70} | {} | {} ".format(ol[0],ol[1],ol[2]))
    # print("---|---|---")
    print(" {:>70} | {} | {} ".format(ol[3],ol[4],ol[5]))
    # print("---|---|---")
    print(" {:>70} | {} | {} ".format(ol[6],ol[7],ol[8]))
    print("")

#Checks if there's a winner. Takes as input the choices and number of the player. 
#Sets the global variable winner to the number of the winning player
def checkwinner(choices,pnumber):
    global winner

    for element in winninglist:
        result = all(elem in choices for elem in element)
        if result:
            winner = "Player "+ str(pnumber)


#Base x and y for all the possible options
drawerpointer=((0,0), (0,11), (0,22),
        (6,0), (6,11), (6,22),
        (12,0), (12,11), (12,22))

#Takes the user input and player number to modify the game matrix with the O or X
def optionselect(pinput, player):
    global mt
    csquare = (2,3,6,7)
    middle = (4,5)
    sides = (0,1,8,9)
    i = drawerpointer[pinput-1]
    x = i[1]
    y = i[0]

    for num in csquare:
        mt[y+1][x+num] = mt[y+3][x+num] = "x"
    if player == 1:
        for num in middle:
            mt[y][x+num] = mt[y+4][x+num] = "x"
            for num in sides: 
                mt[y+2][x+num] = "x"
    else:
        for num in middle:
            mt[y+2][x+num] ="x"
        for num in sides:
            mt[y][x+num] = mt[y+4][x+num] = "x"
    




###
###Program Start
###

choicenumber = 0 # tracks the amount of choices made 

#Welcome 
printwelcome()

#Default selection to enter in the loop
pinput = ""

while choicenumber < 9 and winner == False:
    #Printing player number
    if choicenumber%2==0:
        print("Player 1")
    else: 
        print("Player 2")
    printoptions()
    #take user input
    pinput = input("Choose a number: ")
    #First control if it's a number
    if pinput.isdigit() == True:
        pinput = int(pinput) 
        #Check if the number is in the list of available numbers
        if pinput not in ol:
            print("Sorry, but that choice it's not possible. Please try again.")
            pinput = ""
            time.sleep(2)
            clrscr()
        else:
            #remove from the options disponibles list the number chosen
            x = pinput - 1
            ol[x] = " "
            if choicenumber%2==0:
                p1choices.append(pinput)
                checkwinner(p1choices, 1)
                optionselect(pinput, 1)
            else:
                p2choices.append(pinput)
                checkwinner(p2choices, 2)
                optionselect(pinput, 2)
            #increase the number of choices made
            choicenumber +=1
            clrscr()
    else:
        print("Must be a number. Please try again")
        time.sleep(2)
        clrscr()
    printmatrix()

printend()
time.sleep(5)