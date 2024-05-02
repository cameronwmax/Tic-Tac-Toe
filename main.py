import pygame

import brain

# Game variables
WIDTH = 600
HEIGHT = 600
black = (0, 0, 0)
white = (255, 255, 255)


pygame.init()
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 140)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

board = brain.initial_state()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    # Get current turn
    turn = brain.turn(board)


    tiles = []
    for i in range(3):
        # Create row for each column
        row = []
        for j in range(3):
            # Create and draw rects to screen
            rect = pygame.Rect(i * 200, j * 200, 200, 200)
            pygame.draw.rect(screen, white, rect, 3)
            
            # If current space is not empty
            if board[i][j] != brain.EMPTY:
                # Draw X or O to space
                move = moveFont.render(board[i][j], True, white)
                moveRect = move.get_rect()
                moveRect.center = rect.center
                screen.blit(move, moveRect)
            row.append(rect)
        tiles.append(row)

    # Get users clicks
    click = pygame.mouse.get_pressed()[0]
    if click:
        # Get mouse position
        mouse = pygame.mouse.get_pos()
        # Loop in range of rows and columns
        for i in range(3):
            for j in range(3):
                # Check if current space is empty and if where user clickd
                if (board[i][j] == brain.EMPTY and tiles[i][j].collidepoint(mouse)):
                    # Update current board spot to current turn 
                    board[i][j] = turn

    pygame.display.update()
    clock.tick(60)


