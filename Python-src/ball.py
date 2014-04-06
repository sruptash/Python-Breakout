import sys, os
import pygame
from pygame.locals import *
from loaders import *




class Ball(pygame.sprite.Sprite):
    """
    Defines the ball and its characteristics, including how it interacts with
    other objects.

    It Initializes on top of the paddle, and will be launched when the user hits
    the space bar.

    It is important to note that other balls may be in game, so these must be kept
    track of as well.

    The ball will also have an initial speed that ramps up from certain
    events (breaking a red brick, certain number of paddle hits, etc.).
    The xDir and yDir will change depending on where the ball hits, and 
    these in turn will determine where the ball is going.
    """

    # Initialize the starting ball
    def __init__(self, paddleHeight, paddlePos):
        """
        Initialize the ball sprite and position. Starts on paddle.
        """

        # The sprite to load
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('balls/ball.png', -1)

        # The size of a ball
        self.width = self.rect.width
        self.height = self.rect.height

        # Initial ball speed
        self.speed = 5

        # Initial ball direction
        self.xDir = 0.0
        self.yDir = 0.0

        # Initial position
        self.x = paddlePos[0]
        self.y = paddlePos[1] - paddleHeight
        self.rect.centerx = self.x
        self.rect.centery = self.y

        # Check for if ball is on paddle
        self.onPaddle = True

    # Move ball
    def move(self, paddleX=None):
        """
        If ball is on the paddle, move ball according to
        paddle position.

        Else, move according to collision and speed.
        """

        if self.onPaddle:
            self.x = paddleX
            self.rect.centerx = self.x
