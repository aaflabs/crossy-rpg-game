# Pygame development 1
# Start the basic game set up
# Set up the display

# Gain access to the pygame library
import pygame

# size of the screen
SCREEN_WITH = 800
SCREEN_HEIGHT = 800
# Colors according with RGB
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# Create the window of specified size in white to display the game
game_screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT))
# Set the game window color to white
game_screen.fill(WHITE_COLOR)