import pygame, sys
from pygame.locals import *
from constanten import BREEDTE, HOOGTE


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, boekentasje):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(f"foto/borisFront.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.boekentasje = boekentasje
        self.tijd = 0

    def update(self, boven, onder, links, rechts):
        pressed_key = pygame.key.get_pressed()
        if self.rect.left > links:
            if pressed_key[K_LEFT]:
                self.rect.move_ip(-2, 0)
                self.image = pygame.image.load("foto/BorisLeft.png")
        if self.rect.right < rechts:
            if pressed_key[K_RIGHT]:
                self.rect.move_ip(2, 0)
                self.image = pygame.image.load("foto/BorisRight.png")
        if self.rect.top > boven:
            if pressed_key[K_UP]:
                self.rect.move_ip(0, -2)
                self.image = pygame.image.load("foto/BorisBack.png")
        if self.rect.bottom < onder:
            if pressed_key[K_DOWN]:
                self.rect.move_ip(0, 2)
                self.image = pygame.image.load("foto/BorisFront.png")

    def doolhofwalk(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-2, 0)
            self.image = pygame.image.load("foto/BorisLeft.png")
        elif pressed_key[K_RIGHT] and self.rect.right < BREEDTE:
            self.rect.move_ip(2, 0)
            self.image = pygame.image.load("foto/BorisRight.png")
        elif pressed_key[K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -2)
            self.image = pygame.image.load("foto/BorisBack.png")
        elif pressed_key[K_DOWN] and self.rect.bottom < HOOGTE:
            self.rect.move_ip(0, 2)
            self.image = pygame.image.load("foto/BorisFront.png")

    def wereld_1_walk(self):
        if 29 < self.rect.left and self.rect.left <= 223 and self.rect.bottom <= 164:
            self.update(0, 163, 31, BREEDTE)
        elif 221 <= self.rect.left and self.rect.right < BREEDTE + 1:
            self.update(0, 420, 222, BREEDTE)

    def laatste_walk(self):
        self.update(50, HOOGTE, 0, BREEDTE)
        
    def collisiondoolhof(self, player, objecten):
        pressed_key = pygame.key.get_pressed()
        if pygame.sprite.spritecollideany(player, objecten):
            if pressed_key[K_LEFT]:
                self.rect.move_ip(10, 0)
                self.image = pygame.image.load("foto/BorisRight.png")
                # ad delay to not clip trough trees
                pygame.time.delay(500)
            if pressed_key[K_RIGHT]:
                self.rect.move_ip(-10, 0)
                self.image = pygame.image.load("foto/BorisLeft.png")
                # ad delay to not clip trough trees
                pygame.time.delay(500)
            if pressed_key[K_UP]:
                self.rect.move_ip(0, 10)
                self.image = pygame.image.load("foto/BorisFront.png")
                # ad delay to not clip trough trees
                pygame.time.delay(500)
            if pressed_key[K_DOWN]:
                self.rect.move_ip(0, -10)
                self.image = pygame.image.load("foto/BorisBack.png")
                # ad delay to not clip trough trees
                pygame.time.delay(500)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def kleur_codes_collision(self, player, kleurcodes):
        pressed_key = pygame.key.get_pressed()
        nummer_return = 0
        if pygame.sprite.spritecollideany(player, kleurcodes):
            if pressed_key[K_n]:
                self.tijd += 1
                if 80 > self.tijd >= 1:
                    nummer_return = 1
                elif 160 > self.tijd >= 80:
                    nummer_return = 2
                elif 240 > self.tijd >= 160:
                    nummer_return = 3
                elif 320 > self.tijd >= 240:
                    nummer_return = 4
                if self.tijd > 320:
                    self.tijd = 0
        return nummer_return

    def walk_omg(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_RIGHT] and self.rect.left > 0:
            self.rect.move_ip(-2, 0)
            self.image = pygame.image.load("foto/BorisLeft.png")
        elif pressed_key[K_LEFT] and self.rect.right < BREEDTE:
            self.rect.move_ip(2, 0)
            self.image = pygame.image.load("foto/BorisRight.png")
        elif pressed_key[K_DOWN] and self.rect.top > 0:
            self.rect.move_ip(0, -2)
            self.image = pygame.image.load("foto/BorisBack.png")
        elif pressed_key[K_UP] and self.rect.bottom < HOOGTE:
            self.rect.move_ip(0, 2)
            self.image = pygame.image.load("foto/BorisFront.png")

    def omg_collision(self, player, objecten):
        if pygame.sprite.spritecollideany(player, objecten):
            player.rect.center = (100, 250)
            if "key4" in self.boekentasje:
                print("It's not a bug, it's a feature!") 
