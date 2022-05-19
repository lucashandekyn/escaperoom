from cgitb import text
from json import load
import pygame, sys
from pygame.locals import *
from constanten import BREEDTE, HOOGTE, FONT
from boris import Player


class World:
    def __init__(
        self,
        background: str,
        doors: list,
        carracters,
        kist,
        bomen,
        player,
        walktype: str,
        kleurcode: list,
    ):
        self.doors = doors
        self.carracters = carracters
        self.kist = kist
        self.bomen = bomen
        self.DISPLAYSURF = pygame.display.set_mode((BREEDTE, HOOGTE))
        self.background = pygame.image.load(f"foto/{background}.png")
        self.boris = player
        self.walktype = walktype
        self.user_text = ""
        self.timer = 240
        self.timer2 = 240
        self.timer3 = 240
        self.kleurcodes = kleurcode
        self.tablet = pygame.image.load("foto/tablet.png")

    def act(self, tekst_kist):
        self.DISPLAYSURF.blit(self.background, (0, 0))
        # overloop eerst lijst een self.carracters en dan de tweede lijst self.bomen
        for car in self.carracters + self.bomen + self.doors:
            car.draw(self.DISPLAYSURF)
        # teken van kleurcodes als dit nodig is
        for car in self.kleurcodes:
            car.draw(self.DISPLAYSURF)

        # besturen van de kist in de wereld
        if self.kist is not None:
            self.kist.draw(self.DISPLAYSURF)

            if self.boris.rect.colliderect(self.kist.rect) and not self.kist.open:
                self.code_renderen()
                self.kist.praat(tekst_kist, self.DISPLAYSURF)
                if self.kist.code_chek(self.user_text):
                    self.boris.boekentasje.append(self.kist.inventory)
                    self.kist.open = True
                    self.user_text = ""

            if self.kist.open and self.timer > 0:
                self.kist.praat(
                    f"Boris heeft sleutel {self.kist.inventory[3]} gevonden",
                    self.DISPLAYSURF,
                )
                self.timer -= 1
        # einde besturen kist in de wereld

        if self.walktype == "walktype1":
            self.boris.update(0, HOOGTE, 0, BREEDTE)
        elif self.walktype == "walktype2":
            self.boris.doolhofwalk()
        elif self.walktype == "walktype3":
            self.boris.wereld_1_walk()
        elif self.walktype == "walk_omg":
            self.boris.walk_omg()
        elif self.walktype =="laatste_walk":
            self.boris.laatste_walk()
        self.boris.draw(self.DISPLAYSURF)

    def teleport(self, x: int, y: int, name: str):
        for car in self.carracters:
            if car.name == name:
                car.rect.center = (x, y)

    def teleportplayer(self, player, x: int, y: int):
        player.rect.center = (x, y)

    def code_renderen(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                else:
                    self.user_text += event.unicode
        self.text_surface = FONT.render(self.user_text, True, (0, 0, 0))
        self.text_surface_rect = self.text_surface.get_rect()
        self.text_surface_rect.center = ((BREEDTE // 2) - 5, HOOGTE // 3)
        self.tablet = pygame.image.load("foto/tablet.png")

        self.tablet_rect = self.tablet.get_rect()
        self.tablet_rect.center = (BREEDTE // 2 - 8, HOOGTE // 3 + 44)
        self.DISPLAYSURF.blit(self.tablet, self.tablet_rect)
        self.DISPLAYSURF.blit(self.text_surface, self.text_surface_rect)

    # als we de personage iets willen doen zeggen
    def praat(self, tekst: str, player_rect, carracter):
        if carracter.rect.colliderect(player_rect):
            self.text_surface = FONT.render(tekst, True, (0, 0, 0))
            self.text_surface_rect = self.text_surface.get_rect()
            self.text_surface_rect.topleft = (10, 430)
            self.praatbalk = pygame.image.load("foto/tekstbalk.png")
            self.praatbalk_rect = self.praatbalk.get_rect()
            self.praatbalk_rect.bottomleft = (0, 498)
            self.DISPLAYSURF.blit(self.praatbalk, self.praatbalk_rect)
            self.DISPLAYSURF.blit(self.text_surface, self.text_surface_rect)

    def minigame_win_lose(self, key, player, level_played, tekst_lose):

        if (key in player.boekentasje) and (self.timer2 > 0) and level_played:
            self.text_surface = FONT.render(
                f"Boris heeft als beloning sleutel {str(key)[3]} gekregen", True, (0, 0, 0)
            )
            self.text_surface_rect = self.text_surface.get_rect()
            self.text_surface_rect.topleft = (10, 430)
            self.DISPLAYSURF.blit(self.praatbalk, self.praatbalk_rect)
            self.DISPLAYSURF.blit(self.text_surface, self.text_surface_rect)
            self.timer2 -= 1
        elif self.timer2 > 0 and level_played:
            self.text_surface = FONT.render(tekst_lose, True, (0, 0, 0))
            self.text_surface_rect = self.text_surface.get_rect()
            self.text_surface_rect.topleft = (10, 430)
            self.DISPLAYSURF.blit(self.praatbalk, self.praatbalk_rect)
            self.DISPLAYSURF.blit(self.text_surface, self.text_surface_rect)
            self.timer2 -= 1

    def act_kleurcode(self, player, kleurcodes, kleur):
        kleur_cijfer = self.boris.kleur_codes_collision(player, kleurcodes)

        if kleur_cijfer == 1:
            kleur.klr = "red"

        if kleur_cijfer == 2:
            kleur.klr = "blue"

        if kleur_cijfer == 3:
            kleur.klr = "yellow"

        if kleur_cijfer == 4:
            kleur.klr = "green"

    def code_check(self, kleurenlijst, juistlijst):
        tel = 0
        correctie = [False, False, False, False]
        for kleur in kleurenlijst:
            geg = kleur.klr
            if geg == juistlijst[tel]:
                correctie[tel] = True
                tel += 1
        return correctie

    def kleurcode_key(self, kleurenlijst, juistlijst, player):
        lijst = self.code_check(kleurenlijst, juistlijst)
        if False not in lijst and "key7" not in player.boekentasje:
            player.boekentasje.append("key7")
        if self.timer3 > 0 and "key7" in player.boekentasje:
            self.text_surface = FONT.render(
                "Boris heeft sleutel 7 gevonden", True, (0, 0, 0)
            )
            self.text_surface_rect = self.text_surface.get_rect()
            self.text_surface_rect.topleft = (10, 430)
            self.praatbalk = pygame.image.load("foto/tekstbalk.png")
            self.praatbalk_rect = self.praatbalk.get_rect()
            self.praatbalk_rect.bottomleft = (0, 498)
            self.DISPLAYSURF.blit(self.praatbalk, self.praatbalk_rect)
            self.DISPLAYSURF.blit(self.text_surface, self.text_surface_rect)
            self.timer3 -= 1
