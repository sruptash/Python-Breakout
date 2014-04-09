import sys, os
import pygame
from pygame.locals import *


# Loads the specified image and returns it
def load_image(name, colorkey=None):

    try:
        image = pygame.image.load(name)

    except pygame.error as message:

        print('Cannot load image: ' + name)
        print(message)
        sys.exit(-1)

    image = image.convert()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))

        image.set_colorkey(colorkey, RLEACCEL)

    return image, image.get_rect()


# Loads specific text for the screen
def load_text(text, size, color=None):
    font = pygame.font.Font(None, size)
    if color is None:
        loadedText = font.render(text, 1, (255, 255, 255))
    else:
        loadedText = font.render(text, 1, color)

    return loadedText
