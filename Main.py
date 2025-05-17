import random

completedTurn = []
completedTurnByNumber = []
completedPointNumber = []
letterSet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def singleNumberIt(board, size, mineBoard, move):
    if size == 8:
        hasUp = move[1] != 1
        hasDown = move[1] != 8
        hasLeft = move[0] != "a"
        hasRight = move[0] != "h"

        coordOne = letterSet.index(move[0])
        coordTwo = move[1] - 1

        count = 0

        if hasUp and mineBoard[coordTwo-1][coordOne] == "x":
            count += 1
        if hasDown and mineBoard[coordTwo+1][coordOne] == "x":
            count += 1
        if hasLeft and mineBoard[coordTwo][coordOne-1] == "x":
            count += 1
        if hasRight and mineBoard[coordTwo][coordOne+1] == "x":
            count += 1
        if hasUp and hasLeft and mineBoard[coordTwo-1][coordOne-1] == "x":
            count += 1
        if hasUp and hasRight and mineBoard[coordTwo-1][coordOne+1] == "x":
            count += 1
        if hasDown and hasRight and mineBoard[coordTwo+1][coordOne+1] == "x":
            count += 1
        if hasDown and hasLeft and mineBoard[coordTwo+1][coordOne-1] == "x":
            count += 1

        board[coordTwo][coordOne] = str(count)

def groupNumberIt(board, size, mineBoard):
    
    if size == 8:
        for pair in completedTurn:
            hasUp = pair[1] != 1
            hasDown = pair[1] != 8
            hasLeft = pair[0] != "a"
            hasRight = pair[0] != "h"

            coordOne = letterSet.index(pair[0])
            coordTwo = pair[1] - 1

            count = 0

            if hasUp and mineBoard[coordTwo-1][coordOne] == "x":
                count += 1
            if hasDown and mineBoard[coordTwo+1][coordOne] == "x":
                count += 1
            if hasLeft and mineBoard[coordTwo][coordOne-1] == "x":
                count += 1
            if hasRight and mineBoard[coordTwo][coordOne+1] == "x":
                count += 1
            if hasUp and hasLeft and mineBoard[coordTwo-1][coordOne-1] == "x":
                count += 1
            if hasUp and hasRight and mineBoard[coordTwo-1][coordOne+1] == "x":
                count += 1
            if hasDown and hasRight and mineBoard[coordTwo+1][coordOne+1] == "x":
                count += 1
            if hasDown and hasLeft and mineBoard[coordTwo+1][coordOne-1] == "x":
                count += 1

            board[coordTwo][coordOne] = str(count)

def whichToMakeGoBoom(board, size, mineBoard, move):
    coordOne = letterSet.index(move[0])
    coordTwo = move[1] - 1
    
    if mineBoard[coordTwo][coordOne] == "x":
        return "KABOOM"
    
    completedTurn.append([move[0], move[1]])
    convertLetterNumToNumNum(board)
    fillIn(board, size, move)
    singleNumberIt(board, size, mineBoard, move)
    groupNumberIt(board, size, mineBoard)

def convertTurnToNum(board):
    global completedPointNumber
    bigList = []
    for move in completedTurnByNumber:
        value = move[1] - 1
        blank = value * len(board[0])
        blank += move[0]
        blank += 1
        bigList.append(blank)
    completedPointNumber = bigList

def convertLetterNumToNumNum(board):
    global completedTurnByNumber
    bigList = []
    for move in completedTurn:
        blankSlate = [0, 0]
        blankSlate[1] = move[1]
        count = 0
        for letter in letterSet:
            if letter == move[0]:
                break
            count += 1
        blankSlate[0] = count
        bigList.append(blankSlate)
    completedTurnByNumber = bigList
    convertTurnToNum(board)

def fillIn(board, size, move):
    coordOne = letterSet.index(move[0])
    coordTwo = move[1] - 1
    convertLetterNumToNumNum(board)

