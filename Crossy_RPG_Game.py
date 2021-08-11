# Pygame development 5
# Implement game classes
# Implement generic game object class

# Gain access to the pygame library
import pygame

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
        game_screen = pygame.display.set_mode((width, height))
        # Set the game window color to white
        game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):

        is_game_over = False

        # A loop to get all of the events occuring at any given time
        # Events are most often mouse movement, mouse and button clicks, or exit events
        
        while not is_game_over:

            for event in pygame.event.get():
                # If we have a quite type event (exit out) then exit out of the game loop
                if event.type == pygame.QUIT:
                    is_game_over = True

                print(event)
 
            # Update all game graphics
            pygame.display.update()
            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)

pygame.init()

new_game = Game(SCREEN_TITLE,SCREEN_WITH,SCREEN_HEIGHT)

new_game.run_game_loop()

class GameObject:

    def __init__(self, image_path, x, y, width, height) -> None:
        object_image = pygame.image.load(image_path)
        # Scale the image up
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

# Quit pygame and the program
pygame.quit()
quit()



# Draw a rectangle on top of the game screen canvas (x, y, with,height)
# pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
# Draw a circle on top of the game screen (x, y, radius)
# pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

# game_screen.blit(player_image, (375, 375))