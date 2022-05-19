from tkinter import Y
import pygame, sys
from pygame.locals import *

from boris import Player

class trees(pygame.sprite.Sprite):
    def __init__(self,soort:str,x:int,y:int):#geebruik tuple/list voor x,y is een mogelijkheid
        super().__init__()
        self.soort=soort
        self.image=pygame.transform.scale(pygame.image.load(f"foto/{self.soort}Py.png"),(100,100))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)#gebruik maken van een positeie in tuple/list is een mogelijkheid

    def draw(self,surface)->None:
        surface.blit(self.image, self.rect)