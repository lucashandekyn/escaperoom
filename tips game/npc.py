from unicodedata import name
import pygame, sys
from pygame.locals import *

class Npc(pygame.sprite.Sprite):
    def __init__(self,x:int,y:int,name:str,):
        super().__init__()
        self.x=x
        self.y=y
        self.name=name
#opletten naam van de foto is hoofdletter gevoellig
        self.image=pygame.image.load(f"foto/{self.name}Py.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,self.y)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
#als we de personage iets willen doen zeggen
    def praat(self, tekst:str):
        print(tekst)

