# This is the file you need to run to start the game
import pygame, sys
from pygame.locals import *
from gamestate import Gamestate

gamestate = Gamestate()

FPS = 120
FramePerSec = pygame.time.Clock()
pygame.display.set_caption("Game")


class Music:
    def __init__(self):
        self.teller = 1

    def music(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    if self.teller == 1:
                        pygame.mixer.music.pause()
                        self.teller = 0
                    elif self.teller == 0:
                        pygame.mixer.music.unpause()
                        self.teller = 1


pygame.mixer.init()
pygame.mixer.music.load("foto/borissong.flac")
pygame.mixer.music.play(-1)

muziek = Music()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    muziek.music(events)
    gamestate.state_manager(events)
    pygame.display.update()

    FramePerSec.tick(FPS)
