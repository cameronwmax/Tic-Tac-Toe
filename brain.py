X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

def turn(board):
    # Return X if board in initial state
    if board == initial_state:
        return X
    
    x_count = 0
    o_count = 0

    # Loop through rows and columns
    for i in range(3):
        for j in range(3):
            # Update x count if space is X
            if board[i][j] == X:
                x_count += 1
            # Update o count if space if O
            if board[i][j] == O:
                o_count += 1

    # Return marker with higher count
    if x_count > o_count:
        return O
    else:
        return X
    
def actions(board):
    ...

def result(board, action):
    ...

def winner(board):
    """Function to check if there is a winner"""

    # Check for row wins
    for i in range(3):
        if board[i][0] ==  board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        
    # Check for columns wins
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
        

    return None

def terminal(board):
    ...

def utility(board):
    ...

def min_value(board):
    ...

def max_value(board):
    ...

def minimax(board):
    ...