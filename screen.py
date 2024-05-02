import pygame


WIDTH = 400
HEIGHT = 400
vertical_x = WIDTH / 3
horizontal_y = HEIGHT /3

class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 400))

        # Draw two vertical lines to the screen
        pygame.draw.line(self.screen, "white", (vertical_x, 0), (vertical_x, HEIGHT), 5)
        pygame.draw.line(self.screen, "white", (vertical_x * 2, 0), (vertical_x * 2, HEIGHT), 5)

        # Draw two horizontal lines to the screen
        pygame.draw.line(self.screen, "white", (0, horizontal_y), (WIDTH, horizontal_y), 5)
        pygame.draw.line(self.screen, "white", (0, horizontal_y * 2), (WIDTH, horizontal_y * 2), 5)