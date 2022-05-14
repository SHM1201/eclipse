def printBoard(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

def isSafe(board,r,c,n):
    for i in range(c):
        if board[r][i]==1:
            return False
    
    for i,j in zip(range(r,-1,-1),range(c,-1,-1)):
        if board[i][j]==1:
            return False
        
    for i,j in zip(range(r,n,1),range(c,-1,-1)):
        if board[i][j]==1:
            return False

    return True

def placeQueen(board,n,col):
    if col>=n:
        return True

    for i in range(n):
        if isSafe(board,i,col,n):
            board[i][col]=1
            if placeQueen(board,n,col+1):
                return True
            board[i][col]=0
    return False


N = int(input("Enter the number of queens: "))
board=[]

for i in range(N):
    arr=[]
    for j in range(N):
        arr.append(0)
    board.append(arr)

if placeQueen(board,N,0):
    printBoard(board,N)
else:
    print("No solution possible")
