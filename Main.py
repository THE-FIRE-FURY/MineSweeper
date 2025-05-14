import random

completedTurn = []
completedTurnByNumber = []
completedPointNumber = []
letterSet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def whichToMakeGoBoom(board, size, mineBoard, move):
    
    coordOne = 0
    
    for letter in letterSet:
        
        if (letter == move[0]):
            
            break
        
        coordOne += 1
    
    coordTwo = move[1] - 1
    
    currentMove = [coordOne, coordTwo]
    
    if (mineBoard[coordTwo][coordOne] == "x"):
        
        return "KABOOM"
        
    completedTurn.append(currentMove)
    convertLetterNumToNumNum(board)
    
    fillIn(board, size, move)

def convertTurnToNum(board):
    
    global completedPointNumber
    
    bigList = []
    
    for again in range(len(completedTurnByNumber)):
        
        current = completedTurnByNumber[again]
        
        blank = 0
        
        value = current[1] - 1
        
        blank = value * len(board[0])
        
        blank += current[0]
        
        blank += 1
        
        bigList.append(blank)
        
    completedPointNumber = bigList

def convertLetterNumToNumNum(board):
    
    global completedTurnByNumber
        
    bigList = []
    
    for again in range(len(completedTurn)):
        
        current = completedTurn[again]
        
        blankSlate = [0,0]
        
        blankSlate[1] =  current[1]
        
        count = 0
        
        for letter in letterSet:
            
            if (letter == current[0]):
                
                break
            
            count += 1
            
        blankSlate[0] = count
        
        bigList.append(blankSlate)
        
    completedTurnByNumber = bigList
    
    convertTurnToNum(board)
    
def fillIn(board, size, move):
    
    count = 0
    
    for rep in letterSet:
        
        if (rep == move[0]):
            
            break
        
        count += 1
        
    coordOne = move[1] - 1
    coordTwo = count
    
    board[coordOne][coordTwo] = '0'
    
    convertLetterNumToNumNum(board)

