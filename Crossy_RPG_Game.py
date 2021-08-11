# Pygame development 6
# Implement game classes
# Implement player character class and movement

# Gain access to the pygame library
import pygame
from pygame.constants import KEYUP

# size of the screen
SCREEN_WITH = 800
SCREEN_HEIGHT = 800
# Colors according with RGB
SCREEN_TITLE = 'Crossy RPG'
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Clock used to update game events and frames
clock = pygame.time.Clock()

class Game:

    # Typical rate of 60, equivalent to FPS
    TICK_RATE = 60

    # Initializer for the game class to set up the with, height and title
    def __init__(self, title, width, height) -> None:
        self.title = title
        self.width = width
        self.height = height

        # Create the window of specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        # Set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):

        is_game_over = False
        direction = 0

        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
       
        # Main game loop, used to update all gameplay such as movement, checks,
        # Runs until is_game_over = True
        while not is_game_over:

            # A loop to get all of the events occuring at any given time
            # Events are most often mouse movement, mouse and button clicks, or exit events
            for event in pygame.event.get():
                # If we have a quite type event (exit out) then exit out of the game loop
                if event.type == pygame.QUIT:
                    is_game_over = True
                # Detect when key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # Move up if up key pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Move down if down key pressed
                    if event.key == pygame.K_DOWN:
                        direction = -1
                # Detect when key is released
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            # Redraw the screen to be a blank white window
            self.game_screen.fill(WHITE_COLOR)
            # Update the player position
            player_character.move(direction)
            # Draw the player at the new position
            player_character.draw(self.game_screen)
 
            # Update all game graphics
            pygame.display.update()
            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)

# Generic game object class to be subclassed by other objects in the game
class GameObject:

    def __init__(self, image_path, x, y, width, height) -> None:
        object_image = pygame.image.load(image_path)
        # Scale the image up
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.witdh = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

# Class to represent the character controlled by the player
class PlayerCharacter(GameObject):

    # How many tiles the character moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height) -> None:
        super().__init__(image_path, x, y, width, height)

    # Move function will move character up if direction > 0 and down if < 0
    def move(self, direction):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        

pygame.init()

new_game = Game(SCREEN_TITLE,SCREEN_WITH,SCREEN_HEIGHT)

new_game.run_game_loop()

# Quit pygame and the program
pygame.quit()
quit()



# Draw a rectangle on top of the game screen canvas (x, y, with,height)
# pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
# Draw a circle on top of the game screen (x, y, radius)
# pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

# game_screen.blit(player_image, (375, 375))