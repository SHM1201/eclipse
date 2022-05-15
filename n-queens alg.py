# n-queens alg

N=5 # dimensions (nxn)

board=[ [0 for i in range(N)] for j in range(N)]
print(board)
def printboard(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ")
        print()

def issafe(board,row,col):
    # check if a queen can be placed in a particular row
    for i in range(col):
        if board[row][i]:
            return False
    
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
            if board[i][j]:
                return False
    
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
            if board[i][j]:
                return False
    return True


def solvenq(board,col):
    # base case
    if col>=N:
        return True
    
    # recursive case
    for i in range(N):
        if issafe(board,i,col):
            board[i][col]=1
            if solvenq(board,col+1):
                return True
            
            board[i][col]=0
    return False

def solve():
    if solvenq(board,0):
        printboard(board)
    
    elif solvenq(board,0)==False:
        print("This solution does not exist")

solve()