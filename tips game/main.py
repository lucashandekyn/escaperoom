import pygame, sys
from pygame.locals import *

from gamestate import Gamestate

gamestate=Gamestate()

FPS = 120
FramePerSec = pygame.time.Clock()
pygame.display.set_caption("Game")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    gamestate.state_manager()

    pygame.display.update()
    FramePerSec.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()