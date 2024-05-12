import pygame
import time
import brain
import math

# Game variables
WIDTH = 600
HEIGHT = 600
black = (0, 0, 0)
white = (255, 255, 255)
player = brain.X
game_state = True
ai_turn = False

pygame.init()
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 140)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

board = brain.initial_state()



while game_state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
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

    if brain.turn(board) != player:
        if ai_turn:
            time.sleep(0.5)
            move = brain.minimax(board, -math.inf, math.inf)[0]
            board = brain.result(board, move)
            ai_turn = False
        else:
            ai_turn = True
            
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

    # Check if game is over
    if brain.terminal(board):
        winner = brain.winner(board)

        


    pygame.display.update()



