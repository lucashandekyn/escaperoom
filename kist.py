import pygame, sys
from pygame.locals import *
from constanten import FONT


class Schatkist(pygame.sprite.Sprite):
    def __init__(self, code, x: int, y: int, inventory):
        super().__init__()
        self.code = code
        self.open = False
        self.inventory = inventory
        # TODO foto van schatkist nog maken
        self.image = pygame.image.load(f"foto/chestclosed.png")
        # TODO foto schatkist open
        self.image2 = pygame.image.load(f"foto/chestopen.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # cordinaten
        self.praatbalk = pygame.image.load("foto/tekstbalk.png")

    def code_chek(self, code):
        return self.code == code

    def praat(self, tekst: str, surface: str):
        self.text_surface = FONT.render(tekst, True, (0, 0, 0))
        self.text_surface_rect = self.text_surface.get_rect()
        self.text_surface_rect.topleft = (10, 430)
        self.praatbalk_rect = self.praatbalk.get_rect()
        self.praatbalk_rect.bottomleft = (0, 498)
        surface.blit(self.praatbalk, self.praatbalk_rect)
        surface.blit(self.text_surface, self.text_surface_rect)

    def draw(self, surface):
        if self.open:
            surface.blit(self.image2, self.rect)
        else:
            surface.blit(self.image, self.rect)
