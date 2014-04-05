import sys, os
import pygame
from paddle import Paddle
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


class BreakoutMain:
    """
    This class is instantiated upon the game being launched.
    This houses information on width, height, and tick rate.
    """

    # Initialization function
    def __init__(self, width=640, height=480):
        """
        Initialize a new window using pygame, with a specified w and h.
        Set the caption and tick rate.
        """

        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Breakout!')
        self.clock = pygame.time.Clock()

    # Used to load sprites to the screen
    def loadSprites(self):
        """
        From here we can load all sprites needed, whether they
        are the paddle, balls, bricks, powerups/powerdowns, etc.
        """

        # paddle
        self.paddle = Paddle.paddle(self.width, self.height)
        self.paddleSprite = pygame.sprite.RenderPlain((self.paddle))

    # Loop function
    def loop(self):
        """
        Function repeated over and over to check for new events,
        such as key presses or events in game.
        """

        # Load our sprites
        self.loadSprites()

        while 1:
            for event in pygame.event.get():
                # Window 'X' clicked
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Escape Key
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))

                    if ((event.key == K_RIGHT)
                            or (event.key == K_LEFT)):
                        self.paddle.move(event.key)

        # Redraw sprites
        self.snake_sprites.draw(self.screen)
        pygame.display.flip()

        # Update screen at 60 frames per second
        pygame.display.update()
        self.clock.tick(60)


# Start the game
if __name__ == "__main__":
    mainWindow = BreakoutMain()
    mainWindow.loop()
