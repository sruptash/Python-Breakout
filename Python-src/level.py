import sys, os
import pygame
from pygame.locals import *
from loaders import *

from brick import Brick




class Level(pygame.sprite.Sprite):
    """
    Class used to define the current level that is being played.
    This class will also be used to define the menu (aka level 0)
    on startup.
    """

    # Initialize the level
    def __init__(self, level):
        """
        Initialize the level. If 'level0', then Initialize the menu.

        This function will return a list of bricks onscreen, as well as a background.
        """

        # The sprite to load
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('bricks/' + color + 'Brick.png', -1)

        # Brick initial position
        self.rect.x = x
        self.rect.y = y

        # Powerup embedded in brick
        if powerup == None:
            self.powerup = None

        else:
            self.powerup = powerup