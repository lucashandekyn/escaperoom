import pygame, sys

from pygame.locals import *

class Kleur(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.klr = "green"
        self.tijd = 0
        self.x = x
        self.y = y
        self.image = pygame.image.load(f"foto/{self.klr}.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, surface):
        self.image = pygame.image.load(f"foto/{self.klr}.png")
        surface.blit(self.image, self.rect)
