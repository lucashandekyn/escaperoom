import pygame, sys
import random

BREEDTE = 1216
HOOGTE = 500
CODE = random.randint(1000,10000)
pygame.init()
FONT = pygame.font.SysFont("None", 32)
LIJST_CORDINATEN_DOOLHOF1 = [
    (0, 180),
    (100, 180),
    (200, 180),
    (300, 180),
    (400, 180),
    (500, 180),
    (600, 180),
    (700, 180),
    (400, 180),
    (700, 180),
    (700, 280),
    (700, 380),
    (0, 330),
    (100, 330),
    (200, 330),
    (300, 330),
    (400, 330),
    (500, 330),
    (500, 380),
    (0, 380),
    (100, 380),
    (200, 380),
    (300, 380),
    (400, 380),
    (0, 530),
    (100, 530),
    (200, 530),
    (300, 530),
    (400, 530),
    (500, 530),
    (800, 380),
    (900, 380),
    (600, 530),
    (700, 530),
    (800, 530),
    (900, 380),
    (900, 530),
    (900, 280),
    (1200, 30),
    (900, 180),
    (1100, 30),
    (1100, 80),
    (1100, 180),
    (1100, 380),
    (1100, 480),
    (1100, 530),
    (0, 30),
    (100, 30),
    (200, 30),
    (300, 30),
    (400, 30),
    (500, 30),
    (600, 30),
    (700, 30),
    (800, 30),
    (900, 30),
    (1000, 30),
    (1000, 530),
]
LIJST_COORDS_OMG = [
    (330, 145),
    (340, 445),
    (260, 279),
    (370, -5),
    (550, 295),
    (630, 118),
    (710, 415),
    (830, 315),
    (1030, 235),
    (1130, 395),
]