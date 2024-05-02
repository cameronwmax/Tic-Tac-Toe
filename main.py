import pygame

# Game variables
WIDTH = 600
HEIGHT = 600
black = (0, 0, 0)
white = (255, 255, 255)
EMPTY = None
X = "X"
O = "O"

pygame.init()
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 140)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def initial_state():
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

def return_turn():
    if board == initial_state():
        return X
    
    x_count = 0
    o_count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1

    if x_count > o_count:
        return O
    else:
        return X

board = initial_state()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    turn = return_turn()


    tiles = []
    for i in range(3):
        row = []
        for j in range(3):
            rect = pygame.Rect(i * 200, j * 200, 200, 200)
            pygame.draw.rect(screen, white, rect, 3)

            if board[i][j] != EMPTY:
                move = moveFont.render(board[i][j], True, white)
                moveRect = move.get_rect()
                moveRect.center = rect.center
                screen.blit(move, moveRect)
            row.append(rect)
        tiles.append(row)


    click, _, _ = pygame.mouse.get_pressed()
    if click == 1:
        mouse = pygame.mouse.get_pos()
        for i in range(3):
            for j in range(3):
                if (board[i][j] == EMPTY and tiles[i][j].collidepoint(mouse)):
                    board[i][j] = turn

    pygame.display.update()
    clock.tick(60)


