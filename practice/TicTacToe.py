
board = [' ' for x in range(10)]

def insertletter(letter,pos):
    board[pos] = letter

def freespace(pos):
    return board[pos] == ' '

def printBoard(board):
    print("       |       |       ")
    print("   " + board[1] + "   |   " + board[2] + "   |   " + board[3])
    print("_______|_______|_______")
    print("       |       |       ")
    print("   " + board[4] + "   |   " + board[5] + "   |   " + board[6])
    print("_______|_______|_______")
    print("       |       |       ")
    print("   " + board[7] + "   |   " + board[8] + "   |   " + board[9])
    print("       |       |       ")

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def isWinner(b,l):
    return (b[1] == l and b[2] == l and b[3] == l) \
        or (b[4] == l and b[5] == l and b[6] == l) \
        or (b[7] == l and b[8] == l and b[9] == l) \
        or (b[1] == l and b[4] == l and b[7] == l) \
        or (b[2] == l and b[5] == l and b[8] == l) \
        or (b[3] == l and b[6] == l and b[9] == l) \
        or (b[1] == l and b[5] == l and b[9] == l) \
        or (b[3] == l and b[5] == l and b[7] == l) \

def playerMove():
    run = True
    while run:
        move = input("Please select a position to enter the X between 1 to 9:")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if freespace(move):
                    run = False
                    insertletter("X", move)
                else:
                    print("Sorry, This space is occupied")
            else:
                print("Please type a number between 1 to 9")

        except:
            print("please type a number")

def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

        if len(edgesOpen) > 0:
            move = selectRandom(edgesOpen)
            return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to the game!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry you loose")
            break

        if not(isWinner(board , "X")):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertletter('O' , move)
                print("Computer placed an O on position", move , ':')
                printBoard(board)
        else:
            print("You Win")
            break

    if isBoardFull(board):
        print("Tie game")

while True:
    start = input("Do you want to play again? (Y/N) :")
    if start.lower() == "y":
        board = [' ' for x in range(10)]
        print("-----------------")
        main()
    else:
        break