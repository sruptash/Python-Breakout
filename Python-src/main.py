import sys, os
import pygame
from pygame.locals import *

from paddle import Paddle
from ball import Ball
from level import Level
from loaders import *

if not pygame.font: print("Warning, fonts disabled")
if not pygame.mixer: print("Warning, sound disabled")


class BreakoutMain:
    """
    This class is instantiated upon the game being launched.
    This houses information on width, height, and tick rate.

    Note that all loops essential to game function are located
    near the bottom of this file.
    """

    # Keep a list of all levels used. More levels can be added
    # by updating this list.
    # NOTE: "level0" is the menu.
    levels = ["level0",
              "level1",
              "level2",
              "level3",
              "level4",
              "level5"]

    # Here is a tuple with the standard width and height.
    # Change these to change dimensions of screen.
    # NOTE: Window is non-resizeable.
    dimensions = (600, 600)

    # Initialization function
    def __init__(self):
        """
        Initialize a new window using pygame, with a specified w and h.
        Set the caption as well.
        """
        pygame.init()

        # Screen and window settings
        self.width = BreakoutMain.dimensions[0]
        self.height = BreakoutMain.dimensions[1]
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Breakout!')

        # Timer settings
        self.clock = pygame.time.Clock()
        self.elapsed = 0.0

        # Game vars
        self.ballLaunched = False
        self.paused = False

        # Life vars
        self.lives = 3
        self.lifeRadius = 5
        self.lifeX = 0 + 5
        self.lifeY = self.height - 5

        # Score var
        self.score = 0

        self.difficulty = "normal"

    # Used to load sprites to the screen
    def loadSprites(self):
        """
        From here we can load all sprites needed, whether they
        are the paddle, balls, bricks, backgrounds, etc.
        """

        # level
        # Background and bricks defined in here
        self.level = Level('level4')

        # paddle
        self.paddle = Paddle(self.width, self.height)
        self.paddleSprite = pygame.sprite.GroupSingle(self.paddle)

        # ball
        self.mainBall = Ball((self.paddle.x, self.paddle.y),
                             self.paddle.height)
        self.ballSprites = pygame.sprite.RenderPlain(self.mainBall)

    # Draw score
    def drawScore(self):
        """
        Draws the score to the bottom right of the screen.
        """
        text = load_text("Score: %s" % self.score, 18)
        textpos = text.get_rect(bottomright=(self.width,
                                             self.height))
        pygame.draw.rect(self.screen,
                         (0, 0, 0),
                         textpos)
        self.screen.blit(text, textpos)

    # Draw lives
    def drawLives(self):
        """
        Draws the number of lives remaining to the bottom left
        of the screen.
        """
        if self.lives > 0:
                for i in range(self.lives - 1):
                    pygame.draw.circle(self.screen,
                                       (255, 255, 255),
                                       (self.lifeX + (i*10), self.lifeY),
                                       self.lifeRadius)

    # MENU LOOP FUNCTION
    def menuLoop(self):
        """
        Function used to give the user a navigatable menu.
        Once this loop returns, the game begins.
        """
        pass

    # GAME LOOP FUNCTION
    def gameLoop(self):
        """
        Function houses a loop that isrepeated over and over to check
        for new events, such as key presses or events in game.
        """

        # Load our sprites
        self.loadSprites()

        # Set key repeat on
        pygame.key.set_repeat(5, 10)

        # Draw background to screen initially
        self.screen.blit(self.level.background, (0, 0))
        self.level.brickSprites.draw(self.screen)
        self.drawScore()

        while 1:
            seconds = self.elapsed / 1000.0

            # Redraw where paddle and balls used to be
            self.screen.blit(self.level.background,
                             (self.paddle.rect.x, self.paddle.rect.y),
                             self.paddle.rect)
            for ball in self.ballSprites:
                self.screen.blit(self.level.background,
                                 (ball.rect.x, ball.rect.y),
                                 ball.rect)

            # EVENT CHECKER
            for event in pygame.event.get():
                # Window 'X' clicked
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Keys pressed
                if event.type == KEYDOWN:
                    # Quit game
                    if event.key == K_ESCAPE or event.key == K_q:
                        pygame.event.post(pygame.event.Event(QUIT))

                    # Move paddle
                    if (event.key == K_LEFT or
                            event.key == K_RIGHT):
                        self.paddle.move(event.key,
                                         self.width,
                                         self.height,
                                         self.mainBall,
                                         seconds)

                    # Start game by launching the ball
                    if event.key == K_SPACE:
                        if not self.ballLaunched:
                            self.mainBall.launch()
                            self.ballLaunched = True

            # Move balls onscreen
            if self.ballLaunched:
                for ball in self.ballSprites:
                    ballLost = ball.move(self.width,
                                         self.height,
                                         seconds,
                                         self.paddle)

                    # Check if ball went past paddle
                    if ballLost:
                        pygame.time.delay(200)
                        ball.kill()
                        if not self.ballSprites:
                            self.mainBall = Ball((self.paddle.x, self.paddle.y),
                                                 self.paddle.height)
                            self.ballSprites.add(self.mainBall)
                            self.ballLaunched = False

                            # Lose a life, fill in circle where one used to be
                            self.lives -= 1
                            self.drawScore()
                            pygame.draw.circle(self.screen,
                                       (0, 0, 0),
                                       (self.lifeX + ((self.lives - 1)*10), self.lifeY),
                                       self.lifeRadius)

                            # End game if lives are gone
                            if self.lives < 0:
                                return "lost"

            # COLLISION DETECTION
            # Collision detection between ball and paddle
            hitPaddle = pygame.sprite.spritecollide(self.paddle,
                                                    self.ballSprites,
                                                    False)
            if hitPaddle:
                for ball in hitPaddle:
                    ball.paddleCollide(self.paddle)

            # Collision detection between ball and brick
            for ball in self.ballSprites:
                hitBricks = pygame.sprite.spritecollide(ball,
                                                        self.level.brickSprites,
                                                        True)
                ball.brickCollide(hitBricks)
                for brick in hitBricks:
                    self.screen.blit(self.level.background,
                                     (brick.rect.x, brick.rect.y),
                                     brick.rect)
                    self.score += 1
                    # Redraw score
                    self.drawScore()

            # SPRITE DRAW
            # Redraw lives left
            self.drawLives()

            # Redraw sprites
            self.paddleSprite.draw(self.screen)
            self.ballSprites.draw(self.screen)
            pygame.display.update()

            # Keep track of time elapsed
            self.elapsed = self.clock.tick(60)

    # END LOOP FUNCTION
    def endLoop(self, state):
        """
        Called when the game reaches an end state.
        There are 3 possible states:
            -Game Win
            -Game Lose
            -Next Level
        This loop will handle them all accordingly.
        """
        pass

# Start the game
if __name__ == "__main__":
    mainWindow = BreakoutMain()

    while True:
        mainWindow.menuLoop()
        state = mainWindow.gameLoop()
        mainWindow.endLoop(state)
