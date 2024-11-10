def is_safe(board ,row ,col, n):
    for i in range(row):
        if board[i][col]==1:
            return False
    for i ,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,n)):
        if board[i][j]==1:
            return False
    return True
def n_util(board,row,n):
    if row==n:
        return True
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col]=1
            if n_util(board,row+1,n):
                return True
            board[row][col]=0
    return False
def solve_n(n):
    board=[[0]*n for _ in range(n)]
    if not n_util(board,0 ,n):
        return 0
    for row in board:
        print(row)
    return True
i=9
solve_n(i)
