def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, N):
    if row == N:
        return True
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            
            if solve_n_queens_util(board, row + 1, N):
                return True
            
            board[row][col] = 0
    
    return False

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    
    if not solve_n_queens_util(board, 0, N):
        print("Solution does not exist")
        return False
    
    print("Solution:")
    for row in board:
        print(row)

    return True

# Example usage:
n=int(input("n="))
solve_n_queens(n)