def checkAround(board, size, move, kaboomCount):

    bCount = kaboomCount - 10
    
    up = True
    down = True
    left = True
    right = True
    
    if (size == 8):
    
        if (move[0] == "a"):
            
            left = False
        
        if (move[0] == "h"):
        
            right = False
            
        if (move[1] == 1):
            
            up = False
            
        if (move[1] == 8):
            
            down = False
        
        if (left == True and bCount > 0):
            
            chooseLeft = random.randint(1, 10)
            
            if (chooseLeft != 10):

                count = 0

                while letterSet[count] != move[0]:

                    count += 1

                count -= 1

                nextMove = [letterSet[count], move[1]]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)   

                bCount -= 1

        if (right == True and bCount > 0):
            
            chooseRight = random.randint(1, 10)
            
            if (chooseRight != 10):

                count = 0

                while letterSet[count] != move[0]:

                    count += 1

                count += 1

                nextMove = [letterSet[count], move[1]]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)  

                bCount -= 1

        if (up == True and bCount > 0):
            
            chooseUp = random.randint(1, 10)
            
            if (chooseUp != 10):

                nextMove = [move[0], move[1]-1]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)    

                bCount -= 1            

        if (down == True and bCount > 0):
            
            chooseDown = random.randint(1, 10)
            
            if (chooseDown != 10):

                nextMove = [move[0], move[1]+1]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)            

                bCount -= 1    

        if (up == True and left == True and bCount > 0):

            chooseUpLeft = random.randint(1, 6)

            if (chooseUpLeft != 6):

                count = 0

                while letterSet[count] != move[0]:

                    count += 1

                count -= 1

                nextMove = [letterSet[count], move[1] - 1]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)

                bCount -= 1

        if (up == True and right == True and bCount > 0):

            chooseUpRight = random.randint(1, 6)

            if (chooseUpRight != 6):

                count = 0

                while letterSet[count] != move[0]:

                    count += 1

                count += 1

                nextMove = [letterSet[count], move[1] - 1]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)

                bCount -= 1

        if (down == True and left == True and bCount > 0):

            chooseDownLeft = random.randint(1, 6)

            if (chooseDownLeft != 6):

                count = 0

                while letterSet[count] != move[0]:

                    count += 1

                count -= 1

                nextMove = [letterSet[count], move[1] + 1]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)

                bCount -= 1

        if (down == True and right == True and bCount > 0):

            chooseDownRight = random.randint(1, 6)

            if (chooseDownRight != 6):

                count = 0

                while letterSet[count] != move[0]:

                    count += 1

                count += 1

                nextMove = [letterSet[count], move[1] + 1]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)

                bCount -= 1
        
        doubleUp = False

        if (up == True):

            if (move[1] >= 3):

                doubleUp = True

        doubleDown = False

        if (down == True):

            if (move[1] <= 6):

                doubleDown = True

        doubleLeft = False

        if (left == True):

            count = 0

            while letterSet[count] != move[0]:

                count += 1

            count -= 2

            if count >= 0:

                doubleLeft = True

        doubleRight = False

        if (right == True):

            count = 0

            while letterSet[count] != move[0]:

                count += 1

            count += 2

            if count <= 8:

                doubleRight = True
                
        if (doubleUp == True and bCount > 0):
            
            chooseDoubleUp = random.randint(1, 5)
            
            if (chooseDoubleUp != 5):

                nextMove = [move[0], move[1]-2]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)    

                bCount -= 1    
                
        if (doubleDown == True and bCount > 0):
            
            chooseDoubleDown = random.randint(1, 5)
            
            if (chooseDoubleDown != 5):

                nextMove = [move[0], move[1]+2]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)    

                bCount -= 1  
                
        if (doubleLeft == True and bCount > 0):
            
            chooseDoubleLeft = random.randint(1, 5)
            
            if (chooseDoubleLeft != 5):
                
                count = 0

                while letterSet[count] != move[0]:

                    count += 1

                count -= 2

                nextMove = [letterSet[count], move[1]]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)   

                bCount -= 1
                
        if (doubleRight == True and bCount > 0):
            
            chooseDoubleRight = random.randint(1, 5)
            
            if (chooseDoubleRight != 5):
                
                count = 0

                while letterSet[count] != move[0]:

                    count += 1

                count += 2

                nextMove = [letterSet[count], move[1]]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)   

                bCount -= 1
                
        if (doubleUp == True and left == True and bCount > 0):
            
            chooseDoubleUpOneLeft = random.randint(1,4)
            
            if (chooseDoubleUpOneLeft != 4):
                
                count = 0
                
                while letterSet[count] != move[0]:

                    count += 1

                count -= 1
                
                nextMove = [letterSet[count], move[1]-2]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)   

                bCount -= 1
                
        if (doubleUp == True and right == True and bCount > 0):
            
            chooseDoubleUpOneRight = random.randint(1,4)
            
            if (chooseDoubleUpOneRight != 4):
                
                count = 0
                
                while letterSet[count] != move[0]:

                    count += 1

                count += 1
                
                nextMove = [letterSet[count], move[1]-2]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)   

                bCount -= 1
                
        if (doubleDown == True and left == True and bCount > 0):
            
            chooseDoubleDownOneLeft = random.randint(1,4)
            
            if (chooseDoubleDownOneLeft != 4):
                
                count = 0
                
                while letterSet[count] != move[0]:

                    count += 1

                count -= 1
                
                nextMove = [letterSet[count], move[1]+2]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)   

                bCount -= 1
                
        if (doubleDown == True and right == True and bCount > 0):
            
            chooseDoubleDownOneRight = random.randint(1,4)
            
            if (chooseDoubleDownOneRight != 4):
                
                count = 0
                
                while letterSet[count] != move[0]:

                    count += 1

                count += 1
                
                nextMove = [letterSet[count], move[1]+2]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)   

                bCount -= 1
                
        if (up == True and doubleLeft == True and bCount > 0):
            
            chooseOneUpDoubleLeft = random.randint(1,4)
            
            if (chooseOneUpDoubleLeft != 4):
                
                count = 0
                
                while letterSet[count] != move[0]:

                    count += 1

                count -= 2
                
                nextMove = [letterSet[count], move[1]-1]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)   

                bCount -= 1
                
        if (up == True and doubleRight == True and bCount > 0):
            
            chooseOneUpDoubleRight = random.randint(1,4)
            
            if (chooseOneUpDoubleRight != 4):
                
                count = 0
                
                while letterSet[count] != move[0]:

                    count += 1

                count += 2
                
                nextMove = [letterSet[count], move[1]-1]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)   

                bCount -= 1
                
        if (down == True and doubleLeft == True and bCount > 0):
            
            chooseOneDownDoubleLeft = random.randint(1,4)
            
            if (chooseOneDownDoubleLeft != 4):
                
                count = 0
                
                while letterSet[count] != move[0]:

                    count += 1

                count -= 2
                
                nextMove = [letterSet[count], move[1]+1]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)   

                bCount -= 1
                
        if (down == True and doubleRight == True and bCount > 0):
            
            chooseOneDownDoubleRight = random.randint(1,4)
            
            if (chooseOneDownDoubleRight != 4):
                
                count = 0
                
                while letterSet[count] != move[0]:

                    count += 1

                count += 2
                
                nextMove = [letterSet[count], move[1]+1]

                completedTurn.append(nextMove)

                fillIn(board, size, nextMove)   

                bCount -= 1
                
        TripleUp = False

        if (up == True):

            if (move[1] >= 4):

                TripleUp = True

        TripleDown = False

        if (down == True):

            if (move[1] <= 5):

                TripleDown = True

        TripleLeft = False

        if (left == True):

            count = 0

            while letterSet[count] != move[0]:

                count += 1

            count -= 3

            if count >= 0:

                TripleLeft = True

        TripleRight = False

        if (right == True):

            count = 0

            while letterSet[count] != move[0]:

                count += 1

            count += 3

            if count <= 8:

                TripleRight = True
                
        convertLetterNumToNumNum(board)

