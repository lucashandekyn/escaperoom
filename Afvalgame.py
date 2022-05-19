from black import main
import pygame, sys, random
from pygame.math import Vector2


pygame.init()
cell_grootte = 15
cell_aantal_x = 40
cell_aantal_Y = 30

scherm = pygame.display.set_mode(
    (cell_aantal_x * cell_grootte, cell_aantal_Y * cell_grootte)
)
clock = pygame.time.Clock()
afval = pygame.image.load("foto/vuilniszak.png").convert_alpha()
game_font = pygame.font.SysFont("None", 25)

SCHERM_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCHERM_UPDATE, 150)

# 1:18 - 1:38
class Collector:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.richting = Vector2(1, 0)
        self.new_block = False

        self.boris_up = pygame.image.load("foto/borisBack.png").convert_alpha()
        self.boris_down = pygame.image.load("foto/borisFront.png").convert_alpha()
        self.boris_left = pygame.image.load("foto/borisLeft.png").convert_alpha()
        self.boris_right = pygame.image.load("foto/borisRight.png").convert_alpha()

        self.vuilniszak = pygame.image.load("foto/vuilniszak.png").convert_alpha()

        self.tail = pygame.image.load("foto/vuilniszak.png").convert_alpha()

    def draw_collector(self):
        self.update_boris_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_positie = int(block.x * cell_grootte)
            y_positie = int(block.y * cell_grootte)
            block_rect = pygame.Rect(x_positie, y_positie, cell_grootte, cell_grootte)

            if index == 0:
                scherm.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                scherm.blit(self.vuilniszak, block_rect)
            else:
                scherm.blit(self.vuilniszak, block_rect)

    def update_boris_graphics(self):
        boris_richting = self.body[1] - self.body[0]
        if boris_richting == Vector2(1, 0):
            self.head = self.boris_left
        if boris_richting == Vector2(-1, 0):
            self.head = self.boris_right
        if boris_richting == Vector2(0, 1):
            self.head = self.boris_up
        if boris_richting == Vector2(0, -1):
            self.head = self.boris_down

    def update_tail_graphics(self):
        self.tail = self.vuilniszak

    # tail_richting = self.body[-2] - self.body[-1]
    #        if tail_richting == Vector2(1, 0):
    #          self.head = self.tail_left
    #       if tail_richting == Vector2(-1, 0):
    #          self.head = self.tail_right
    #     if tail_richting == Vector2(0, 1):
    #        self.head = self.tail_up
    #   if tail_richting == Vector2(0, -1):
    #      self.head = self.tail_down

    def beweging_collector(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.richting)
            self.body = body_copy[:]
            self.new_block = False

        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.richting)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


class Afval:
    def __init__(self):
        self.randomize()

    def draw_afval(self):
        afval_rect = pygame.Rect(
            int(self.positie.x * cell_grootte),
            int(self.positie.y * cell_grootte),
            cell_grootte,
            cell_grootte,
        )

        scherm.blit(afval, afval_rect)

    def randomize(self):
        self.x = random.randint(0, cell_aantal_x - 2)
        self.y = random.randint(0, cell_aantal_Y - 2)
        self.positie = Vector2(self.x, self.y)


class Main_afval:
    def __init__(self):
        self.collector = Collector()
        self.afval = Afval()
        

    def reset(self):
        self.collector.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.collector.richting = Vector2(1, 0)
        self.collector.new_block = False

    def update(self):
        self.collector.beweging_collector()
        self.check_collision()
        self.check_fail()
        backgr = pygame.image.load("foto/trashworld.png")
        scherm.blit(backgr,(0,0))

    def draw_elementen(self):
        self.afval.draw_afval()
        self.collector.draw_collector()
        self.draw_score()
        
    def check_collision(self):
        if self.afval.positie == self.collector.body[0]:
            self.afval.randomize()
            self.collector.add_block()
        for block in self.collector.body[1:]:
            if block == self.afval.positie:
                self.afval.randomize()

    def check_fail(self):
        if (
            not 0 <= self.collector.body[0].x < cell_aantal_x
            or not 0 <= self.collector.body[0].y < cell_aantal_Y
        ):
            return True
        for block in self.collector.body[1:]:
            if block == self.collector.body[0]:
                return True

    def win(self):
        if int(len(self.collector.body) - 3) == 15:
            return True

    def draw_score(self):
        score_text = str(len(self.collector.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_grootte * cell_aantal_x + 60)
        score_y = int(cell_grootte * cell_aantal_Y)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        afval_rect = afval.get_rect(midright=(score_x - 5, score_rect.centery))
        bg_rect = pygame.Rect(
            afval_rect.left,
            afval_rect.top,
            afval_rect.width + score_rect.width + 5,
            afval_rect.height,
        )
        pygame.draw.rect(scherm, (164, 209, 61), bg_rect)
        scherm.blit(score_surface, score_rect)
        scherm.blit(afval, afval_rect)
        pygame.draw.rect(scherm, (56, 74, 12), bg_rect, 2)

    def afval_run(self, object, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCHERM_UPDATE:
                self.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.collector.richting.y != 1:
                        self.collector.richting = Vector2(0, -1)

                elif event.key == pygame.K_DOWN:
                    if self.collector.richting.y != -1:
                        self.collector.richting = Vector2(0, 1)

                elif event.key == pygame.K_RIGHT:
                    if self.collector.richting.x != -1:
                        self.collector.richting = Vector2(1, 0)

                elif event.key == pygame.K_LEFT:
                    if self.collector.richting.x != 1:
                        self.collector.richting = Vector2(-1, 0)
        
        object.draw_elementen()
