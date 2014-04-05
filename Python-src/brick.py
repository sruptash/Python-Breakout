import sys, os
import pygame
from pygame.locals import *
from loaders import *




class Brick(pygame.sprite.Sprite):
    """
    Defines a brick and its characteristics. This class will be used
    in conjunction with a level loader to load multiple bricks to the screen.

    The brick will be defined by position, color, and whether or not it has a powerup
    """

    # Initialize the brick
    def __init__(self, x, y, color, powerup=None):
        """
        Initialize the brick sprite and position.
        """

        # The sprite to load
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('bricks/' + color + 'Brick.png', -1)
        self.image.convert()

        # Brick initial position
        self.rect.x = x
        self.rect.y = y

        # Powerup embedded in brick
        if powerup == None:
            self.powerup = None

        else:
            self.powerup = powerup