def isPast(letter, size, board):
    
    letterSet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    highestLetter = "-"
    
    if (size == 8):
        
        highestLetter = "h"
        
    elif (size == 16):
        
        highestLetter = "p"
        
    else:
        
        highestLetter = "x"
        
    count = 1
    
    for char in letterSet:
        
        if (char == letter):
            
            break
        
        count += 1
        
    letterH = 8
    letterP = 16
    letterX = 24
    
    if (size > count):
        
        return False
        
    elif (size < count):
        
        return True
    
    convertLetterNumToNumNum(board)
    
def turnOne(board, size, mineCount, mineBoard):
    
    print()
    
    kaboomCount = -1
    
    if (size == 8):
        
        kaboomCount = random.randint(10, 35)
        
    elif (size == 16):
        
        kaboomCount = random.randint(30, 70)
        
    else:
        
        kaboomCount = random.randint(90, 170)
        
    moveOne = []

    work = False
    
    while (work == False):
        
        try:
        
            moveOne = input("Where would you like to select? (Letter first, then Number) ")
            work = True
        
        except:
            
            print("Try again u got this!!!\n")
            work = False
    
    print("\n\n\n")
    
    moveOneSplit = list(moveOne)
    
    oneMoveStr = moveOneSplit[0].lower()
    oneMoveNum = int(moveOneSplit[1])
    
    if (oneMoveNum > size):
        
        oneMoveNum = size
        
    if (isPast(oneMoveStr, size, board)):
        
        if (size == 8):
            
            oneMoveStr = "h"
            
        elif (size == 16):
            
            oneMoveStr = "p"
            
        else:
            
            oneMoveStr = "x"
            
    newMoveOne = [oneMoveStr, oneMoveNum]
    
    completedTurn.append(newMoveOne)
    
    fillIn(board, size, newMoveOne)
    
    surrounding = []
         
    checkAround(board, size, newMoveOne, kaboomCount)
    
    printBoard(board, size)
    
    convertLetterNumToNumNum(board)
    
    addMine(board, kaboomCount, size, mineBoard, newMoveOne)
    
    return kaboomCount
    
