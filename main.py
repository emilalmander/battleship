

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

def createShips(board):
    for ship in range(5):
        shipRow, shipColumn = randint(0,7), randint(0,7)
        while board[shipRow][shipColumn] == "X":
            shipRow, shipColumn = randint(0,7), randint(0,7)
        board[shipRow][shipColumn] = "X"


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


createShips(hiddenBoard)
print("welcome to battleship, this is a singleplayer game! there are 3 different modes. easy, medium and hard. they have different amout of ships 3,5 and 7. ")
turns = 10
while turns > 0:
    
    printBoard(guessBoard)
    row, column = getShipLocation()
    if guessBoard[row][column] == "-":
        print("you have already guessed that.")
    elif hiddenBoard[row][column] == "X":
        print("congratz, you have sunk a battleship")
        guessBoard[row][column] = "X"
        turns -= 1
    else:
        print("you missed the battleships")
        guessBoard[row][column] = "-"
        turns -= 1
    if countHitShips(guessBoard) == 5:
        print("all ships have been sunk!")
        break
    print("you have " + str(turns) + "turns remaining")
    if turns == 0:
        print("you ran out of turns, you lost!")
        break






