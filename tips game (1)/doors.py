# from msilib.schema import Font
from unicodedata import name
import pygame, sys
from pygame.locals import *
from constanten import FONT

class Doors(pygame.sprite.Sprite):
    def __init__(self,x:int,y:int,name:str):
        super().__init__()
        self.name=name
        #opletten naam van de foto is hoofdletter gevoellig
        self.image=pygame.image.load(f"foto/{self.name}Py.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)