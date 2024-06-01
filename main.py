import pygame
import time
import brain
import math

# Game variables
WIDTH = 600
HEIGHT = 600
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)
player = brain.X
ai_turn = False

pygame.init()
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 140)
gameOverFont = pygame.font.Font("OpenSans-Regular.ttf", 100)
winnerFont = pygame.font.Font("OpenSans-Regular.ttf", 80)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screenRect = screen.get_rect()

board = brain.initial_state()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(black)

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

    # Variable for game_over state
    game_over = brain.terminal(board)
    
    if not game_over:
        # AI move
        if brain.turn(board) != player:
            if ai_turn:
                time.sleep(0.5)
                # Get move for computer
                move = brain.minimax(board, 8, -math.inf, math.inf, True)[0]
                # Update board with computers move
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
    if game_over:
        # Draw the game over text
        winner = brain.winner(board)
        game_over_text = gameOverFont.render("Game Over", True, white)
        game_over_rect = game_over_text.get_rect()
        game_over_rect.center = screenRect.center
        pygame.draw.rect(screen, gray, game_over_rect, 0)
        screen.blit(game_over_text, game_over_rect)

        # Draw the winner/tie text
        if winner == None:
            winner_text = gameOverFont.render("Tie", True, white)
        else:
            winner_text = winnerFont.render(f"Player {winner} Wins!", True, white)
        winner_text_rect = winner_text.get_rect()
        winner_text_rect.center = [WIDTH / 2, 150]
        pygame.draw.rect(screen, gray, winner_text_rect, 0)
        screen.blit(winner_text, winner_text_rect)  

        # Draw the restart text
        restart_text = winnerFont.render("Restart", True, white)
        restart_text_rect = restart_text.get_rect()
        restart_text_rect.center = [WIDTH / 2, 450]
        pygame.draw.rect(screen, gray, restart_text_rect, 0)
        screen.blit(restart_text, restart_text_rect)

        # Check if player clicks resart
        click = pygame.mouse.get_pressed()[0]
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if restart_text_rect.collidepoint(mouse):
                time.sleep(0.2)
                # Reset the game board
                board = brain.initial_state()
                ai_turn = False

    pygame.display.flip()



