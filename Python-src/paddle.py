import sys, os
import pygame
from pygame.locals import *
from loaders import *

import ball


class Paddle(pygame.sprite.Sprite):
    """
    Defines the paddle for the game, as well as how it moves around the screen.

    The paddle will have 5 sizes, identified as a number from 1 - 5. Normal size is
    3.

    The paddle can only move on one axis (left/right, or up/down)
    and has a fixed speed that does not change.
    """

    # Initialize the paddle
    def __init__(self, width, height):

        # The sprite to load
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('Media/paddles/paddle.png', -1)
        self.image.convert()

        # The starting size for our paddle.
        # Height will always remain the same
        self.width = self.rect.width
        self.height = self.rect.height

        # The speed of the paddle
        self.speed = 900.0

        # Initial position
        self.x = float(width / 2)
        self.y = float(height - 20)
        self.rect.centerx = self.x
        self.rect.centery = self.y

    # Moves the paddle when arrow key left/right are pushed
    def move(self, key, width, height, ball, seconds):
        """
        Key presses will change depending on orientation of the screen.
        Orientation will vary from level to level, so key presses should change
        accordingly. This function also makes sure the paddle does not move
        off the screen
        """

        if (key == K_RIGHT):
            self.x += self.speed * seconds
            if self.x > (width - (self.width / 2)):
                self.x = width - (self.width / 2)

            self.rect.centerx = self.x

            if ball.onPaddle:
                ball.move(width, height, seconds, self)

        elif (key == K_LEFT):
            self.x -= self.speed * seconds
            if self.x < (0 + (self.width / 2)):
                self.x = 0 + (self.width / 2)

            self.rect.centerx = self.x

            if ball.onPaddle:
                ball.move(width, height, seconds, self)