def printBoard(board, size):
    
    if (size == 8):
        
        print("    a  b  c  d  e  f  g  h")
        
    elif (size == 16):
        
        print("    a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p")
        
    else:
        
        print("    a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x")
        
    count = 1
    
    print()
    
    for line in range(len(board)):
        
        if (count < 10):
        
            print(count ,end = "   ")
            
            for val in range(len(board)):
                
                print(board[line][val], end = "  ")
            
            print()
            
        else:
        
            print(count , end = "  ")
            
            for val in range(len(board)):
                
                print(board[line][val], end = "  ")
            
            print()
        
        count += 1

    print("\n\n\n")
    
    convertLetterNumToNumNum(board)
    
def addMine(board, mineCount, size, mineBoard, move):
    
    mineLab = []
            
    while (len(mineLab) != mineCount):
        
        randomMine = random.randint(0, size*size)
        
        if (randomMine not in mineLab and randomMine + 1 not in completedPointNumber):
            
            mineLab.append(randomMine)
            
    mineLab.sort()
    
    preCount = 0
    
    count = 0
    
    end = False
    
    for repeat in range(size):
        
        for repeatTwo in range(size):
            
            if (mineLab[preCount] == count):
                
                mineBoard[repeat][repeatTwo] = "x"
                
                preCount += 1
                
                if (preCount == mineCount):
                    
                    end = True
                    break
            
            count += 1
            
        if (end == True):
            
            break

def main():
    
    count = 0
    
    try:
    
        count = int(input("Size 1, 2, or 3? "))
    
    except:
        
        print("Why u need break code? :(")
        return
    
    print()
    
    size = count * 8    
    
    small = [["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"]]
    
    small2 = [["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□"]]
    
    medium = [["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]]
    
    medium2 = [["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]]
    
    large = [["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]]
    
    large2 = [["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]]
    
    sMine = 8
    mMine = 16
    lMine = 24
    
    mineCount = -1
        
    if (size == 8):
        
        mineBoard = small2
        board = small
        mineCount = sMine
        
    elif (size == 16):
        
        mineBoard = medium2
        board = medium
        mineCount = mMine
        
    else:
        
        mineBoard = large2
        board = large
        mineCount = lMine
    
    printBoard(board, size)
    
    mCount = turnOne(board, size, mineCount, mineBoard)
    
    convertLetterNumToNumNum(board)
    
    win = False
    
    openSquares = len(board[0])*len(board[0]) - len(completedTurn) - mCount
    
    currentNum = 1
    
    while (openSquares > 0):
        
        print("Turn ", currentNum , ": What is your move? (Letter first, Then number)", end = " ")
        
        cMove = input()
        
        print("\n\n\n")
    
        moveSplit = list(cMove)
        
        move1 = moveSplit[0].lower()
        move2 = int(moveSplit[1])
        
        if (move2 > size):
        
            move2 = size
        
        if (isPast(move1, size, board)):
            
            if (size == 8):
                
                move1 = "h"
                
            elif (size == 16):
                
                move1 = "p"
                
            else:
                
                move1 = "x"
        
        newMove = [move1, move2]
        
        if (newMove in completedTurn):
            
            print("Give a better input man.\n")
            pass
        
        ans = whichToMakeGoBoom(board, size, mineBoard, newMove)
        
        if (ans == "KABOOM"):
            
            openSquares = -1
        
        currentNum += 1
        
        openSquares -= 1
        
        printBoard(board, size)
        
    if (openSquares == 0):
        
        win = True
        
    if (win == True):
        
        print("YAY! CONGRATS!!!")
        
    else:
        
        print("Aw man, maybe next time!")
    
main()
