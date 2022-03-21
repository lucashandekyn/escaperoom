import pygame, sys
from pygame.locals import *

from boris import Player
from npc import Npc
from wereld import World

brecht=Npc(100,100,"Brecht")
carlo=Npc(200,100,"Carlul")
cisse=Npc(200,100,"Cisse")
boris=Player(100,200)

cisses = pygame.sprite.Group()
cisses.add(cisse)
carlos = pygame.sprite.Group()
carlos.add(carlo)
brechts = pygame.sprite.Group()
brechts.add(brecht)

wereld1=World("backgroundpath",[brecht,cisse,carlo],boris)
wereld2=World("backgroundbeach",[brecht,cisse],boris)

class Gamestate:
    def __init__(self):
        self.level=1
    def bots(self):
        if pygame.sprite.spritecollideany(boris,cisses):
            self.level=2
        elif pygame.sprite.spritecollideany(boris,brechts):
            self.level=1
    def state_manager(self):
        self.bots()
        if self.level==1:
            wereld1.act()
        elif self.level==2:
#aanpassen van de waarden voor cisse zijn spawn point/rect.center
            wereld2.teleportcisse(800,400)
            wereld2.act()
            print(cisse.y)

           
