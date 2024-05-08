import copy


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
    """Returns set of all possible actions (i, j) available on the board"""
    moves = []
    # Loops through board appending empty spaces to list
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                moves.append((i, j))

    return moves

def result(board, action):
    """Returns the board that results from making move (i, j) on the board"""
    if action not in actions(board):
        # Raise exception if move is not valid
        print(action)
        raise Exception("Not valid action")
    
    # Split action into i and j
    i, j = action
    # Create copy of board
    temp_board = copy.deepcopy(board)
    # Update board copy with move
    temp_board[i][j] = turn(board)

    # Return updated board copy
    return temp_board


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
    """Returns true if game is over, otherwise returns false"""
    if winner(board) == X or winner(board) == O:
        # Returns True if X or O won the game
        return True
    elif winner(board) == None and len(actions(board)) == 0:
        # Returns True if game is a tie
        return True
    else:
        # Returns false if game is still going
        return False

def utility(board):
    """Returns 1 if X has won the game, -1 if O has won, 0 otherwise"""
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def min_value(board):
    ...

def max_value(board):
    ...

def minimax(board):
    ...