'''
IMPLEMENTATION DETAILS:
1. Printing the 4*4 board on each turn in the console and wait for user input. This will initially have two cells populated at random with a 2 or 4
2. User will input 1,2,3,4 for left, right,up and down movements
3. Program will then merge all the tiles in given direction and show the latest sums according to rules mentioned above
4. Next it should select a random empty lication in a tile and place 2 or 4
5. Repeat steps 1-4 till one of the cell reaches 2048

'''
import random
import copy
# to fill a cell randomly with 2 or 4
def pickNewValue():#to fill cells randomly woth 2 or 4
    if random.randint(1,8)==2:
        return 4
    else:
        return 2
def addNewValue():
    rowNumber=random.randint(0,boardsize-1)
    colNumber=random.randint(0,boardsize-1)
    while not board[rowNumber][colNumber]==0:#looping till an empty cell is found
        rowNumber=random.randint(0,boardsize-1)
        colNumber=random.randint(0,boardsize-1)
    board[rowNumber][colNumber]=pickNewValue()#placing empty cell with 2 or 4
    

def win():#checking winning condition
    for row in board:
        if 2048 in row:#if 2048 present...Game won
            return True
    return False

def noMoreMoves():
    temporary1=copy.deepcopy(board)
    temporary2=copy.deepcopy(board)
    
    #if after a move if all possible movements after that results a same result. then there are no moves left and game is over
    #the person is lost
    temporary1=mergeWholeBoardDown(temporary1)
    if temporary1==temporary2:
        temporary1=mergeWholeBoardUp(temporary1)
        if temporary1==temporary2:
            temporary1=mergeWholeBoardLeft(temporary1)
            if temporary1==temporary2:
                temporary1=mergeWholeBoardRight(temporary1)
                if temporary1==temporary2:
                    return True
    return False
    
    
    
    

boardsize=4
board=[]
for i in range(boardsize):
    board.append([0]*boardsize)

numNeed=0
while numNeed <2:
    rowNumber=random.randint(0,boardsize-1)
    colNumber=random.randint(0,boardsize-1)
    if board[rowNumber][colNumber]==0:
        board[rowNumber][colNumber]=pickNewValue()
        numNeed+=1

def displayBoard():#to print the board after the move
    large=board[0][0]
    for row in board:
        for ele in row:
            if ele > large:
                large=ele
    spaces=len(str(large))#for correct padding during the display of the board
    for row in board:
        preRow="|"
        for ele in row:
            if ele==0:
                preRow+=" "*spaces+"|"
            else:
                preRow+=(" "*(spaces-len(str(ele))))+str(ele)+"|"
        print(preRow)
    print()


def mergeSingleRowLeft(row):#merge of a single row in the board
    #move everything to extreme left as possible
    for j in range(boardsize-1):
        for i in range(boardsize-1,0,-1):
            #find the empty spaces and move the left values to the empty spaces
            if row[i-1]==0:
                row[i-1]=row[i]
                row[i]=0
    #for merging if left element is present:
    for i in range(boardsize-1):
        #check values. if same add
        if row[i]==row[i+1]:
            row[i]*=2
            row[i+1]=0
    #after adding now move everythig to as left as possible
    for i in range(boardsize-1,0,-1):
        if row[i-1]==0:
            row[i-1]=row[i]
            row[i]=0
                
    return row

def mergeWholeBoardLeft(presentBoard):
    for i in range(boardsize):
        presentBoard[i]=mergeSingleRowLeft(presentBoard[i])
    return presentBoard

'''
To the right move: we reverse the board ,
then merge it using functions available for left
and then we again reverse the resultant board to get the required result
'''
def reverseBoardRow(row):
    return row[::-1]
def mergeWholeBoardRight(presentBoard):
    for i in range(boardsize):
        #reverse every row, perfor  the left operations and reverse again
        presentBoard[i]=reverseBoardRow(presentBoard[i])
        presentBoard[i]=mergeSingleRowLeft(presentBoard[i])
        presentBoard[i]=reverseBoardRow(presentBoard[i])
    return presentBoard
'''
For upward movement, we transpose the board and then perform left operations
then again we transpose back to get the required result.
'''
def transposeBoard(presentBoard):
    for j in range(boardsize):
        for i in range(j,boardsize):
            presentBoard[j][i],presentBoard[i][j]=presentBoard[i][j],presentBoard[j][i]
    return presentBoard

def mergeWholeBoardUp(presentBoard):
    presentBoard=transposeBoard(presentBoard)
    presentBoard=mergeWholeBoardLeft(presentBoard)
    presentBoard=transposeBoard(presentBoard)
    return presentBoard

'''
For Downward movement:
1. Transpose it
2. mergeWholeBoardRight
3. transpose it

'''
def mergeWholeBoardDown(presentBoard):
    presentBoard=transposeBoard(presentBoard)
    presentBoard=mergeWholeBoardRight(presentBoard)
    presentBoard=transposeBoard(presentBoard)
    return presentBoard





print("WELCOME TO 2048...!!!")
print("Goal is to make a cell 2048 by moving the board in left, right, up and down where each move merges the elements if same.")
print("Everytime you need to type 1 for left, 2 for right, 3 for up and 4 for down")
print("Here is the initial Board")
displayBoard()
gameover=False
while not gameover:
    move=int(input("Choose the direction of move: "))
    validMove=True
    temporary=copy.deepcopy(board)
    if move==1:
        board=mergeWholeBoardLeft(board)
    elif move==2:
        board=mergeWholeBoardRight(board)
    elif move==3:
        board=mergeWholeBoardUp(board)
    elif move==4:
        board=mergeWholeBoardDown(board)
    else:
        validMove=False
    if  not validMove:
        print("Invalid move, please choose again")
    else:
        '''
            1. check win or not
            if win leave else add new value
            check for out of moves
            if yes, print the person is lost

        '''
        if win():
            displayBoard()
            print("YOU WON")
            gameover=True
        else:
            addNewValue()
            if noMoreMoves():
                print("Sorry...!!! NO MORE POSSIBLE MOVES...")
                gameover=True
        displayBoard()
    

                
