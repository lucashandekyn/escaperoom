import pygame, sys, random

pygame.init()

cell_size = 25
cell_number = 20

screen = pygame.display.set_mode((cell_number * cell_size * 2, cell_number * cell_size))
pygame.display.set_caption("Oversteek")
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 25)
achtergrond = pygame.image.load("foto/ocean25.png").convert_alpha()


class Player_oversteek:
    def __init__(self):
        self.x = int(cell_number)
        self.y = 0

    def draw_player(self, b):
        self.posx = self.x * cell_size
        self.posy = self.y * cell_size
        player_rect = pygame.Rect(self.posx, self.posy, cell_size, cell_size)
        screen.blit(b, player_rect)


class Bridge:
    def __init__(self):
        self.x = [int(cell_number)]
        self.y = [0]
        self.co = [[int(cell_number), 0]]

    def make_bridge(self):
        overkant = True
        i = 0
        while overkant:
            a = 0
            if self.x[i] == (cell_number - 1):
                a = random.randint(-1, 0)
            elif self.x[i] == 0:
                a = random.randint(0, 1)
            else:
                a = random.randint(-1, 1)
            if a == -1:
                newx = self.x[i] - 1
                self.x.append(newx)
                self.y.append(self.y[i])
                self.co.append([self.x[i + 1], self.y[i + 1]])
            if a == 0:
                newx = self.x[i] + 1
                self.x.append(newx)
                self.y.append(self.y[i])
                self.co.append([self.x[i + 1], self.y[i + 1]])
            if a == 1:
                newy = self.y[i] + 1
                newy2 = newy + 1
                self.y.append(newy)
                self.y.append(newy2)
                self.x.append(self.x[i])
                self.x.append(self.x[i])
                self.co.append([self.x[i + 1], self.y[i + 1]])
                self.co.append([self.x[i + 2], self.y[i + 2]])
                i += 1
            if self.y[i] == (cell_number - 1):
                overkant = False
            i += 1

    def draw_bridge(self, a):
        self.bridgelen = len(self.x)
        for i in range(0, self.bridgelen):
            self.posx = self.x[i] * cell_size
            self.posy = self.y[i] * cell_size
            bridge_rect = pygame.Rect(self.posx, self.posy, cell_size, cell_size)
            screen.blit(a, bridge_rect)


class Main:
    def __init__(self):
        self.t = 0
        self.a = (0, 0, 0)
        self.b = (0, 0, 0)
        self.bridge = Bridge()
        self.boris = Player_oversteek()
        self.bridge.make_bridge()
        self.borisco = [self.boris.x, self.boris.y]

    def draw_elements(self):
        self.bridge.draw_bridge(self.a)
        self.boris.draw_player(self.b)

    def game_over(self):
        if not (self.borisco in self.bridge.co):
            return True

    def win(self):
        if self.borisco[1] == cell_number - 1:
            return True

    def run_game(self, object, events, character):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.boris.y -= 1
                if event.key == pygame.K_DOWN:
                    self.boris.y += 1
                if event.key == pygame.K_RIGHT:
                    self.boris.x += 1
                if event.key == pygame.K_LEFT:
                    self.boris.x -= 1
        if self.t <= 500:
            self.a = pygame.image.load("foto/bridge.png").convert_alpha()
            self.a = pygame.transform.scale(self.a, (25, 25))
            self.b = pygame.image.load("foto/borisbridge.png").convert_alpha()
            self.b = pygame.transform.scale(self.b, (25, 25))
            self.t += 1
        else:
            self.a = pygame.image.load("foto/sea25.png").convert_alpha()
            self.b = pygame.image.load("foto/borissea.png").convert_alpha()
        object.borisco = [object.boris.x, object.boris.y]
        screen.fill((54, 121, 236))
        screen.blit(achtergrond, (0, 0))
        object.draw_elements()
