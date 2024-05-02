X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

def turn(state):
    # Return X if board in initial state
    if state == initial_state:
        return X
    
    x_count = 0
    o_count = 0

    # Loop through rows and columns
    for i in range(3):
        for j in range(3):
            # Update x count if space is X
            if state[i][j] == X:
                x_count += 1
            # Update o count if space if O
            if state[i][j] == O:
                o_count += 1

    # Return marker with higher count
    if x_count > o_count:
        return O
    else:
        return X