import pygame, sys
from pygame.locals import *
from constanten import BREEDTE, HOOGTE
from boris import Player


class World:
    def __init__(self, background:str, carracters,boris):
        self.carracters=carracters
        self.DISPLAYSURF = pygame.display.set_mode((BREEDTE,HOOGTE))
        self.background = pygame.image.load(f"foto/{background}.png")
        self.boris=boris

    def act(self):
        self.DISPLAYSURF.blit(self.background, (0,0))
        for car in self.carracters:
            car.draw(self.DISPLAYSURF)

        self.boris.update()
        self.boris.draw(self.DISPLAYSURF)
        
    def teleportcisse(self,x:int,y:int):
        for car in self.carracters:
            if car.name=="Cisse":
                car.x=x
                car.y=y
                