def checkAround(board, size, move, kaboomCount):
    bCount = kaboomCount - 10
    up = move[1] != 1
    down = move[1] != 8
    left = move[0] != "a"
    right = move[0] != "h"

    if size == 8:
        if left and bCount > 0:
            chooseLeft = random.randint(1, 10)
            if chooseLeft != 10:
                count = letterSet.index(move[0]) - 1
                nextMove = [letterSet[count], move[1]]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if right and bCount > 0:
            chooseRight = random.randint(1, 10)
            if chooseRight != 10:
                count = letterSet.index(move[0]) + 1
                nextMove = [letterSet[count], move[1]]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if up and bCount > 0:
            chooseUp = random.randint(1, 10)
            if chooseUp != 10:
                nextMove = [move[0], move[1]-1]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if down and bCount > 0:
            chooseDown = random.randint(1, 10)
            if chooseDown != 10:
                nextMove = [move[0], move[1]+1]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if up and left and bCount > 0:
            chooseUpLeft = random.randint(1, 6)
            if chooseUpLeft != 6:
                count = letterSet.index(move[0]) - 1
                nextMove = [letterSet[count], move[1] - 1]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if up and right and bCount > 0:
            chooseUpRight = random.randint(1, 6)
            if chooseUpRight != 6:
                count = letterSet.index(move[0]) + 1
                nextMove = [letterSet[count], move[1] - 1]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if down and left and bCount > 0:
            chooseDownLeft = random.randint(1, 6)
            if chooseDownLeft != 6:
                count = letterSet.index(move[0]) - 1
                nextMove = [letterSet[count], move[1] + 1]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if down and right and bCount > 0:
            chooseDownRight = random.randint(1, 6)
            if chooseDownRight != 6:
                count = letterSet.index(move[0]) + 1
                nextMove = [letterSet[count], move[1] + 1]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        doubleUp = up and move[1] >= 3
        doubleDown = down and move[1] <= 6
        count = letterSet.index(move[0])
        doubleLeft = left and count >= 2
        doubleRight = right and count <= 5

        if doubleUp and bCount > 0:
            chooseDoubleUp = random.randint(1, 5)
            if chooseDoubleUp != 5:
                nextMove = [move[0], move[1]-2]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if doubleDown and bCount > 0:
            chooseDoubleDown = random.randint(1, 5)
            if chooseDoubleDown != 5:
                nextMove = [move[0], move[1]+2]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if doubleLeft and bCount > 0:
            chooseDoubleLeft = random.randint(1, 5)
            if chooseDoubleLeft != 5:
                count = letterSet.index(move[0]) - 2
                nextMove = [letterSet[count], move[1]]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if doubleRight and bCount > 0:
            chooseDoubleRight = random.randint(1, 5)
            if chooseDoubleRight != 5:
                count = letterSet.index(move[0]) + 2
                nextMove = [letterSet[count], move[1]]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if doubleUp and left and bCount > 0:
            chooseDoubleUpOneLeft = random.randint(1, 4)
            if chooseDoubleUpOneLeft != 4:
                count = letterSet.index(move[0]) - 1
                nextMove = [letterSet[count], move[1]-2]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if doubleUp and right and bCount > 0:
            chooseDoubleUpOneRight = random.randint(1, 4)
            if chooseDoubleUpOneRight != 4:
                count = letterSet.index(move[0]) + 1
                nextMove = [letterSet[count], move[1]-2]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if doubleDown and left and bCount > 0:
            chooseDoubleDownOneLeft = random.randint(1, 4)
            if chooseDoubleDownOneLeft != 4:
                count = letterSet.index(move[0]) - 1
                nextMove = [letterSet[count], move[1]+2]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if doubleDown and right and bCount > 0:
            chooseDoubleDownOneRight = random.randint(1, 4)
            if chooseDoubleDownOneRight != 4:
                count = letterSet.index(move[0]) + 1
                nextMove = [letterSet[count], move[1]+2]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if up and doubleLeft and bCount > 0:
            chooseOneUpDoubleLeft = random.randint(1, 4)
            if chooseOneUpDoubleLeft != 4:
                count = letterSet.index(move[0]) - 2
                nextMove = [letterSet[count], move[1]-1]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if up and doubleRight and bCount > 0:
            chooseOneUpDoubleRight = random.randint(1, 4)
            if chooseOneUpDoubleRight != 4:
                count = letterSet.index(move[0]) + 2
                nextMove = [letterSet[count], move[1]-1]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if down and doubleLeft and bCount > 0:
            chooseOneDownDoubleLeft = random.randint(1, 4)
            if chooseOneDownDoubleLeft != 4:
                count = letterSet.index(move[0]) - 2
                nextMove = [letterSet[count], move[1]+1]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        if down and doubleRight and bCount > 0:
            chooseOneDownDoubleRight = random.randint(1, 4)
            if chooseOneDownDoubleRight != 4:
                count = letterSet.index(move[0]) + 2
                nextMove = [letterSet[count], move[1]+1]
                if nextMove not in completedTurn:
                    completedTurn.append(nextMove)
                    fillIn(board, size, nextMove)
                    bCount -= 1

        convertLetterNumToNumNum(board)

def isPast(letter, size, board):
    highestLetter = "h" if size == 8 else "p" if size == 16 else "x"
    count = letterSet.index(letter)
    size_limit = letterSet.index(highestLetter)
    return count > size_limit

