from MainHero import *


class Game(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.pressed_arrows = ['still']

    def infinity_loop(self, hero):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                press_arrows(event, hero, self.pressed_arrows)
            elif event.type == pygame.KEYUP:
                release_arrows(event, hero, self.pressed_arrows)
        self.draw_map(True)
        self.move_hero(hero)
        self.screen_update()

    def draw_map(self, with_grid=False):
        self.screen.fill(BASE_SCREEN_BG)
        if with_grid:
            self.draw_grid()

    def move_hero(self, hero):
        hero.moving()
        self.screen.blit(hero.current_image, hero.rect)

    @staticmethod
    def screen_update():
        pygame.display.flip()
        pygame.display.update()
        pygame.time.wait(ONE_TICK)

    def draw_grid(self):
        x_step, y_step = WIDTH // COUNT_X, HEIGHT // COUNT_Y
        for i in range(x_step, WIDTH, x_step):
            pygame.draw.line(self.screen, GRAY, [i, 0], [i, HEIGHT])
        for i in range(y_step, HEIGHT, y_step):
            pygame.draw.line(self.screen, GRAY, [0, i], [WIDTH, i])
