import sys
import os
import pygame
from pygame.locals import *


class BreakoutMain:

    def __init__(self, width=640, height=480):
        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Breakout!')
        self.clock = pygame.time.Clock()


    def loop(self):

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        self.clock.tick(60)


if __name__ == "__main__":
    mainWindow = BreakoutMain()
    mainWindow.loop()