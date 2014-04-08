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
    def __init__(self, position, paddleHeight=None):
        """
        Initialize the ball sprite and position. Starts on paddle.

        This function is also used to spawn additional balls, in case
        the user gets a powerup granting them so.
        """

        # The sprite to load
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('Media/balls/ball.png', -1)

        # The size of a ball
        self.width = self.rect.width
        self.height = self.rect.height

        # Initial ball speed
        self.xSpeed = 150.0
        self.ySpeed = 250.0

        # Initial ball direction
        self.xDir = 0.0
        self.yDir = 0.0

        # Initial position
        self.x = float(position[0])
        self.y = float(position[1] - paddleHeight)
        self.rect.centerx = self.x
        self.rect.centery = self.y

        # Check for if ball is on paddle
        self.onPaddle = True

    # Move ball
    def move(self, width, height, seconds, paddle=None):
        """
        If ball is on the paddle, move ball according to
        paddle position.

        Else, move according to window bounds and speed.
        """
        if self.onPaddle:
            self.x = paddle.x
            self.rect.centerx = self.x

        else:
            # X window bounds
            if self.x < (0 + (self.width / 2)):
                self.x = 0 + (self.width / 2)
                self.xDir = -self.xDir

            elif self.x > (width - (self.width / 2)):
                self.x = width - (self.width / 2)
                self.xDir = - self.xDir

            # Y window bounds
            if self.y < (0 + (self.height / 2)):
                self.y = 0 + (self.height / 2)
                self.yDir = -self.yDir

            elif self.y > (height - (self.height / 2) - (paddle.height / 2)):
                return True

            # Set ball trajectory
            self.x += self.xDir * (self.xSpeed * seconds)
            self.y += self.yDir * (self.ySpeed * seconds)

            # Assign to actual rect
            self.rect.centerx = self.x
            self.rect.centery = self.y

    # Launches the ball off the paddle
    def launch(self):
        """
        Will only be called once in main to launch beginning ball.
        """
        self.onPaddle = False
        self.yDir = -1.0
        self.xDir = 0.2
        self.y -= 1
        self.rect.centery = self.y

    # Ball collision with paddle
    def paddleCollide(self, paddle):
        """
        Ball will bounce and change directory based on where it hits
        the paddle.

        The middle of the paddle is a perfect angle reflection,
        While the extremes either decrease or increase the angle
        of reflection depending on the initial xDir.
        Regardless, the yDir is the additive inverse upon collision.
        """
        if self.x != paddle.x:
            ballDist = self.x - paddle.rect.centerx
            percent = ballDist / (paddle.width / 2)

            # set a limit for percent
            if percent < -1.2: percent = -1.2
            if percent > 1.2: percent = 1.2

            # set x direction
            self.setXDirection(self.xDir + percent)

        # Always set y direction to negative inverse after paddle collide
        self.setYDirection(-self.yDir)

    # Ball collision with a brick
    def brickCollide(self, bricks):
        """
        Ball will bounce and change directory based on what side
        it has hit a brick on.

        Hitting the top or bottom translates to the additive inverse of
        the y direction,
        while hitting the left or right is the additive inverse of
        the x direction.
        """
        brickHit = False

        for brick in bricks:
            if not brickHit:
                if (self.y > brick.rect.centery and
                    (self.rect.right > brick.rect.x and
                        self.rect.left < brick.rect.right) and
                        self.yDir < 0):
                    self.setYDirection(-self.yDir)

                elif (self.y < brick.rect.centery and
                      (self.rect.right > brick.rect.x and
                        self.rect.left < brick.rect.right) and
                        self.yDir > 0):
                    self.setYDirection(-self.yDir)

                elif (self.x > brick.rect.centerx and
                      (self.rect.bottom > brick.rect.y and
                        self.rect.top < brick.rect.bottom) and
                        self.xDir < 0):
                    self.setXDirection(-self.xDir)

                elif (self.x < brick.rect.centerx and
                      (self.rect.bottom > brick.rect.y and
                        self.rect.top < brick.rect.bottom) and
                        self.xDir > 0):
                    self.setXDirection(-self.xDir)

            brickHit = True

    # Set the x direction
    def setXDirection(self, xDir):
        """
        Used when spawning new balls, as well as when a collision is detected
        between a ball and an object.

        When new ball is spawned from a powerup, new ball will slightly follow
        trajectory of old ball.
        """
        self.xDir = xDir

    # Set the y direction
    def setYDirection(self, yDir):
        """
        Used when spawning new balls, as well as when a collision is detected
        between a ball and an object.

        When new ball is spawned from a powerup, new ball will slightly follow
        trajectory of old ball.
        """
        self.yDir = yDir
