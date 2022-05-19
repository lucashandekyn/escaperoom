import pygame, sys

# achtergrond moet nog aangepast worden guys
pygame.init()
cell_grootte = 64
cell_begin_x, cell_begin_y = (1216 - (6 * cell_grootte)) / 2, (
    500 - (7 * cell_grootte)
) / 2
cell_aantal_x, cell_aantal_y = 4, 5
# 1216,500
clock = pygame.time.Clock()
scherm = pygame.display.set_mode((1216, 500))


class Grid:
    def __init__(self):
        self.actief = [
            [1, 1],
            [1, 2],
            [2, 2],
            [3, 2],
            [4, 2],
            [4, 1],
            [1, 5],
            [1, 4],
            [2, 4],
            [3, 4],
            [4, 4],
            [4, 5],
        ]

    def draw_grid(self):
        for i in range(0, len(self.actief)):
            x_positie = int(self.actief[i][0] * cell_grootte + cell_begin_x)
            y_positie = int(self.actief[i][1] * cell_grootte + cell_begin_y)

            clearocean = pygame.image.load("foto/sea64.png")
            scherm.blit(clearocean, (x_positie, y_positie))

    def check_a(self):
        for i in range(1, 5):
            if [i, 1] in self.actief:
                self.actief.remove([i, 1])
            else:
                self.actief.insert(0, [i, 1])

    def check_b(self):
        for i in range(1, 5):
            if [i, 2] in self.actief:
                self.actief.remove([i, 2])
            else:
                self.actief.insert(0, [i, 2])

    def check_c(self):
        for i in range(1, 5):
            if [i, 3] in self.actief:
                self.actief.remove([i, 3])
            else:
                self.actief.insert(0, [i, 3])

    def check_d(self):
        for i in range(1, 5):
            if [i, 4] in self.actief:
                self.actief.remove([i, 4])
            else:
                self.actief.insert(0, [i, 4])

    def check_e(self):
        for i in range(1, 5):
            if [i, 5] in self.actief:
                self.actief.remove([i, 5])
            else:
                self.actief.insert(0, [i, 5])

    def check_1(self):
        for i in range(1, 6):
            if [1, i] in self.actief:
                self.actief.remove([1, i])
            else:
                self.actief.insert(0, [1, i])

    def check_2(self):
        for i in range(1, 6):
            if [2, i] in self.actief:
                self.actief.remove([2, i])
            else:
                self.actief.insert(0, [2, i])

    def check_3(self):
        for i in range(1, 6):
            if [3, i] in self.actief:
                self.actief.remove([3, i])
            else:
                self.actief.insert(0, [3, i])

    def check_4(self):
        for i in range(1, 6):
            if [4, i] in self.actief:
                self.actief.remove([4, i])
            else:
                self.actief.insert(0, [4, i])

    def check_RIGHT(self):
        for i in range(1, 5):
            if [i, 6 - i] in self.actief:
                self.actief.remove([i, 6 - i])
            else:
                self.actief.insert(0, [i, 6 - i])

    def check_DOWN(self):
        for i in range(1, 5):
            if [i, i] in self.actief:
                self.actief.remove([i, i])
            else:
                self.actief.insert(0, [i, i])

    def check_UP(self):
        for i in range(1, 5):
            if [i, 1 + i] in self.actief:
                self.actief.remove([i, 1 + i])
            else:
                self.actief.insert(0, [i, 1 + i])

    def check_LEFT(self):
        for i in range(1, 5):
            if [i, 5 - i] in self.actief:
                self.actief.remove([i, 5 - i])
            else:
                self.actief.insert(0, [i, 5 - i])

    def check_r(self):
        self.actief = [
            [1, 1],
            [1, 2],
            [2, 2],
            [3, 2],
            [4, 2],
            [4, 1],
            [1, 5],
            [1, 4],
            [2, 4],
            [3, 4],
            [4, 4],
            [4, 5],
        ]


class Main_grid:
    def __init__(self):
        self.grid = Grid()

    def update(self):
        self.grid.draw_grid()
        self.check_full_grid()

    def check_full_grid(self):
        x = 0
        for i in range(1, 5):
            if [i, 1] and [i, 2] and [i, 3] and [i, 4] and [i, 5] in self.grid.actief:
                x += 1
            else:
                x = 0
            if x == 4:
                return True

    def grid_while(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            achtergrond_gridpuzzel = pygame.image.load("foto/oilocean.png")
            scherm.blit(achtergrond_gridpuzzel, (0, 0))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.grid.check_a()
                elif event.key == pygame.K_b:
                    self.grid.check_b()
                elif event.key == pygame.K_c:
                    self.grid.check_c()
                elif event.key == pygame.K_d:
                    self.grid.check_d()
                elif event.key == pygame.K_e:
                    self.grid.check_e()
                elif event.key == pygame.K_1:
                    self.grid.check_1()
                elif event.key == pygame.K_2:
                    self.grid.check_2()
                elif event.key == pygame.K_3:
                    self.grid.check_3()
                elif event.key == pygame.K_4:
                    self.grid.check_4()
                elif event.key == pygame.K_UP:
                    self.grid.check_UP()
                elif event.key == pygame.K_DOWN:
                    self.grid.check_DOWN()
                elif event.key == pygame.K_LEFT:
                    self.grid.check_LEFT()
                elif event.key == pygame.K_RIGHT:
                    self.grid.check_RIGHT()
                elif event.key == pygame.K_r:
                    self.grid.check_r()
        self.update()
        pygame.display.update()
        clock.tick(60)
