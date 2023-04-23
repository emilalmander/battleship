

cur.execute("""create table if not exists""")


def resetBoard():
    global hiddenBoard, guessBoard
    hiddenBoard = [[" "] * 8 for x in range(8)]
    guessBoard = [[" "] * 8 for x in range(8)]

from random import randint

lettersToNumbers = {
"A": 0,
"B": 1,
"C": 2,
"D": 3,
"E": 4,
"F": 5,
"G": 6,
"H": 7
}

def createShipsEasy(board):
    for ship in range(3):
        shipRow, shipColumn = randint(0,7), randint(0,7)
        while board[shipRow][shipColumn] == "X":
            shipRow, shipColumn = randint(0,7), randint(0,7)
        board[shipRow][shipColumn] = "X"
def createShipsMedium(board):
    for ship in range(5):
        shipRow, shipColumn = randint(0,7), randint(0,7)
        while board[shipRow][shipColumn] == "X":
            shipRow, shipColumn = randint(0,7), randint(0,7)
        board[shipRow][shipColumn] = "X"
def createShipsHard(board):
    for ship in range(7):
        shipRow, shipColumn = randint(0,7), randint(0,7)
        while board[shipRow][shipColumn] == "X":
            shipRow, shipColumn = randint(0,7), randint(0,7)
        board[shipRow][shipColumn] = "X"

def createShips(board, mode):
    if mode == "easy":
        createShipsEasy(board)
    elif mode == "medium":
        createShipsMedium(board)
    elif mode == "hard":
        createShipsHard(board)



def getShipLocation():
    row = input("please enter a ship row 1-8: ")
    while row not in "12345678":
        print("please enter a valid row")
        row = input("please enter a ship row 1-8: ")
    column = input("please input a ship column A-H: ").upper()
    while column not in "ABCDEFGH" : 
        print("please enter a valid column")
        column = input("please input a ship column A-H: ").upper()
    return int(row) -1, lettersToNumbers[column]



def chooseGameMode():
    while True:
        mode = input("hello, " + username + " Choose a game mode (easy, medium, hard): ").lower()
        if mode in ["easy", "medium", "hard"]:
            return mode
        else:
            print("Invalid game mode. Please try again.")
            





def countHitShips(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count




def printBoard(board):
    print("  A B C D E F G H")
    print("  ---------------")
    rowNumber = 1
    for row in board:
        print("%d|%s" % (rowNumber, "|".join(row)))
        rowNumber += 1


def printRules():
    print("Rules:")
    print("The objective of the game is to sink all of the hidden ships on the board.")
    print("You have a limited number of turns to make guesses.")
    print("Each turn, you will guess a row and column to attack.")
    print("If your guess hits a ship, the ship will be marked with an X on the board.")
    print("If your guess misses, the location will")
    
    okay = input("when fully understood, write okay: ")
    homescreen()
    


wins = 0
loses = 0

def win():
    global wins
    wins += 1

def lose():
    global loses
    loses += 1

def scoreboard():
    print("Your score is " + str(loses) + " losses and " + str(wins) + " wins.")
    homescreen()

def chooseUsername():
    username = input("Please enter a username: ")
    return username
    homescreen()

def homescreen():
    print ("a, chose another username")
    print ("b, chose another gamemode")
    print(" c, rules ")
    print(" d, new game")
    print(" e, scoreboard")
    print(" f, exit")
    choice = input("chose an option: ")
    if choice == "a" or choice == "A":
        return chooseUsername()
    elif choice == "b" or choice == "B":
        return chooseGameMode()
    elif choice == "c" or choice == "C":
        return printRules()
    elif choice == "d" or choice == "D":
        return runGame()
    elif choice == "e" or choice == "E":
        return scoreboard()

def runGame():
    resetBoard()
    createShips(hiddenBoard, gameMode)


    turns = 2
    while turns > 0:
        printBoard(guessBoard)
        row, column = getShipLocation()
        if guessBoard[row][column] == "-":
            print("you have already guessed that.")
            print(" ")
        elif hiddenBoard[row][column] == "X":
            print("congratz, you have sunk a battleship")
            print(" ")
            guessBoard[row][column] = "X"
            turns -= 1
        else:
            print("you missed the battleships")
            guessBoard[row][column] = "-"
            turns -= 1
        if countHitShips(guessBoard) == 5:
            print("all ships have been sunk!")
            homescreen()
        print("you have " + str(turns) + " turns remaining")
        if turns == 0:
            print("you ran out of turns, you lost!")
            lose()
            homescreen()
            
    







username = chooseUsername()
gameMode = chooseGameMode()
printRules()
homescreen()













