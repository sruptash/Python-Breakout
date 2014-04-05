import sys, os
import pygame
from pygame.locals import *
from loaders import *


class Paddle(pygame.sprite.Sprite):
    """
    Defines the paddle for the game, as well as how it moves around the screen.

    The paddle will have 5 sizes, identified as a number from 1 - 5. Normal size is
    3.

    The paddle can only move left or right (or up/down, depending on the orientation of the level),
    and has a fixed speed that does not change.
    """

    # Initialize the paddle
    def __init__(self, width, height):

        # The sprite to load
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('Media/paddle.png', -1)

        # The starting size for our paddle.
        # Height will always remain 8
        self.width = 28
        self.height = 8

        # The speed of the paddle
        self.speed = 5

        # The starting position of the paddle
        self.x = (width / 2) - 14
        self.y = height - 8
        self.rect.move(self.x, self.y)


    # Moves the paddle when arrow key left/right are pushed
    def move(self, key):

        if (key == K_RIGHT):
            self.x += self.speed

        elif (key == K_LEFT):
            self.x -= self.speed

        # Move sprite
        self.rect.move(self.x, self.y)
