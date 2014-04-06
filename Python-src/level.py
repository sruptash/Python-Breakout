import sys, os
import pygame
from pygame.locals import *
from loaders import *

from brick import Brick


class Level():
    """
    Class used to define the current level that is being played.
    This class will also be used to define the menu (aka level 0)
    on startup.
    """

    # Initialize the level
    def __init__(self, level):
        """
        Initialize the level. If 'level0', then Initialize the menu.

        This function will house a list/group of brick sprites, as well
        as the background sprite.
        """
        # Name of level
        self.name = level

        # Load background
        self.background, self.rect = load_image('levels/' + level + '/background.png', None)

        # Load bricks
        self.brickSprites = pygame.sprite.Group()

        brickFile = open('media/levels/' + level + '/layout.lvl', 'r')
        for line in brickFile:
            brickInfo = line.split()
            brick = Brick(int(brickInfo[1]), int(brickInfo[2]), brickInfo[0])
            self.brickSprites.add(brick)
