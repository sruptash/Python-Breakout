import sys
import os
import pygame
from pygame.locals import *


class BreakoutMain:
    """
    
    This class is instantiated upon the game being launched.
    This houses information on width, height, and tick rate.
    """

    # Initialization function
    def __init__(self, width=640, height=480):
        """
        Initialize a new window using pygame, with a specified width and height.
        Set the caption and tick rate.
        """

        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Breakout!')
        self.clock = pygame.time.Clock()

    # Loop function
    def loop(self):
        """
        Function repeated over and over to check for new events,
        such as key presses or events in game.
        """

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

        # Update screen at 60 frames per second
        pygame.display.update()
        self.clock.tick(60)


# Start the game
if __name__ == "__main__":
    mainWindow = BreakoutMain()
    mainWindow.loop()