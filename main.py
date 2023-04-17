

hiddenBoard = [[" "] * 8 for x in range(8)]
guessBoard = [[" "] * 8 for x in range(8)]


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
    pass


def countHitShips():
    pass

def printBoard(board):
    print("    A B C D E F G H")
    print("    ---------------")
    rowNumber = 1
    for row in board:
        print("%d|%s" % (rowNumber, "|".join(row)))
        rowNumber += 1



