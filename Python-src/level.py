import sys, os
import pygame
import random
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
        self.background, self.rect = load_image('Media/levels/' + level + '/background.png')

        # Load bricks
        self.brickSprites = pygame.sprite.Group()

        brickFile = open('Media/levels/' + level + '/layout.lvl', 'r')
        for line in brickFile:
            brickInfo = line.split()

            # Random powerups, 50% chance of getting a powerup
            powerup = random.choice('aabbccdeefgggggggggg')
            
            # A = growing paddle, 10% chance 
            if powerup == 'a':
                powerup = None

            # B = laser, 10% chance
            elif powerup == 'b':
                powerup = None
            
            # C = multiball, 10% chance
            elif powerup == 'c':
                powerup = None
            
            # D = extra life, 5% chance
            elif powerup == 'd':
                powerup = None
            
            # E = shrink, 10% chance
            elif powerup == 'e':
                powerup = None

            # F = lose life, 5% chance
            elif powerup == 'f':
                powerup = None
                
            # G = nothing, 50% chance
            else:
                powerup = None

            # Adds brick

            brick = Brick(int(brickInfo[1]), int(brickInfo[2]), brickInfo[0], powerup)
            self.brickSprites.add(brick)
