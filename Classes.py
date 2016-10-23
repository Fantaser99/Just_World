import pygame

CREATURE_COORD = CREATURE_COORD_X, CREATURE_COORD_Y = 200, 100
HERO_BASE_COORD = HERO_COORD_X, HERO_COORD_Y = 300, 100
CREATURE_HOME = FIRST_HOME_COORD, SECOND_HOME_COORD = [0, 0], [300, 200]
SCREEN_SIZE = WIDTH, HEIGHT = 800, 600
BASE_SCREEN_BG = [255, 255, 255]

# hp, speed, danger level, damage, armor
bestiary = {
    'dummy': [5, 2, 0, 0, 0],
    'lil_hero': [7, 6, 1, 2, 2]
}

# left, right, (forward, backward)
images = {
    'dummy': ['dummy_left.png', 'dummy_right.png'],
    'lil_hero': ['lil_hero_left.png', 'lil_hero_right.png']
}

arrows = {
    'up': pygame.K_UP,
    'down': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT
}


def press_arrows(event, hero, pressed_arrows):
    for direction in arrows:
        if event.key == arrows[direction]:
            hero.state_edit(direction)
            pressed_arrows.append(direction)


def release_arrows(event, hero, pressed_arrows):
    for direction in arrows:
        if event.key == arrows[direction]:
            pressed_arrows.remove(direction)
            hero.state_edit(pressed_arrows[len(pressed_arrows) - 1])


def base_move_correction(rect, screen=SCREEN_SIZE):
    if rect.left < 0:
        rect.left = 0
    elif rect.right > screen[0]:
        rect.right = screen[0]
    if rect.top < 0:
        rect.top = 0
    elif rect.bottom > screen[1]:
        rect.bottom = screen[1]
    return rect


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
        hero.moving()
        self.screen.fill(BASE_SCREEN_BG)
        self.screen.blit(hero.current_image, hero.rect)
        pygame.display.flip()
        pygame.display.update()
        pygame.time.wait(80)


class Creature:
    def __init__(self, creature='dummy', coordinates=CREATURE_COORD,
                 # move it somewhere else:
                 # home_location=CREATURE_HOME,
                 direction='forward'):
        self.max_health_points = bestiary[creature][0]
        self.health_points = self.max_health_points
        self.move_speed = bestiary[creature][1]
        self.danger_level = bestiary[creature][2]
        self.attack_strength = bestiary[creature][3]
        self.damage_resist = bestiary[creature][4]
        self.image = {
            'left': pygame.image.load(images[creature][0]),
            'right': pygame.image.load(images[creature][1])
        }
        self.current_image = self.image['left']
        self.rect = self.image['left'].get_rect()
        self.state = 'still'
        if coordinates[0] < 0 or coordinates[1] < 0:
            print 'In class Creature __init__():'
            print 'Negative coordinates of creature do not have to be used.', coordinates
            self.coordinates = [CREATURE_COORD_X, CREATURE_COORD_Y]
            print 'Coordinates are', self.coordinates
        else:
            self.coordinates = coordinates
        self.direction = direction
        # move it somewhere else:
        # if home_location[0][0] < 0 or home_location[0][1] < 0 or home_location[1][0] < 0 or home_location[1][1] < 0:
        #     print 'In class Creature __init__():'
        #     print 'Negative coordinates of home location do not have to be used.', home_location
        #     self.home_location = CREATURE_HOME
        #     print 'Coordinates are', self.home_location

    def deal_damage(self):
        raise NotImplementedError('class Creature def deal_damage')

    def take_damage(self):
        raise NotImplementedError('class Creature def take_damage')

    def __del__(self):
        # here's just nothing to do now
        pass


class MainHero(Creature):

    def __init__(self, creature='lil_hero', coordinates=HERO_BASE_COORD, direction='forward'):
        Creature.__init__(self, creature=creature, coordinates=coordinates, direction=direction)

    def state_edit(self, direction='not_chosen'):
        if direction in ('left', 'right', 'up', 'down', 'still'):
            self.state = direction
        else:
            print 'In class Creature state_edit():'
            print 'Wrong parameter name', direction
            print 'Creature will not move.'
            self.state = 'still'

    def moving(self):
        move_shift = [0, 0]
        if self.state == 'right':
            move_shift = [self.move_speed, 0]
            self.current_image = self.image['right']
        elif self.state == 'left':
            move_shift = [-self.move_speed, 0]
            self.current_image = self.image['left']
        elif self.state == 'down':
            move_shift = [0, self.move_speed]
        elif self.state == 'up':
            move_shift = [0, -self.move_speed]
        elif self.state == 'still':
            move_shift = [0, 0]
        if move_shift != [0, 0]:
            self.rect = self.rect.move(move_shift)
            self.rect = base_move_correction(self.rect)


def main():
        just_world = Game()
        hero = MainHero(creature='lil_hero', coordinates=[300, 200])
        while True:
            just_world.infinity_loop(hero)


try:
    main()
except NotImplementedError as error:
    print 'Oops! You used not finished function in', error.args
