import sys, os
import pygame
from pygame.locals import *


# Loads the specified image
def load_image(name, colorkey=None):

    fullname = os.path.join('media', name)

    try:
        image = pygame.image.load(fullname)

    except pygame.error:

        print('Cannot load image: ' + name)
        sys.exit(-1)

    image = image.convert()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))

        image.set_colorkey(colorkey, RLEACCEL)

    return image, image.get_rect()


# Loads a specified level
def loadLevel(level):
    background = pygame.image.load('media/levels/level1/background.png')
    background = background.convert()

    return background