def turnOne(board, size, mineCount, mineBoard):
    print()
    kaboomCount = random.randint(10, 35) if size == 8 else random.randint(30, 70) if size == 16 else random.randint(90, 170)

    while True:
        try:
            moveOne = input("Where would you like to select? (Letter first, then Number (example: d4)) ")
            moveOneSplit = list(moveOne)
            oneMoveStr = moveOneSplit[0].lower()
            oneMoveNum = int(''.join(moveOneSplit[1:]))
            break
        except:
            print("Try again u got this!!!\n")

    print("\n\n\n")
    
    if oneMoveNum > size:
        oneMoveNum = size
    if isPast(oneMoveStr, size, board):
        oneMoveStr = "h" if size == 8 else "p" if size == 16 else "x"
    
    newMoveOne = [oneMoveStr, oneMoveNum]
    completedTurn.append(newMoveOne)
    fillIn(board, size, newMoveOne)
    checkAround(board, size, newMoveOne, kaboomCount)
    convertLetterNumToNumNum(board)
    addMine(board, mineCount, size, mineBoard, newMoveOne)
    return mineCount

def printBoard(board, size, mineBoard=None):
    if size == 8:
        print("    a  b  c  d  e  f  g  h")
    elif size == 16:
        print("    a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p")
    else:
        print("    a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x")
    
    print()
    for line in range(len(board)):
        if line + 1 < 10:
            print(line + 1, end="   ")
        else:
            print(line + 1, end="  ")
        for val in range(len(board)):
            print(board[line][val], end="  ")
        if mineBoard:
            print(" | ", end="")
            for val in range(len(mineBoard)):
                print(mineBoard[line][val], end="  ")
        print()
    print("\n\n\n")
    convertLetterNumToNumNum(board)

def addMine(board, mineCount, size, mineBoard, move):
    mineLab = []
    while len(mineLab) != mineCount:
        randomMine = random.randint(0, size*size-1)
        if randomMine not in mineLab and (randomMine + 1 not in completedPointNumber):
            mineLab.append(randomMine)
    
    mineLab.sort()
    preCount = 0
    count = 0
    for repeat in range(size):
        for repeatTwo in range(size):
            if preCount < len(mineLab) and mineLab[preCount] == count:
                mineBoard[repeat][repeatTwo] = "x"
                preCount += 1
            else:
                mineBoard[repeat][repeatTwo] = " "
            count += 1
    
    groupNumberIt(board, size, mineBoard)

def main():
    count = 0
    try:
        count = int(input("Input the number 1: "))
    except:
        print("Why break code :(")
        return
    
    print()
    size = count * 8
    
    small = [["□" for _ in range(8)] for _ in range(8)]
    small2 = [[" " for _ in range(8)] for _ in range(8)]
    medium = [["□" for _ in range(16)] for _ in range(16)]
    medium2 = [[" " for _ in range(16)] for _ in range(16)]
    large = [["□" for _ in range(24)] for _ in range(24)]
    large2 = [[" " for _ in range(24)] for _ in range(24)]
    
    sMine = 8
    mMine = 16
    lMine = 24
    
    mineCount = -1
    if size == 8:
        mineBoard = small2
        board = small
        mineCount = sMine
    elif size == 16:
        mineBoard = medium2
        board = medium
        mineCount = mMine
    else:
        mineBoard = large2
        board = large
        mineCount = lMine
    
    printBoard(board, size)
    mCount = turnOne(board, size, mineCount, mineBoard)
    printBoard(board, size)
    convertLetterNumToNumNum(board)
    
    win = False
    total_squares = size * size
    openSquares = total_squares - mineCount - len(completedTurn)
    currentNum = 1
    
    while openSquares > 0:
        print("Turn ", currentNum, ": What is your move? (Letter first, Then number)", end=" ")
        cMove = input()
        print("\n\n\n")
    
        try:
            moveSplit = list(cMove)
            move1 = moveSplit[0].lower()
            move2 = int(''.join(moveSplit[1:]))
        except:
            print("Invalid input. Try again.\n")
            continue
        
        if move2 > size:
            move2 = size
        if isPast(move1, size, board):
            move1 = "h" if size == 8 else "p" if size == 16 else "x"
        
        newMove = [move1, move2]
        if newMove in completedTurn:
            print("Give a better input.\n")
            continue
        
        ans = whichToMakeGoBoom(board, size, mineBoard, newMove)
        if ans == "KABOOM":
            openSquares = -1
        else:
            currentNum += 1
            openSquares -= 1
        
        printBoard(board, size)
    
    if openSquares == 0:
        win = True
    
    if win:
        print("YAY! CONGRATS!!!")
    else:
        print("Aw man, maybe next time!")
        print("\n\n\n")
        printBoard(mineBoard, size)

main()