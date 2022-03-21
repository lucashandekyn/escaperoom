import pygame, sys
from pygame.locals import *
from constanten import BREEDTE,HOOGTE

class Player(pygame.sprite.Sprite):
    def __init__(self,x:int,y:int):
        super().__init__()
        self.x=x
        self.y=y
        self.image=pygame.image.load(f"foto/borisFront.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
    def update(self):
        pressed_key = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_key[K_LEFT]:
                self.rect.move_ip(-2, 0)
                self.image =pygame.image.load("foto/BorisLeft.png")
        if self.rect.right < BREEDTE:
            if pressed_key[K_RIGHT]:
                self.rect.move_ip(2, 0)
                self.image =pygame.image.load("foto/BorisRight.png")
        if self.rect.top > 0:        
            if pressed_key[K_UP]:
                self.rect.move_ip(0, -2)
                self.image =pygame.image.load("foto/BorisBack.png")
        if self.rect.bottom < HOOGTE:
            if pressed_key[K_DOWN]:
                self.rect.move_ip(0, 2)
                self.image =pygame.image.load("foto/BorisFront.png")

    def draw(self, surface):
        surface.blit(self.image, self.rect)