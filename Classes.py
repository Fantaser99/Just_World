import pygame

BASE_HERO_COORDINATES = [300, 200]
BASE_X, BASE_Y = 0, 1
ONE_TICK = 60
CREATURE_COORD = CREATURE_COORD_X, CREATURE_COORD_Y = 200, 100
HERO_BASE_COORD = HERO_COORD_X, HERO_COORD_Y = 300, 100
CREATURE_HOME = FIRST_HOME_COORD, SECOND_HOME_COORD = [0, 0], [300, 200]
SCREEN_SIZE = WIDTH, HEIGHT = 800, 600
SCREEN_CELL = COUNT_X, COUNT_Y = 16, 12
BASE_SCREEN_BG = [255, 255, 255]
BLACK = [0, 0, 0]
GRAY = [180, 180, 180]

BEAST_HP, BEAST_SPEED, BEAST_DANGER, BEAST_DAMAGE, BEAST_ARMOR = 0, 1, 2, 3, 4
bestiary = {
    'dummy': [5, 2, 0, 0, 0],
    'lil_hero': [7, 6, 1, 2, 2]
}

items = {
    0: {"name": "Nothing", "icon": None, "weight": 0, "cost": 0, "description": "Empty", "item_id": 0},
}

IMG_LEFT, IMG_RIGHT, IMG_UP, ING_DOWN = 0, 1, 2, 3
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
    elif rect.right > screen[BASE_X]:
        rect.right = screen[BASE_X]
    if rect.top < 0:
        rect.top = 0
    elif rect.bottom > screen[BASE_Y]:
        rect.bottom = screen[BASE_Y]
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


class Creature:
    def __init__(self, creature='dummy', coordinates=CREATURE_COORD,
                 # move it to Beast:
                 # home_location=CREATURE_HOME,
                 direction='forward'):
        self.max_health_points = bestiary[creature][BEAST_HP]
        self.health_points = self.max_health_points
        self.move_speed = bestiary[creature][BEAST_SPEED]
        self.danger_level = bestiary[creature][BEAST_DANGER]
        self.attack_strength = bestiary[creature][BEAST_DAMAGE]
        self.damage_resist = bestiary[creature][BEAST_ARMOR]
        self.image = {
            'left': pygame.image.load(images[creature][IMG_LEFT]),
            'right': pygame.image.load(images[creature][IMG_RIGHT])
        }
        self.current_image = self.image['left']
        self.rect = self.image['left'].get_rect()
        self.state = 'still'
        if coordinates[BASE_X] < 0 or coordinates[BASE_Y] < 0:
            print 'In class Creature __init__():'
            print 'Negative coordinates of creature do not have to be used.', coordinates
            self.coordinates = [CREATURE_COORD_X, CREATURE_COORD_Y]
            print 'Coordinates are', self.coordinates
        else:
            self.coordinates = coordinates
        self.direction = direction
        # move it to Beast:
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


class Item:
    __free_item_id__ = 1

    @staticmethod
    def __get_new_item_id__():
        Item.__free_item_id__ += 1
        return Item.__free_item_id__ - 1

    def __init__(self, identifier, coords):  # int identifier, (int, int) coords.
        if identifier not in items.keys():
            raise ValueError('Id ' + str(identifier) + 'not found!')
        self.info = items[int(identifier)]
        self.on_ground = True
        self._id_ = identifier
        self.item_id = self.__get_new_item_id__()
        self.x = coords[BASE_X]
        self.y = coords[BASE_Y]
        # del self.getNewItemId  # this function shouldn't be in this class's objects.

    def get_item_id(self):
        return self._id_

    def get_id(self):
        return self.item_id

    def is_on_ground(self):
        return self.on_ground

    def get_icon(self):
        return self.info["icon"]

    def get_coords(self):
        # If item is in inventory, func returns inventory coords. Else it returns world-related coords.
        return {"on ground": self.is_on_ground(), "x": self.x, "y": self.y}

    def get_weight(self):
        return self.info["weight"]

    def get_cost(self):
        return self.info["cost"]

    def get_description(self):
        return self.info["description"]

    def get_time_left(self):
        if True:
            raise NotImplementedError('Class Item, method getTimeLeft. Method moveToGround is required.')
        if self.on_ground:
            if self.start + self.duration <= game_time:  # Time must be global.
                pass  # Here should be deletion of item.
            return self.start + self.duration - game_time
        else:
            return None

    def get_info(self):
        # This func isn't cool, it can work longer than other.
        info = self.info
        info["on_ground"] = self.is_on_ground()
        info["id"] = self.getId()
        info["coords"] = (self.x, self.y)
        return info

    def move_to_inventory(self):
        # Here should be choice of coord in player' inventory.
        # Will be realized after realization of Player class.
        raise NotImplementedError('Class Item, method move_to_inventory')

    def move_to_ground(self):
        # Here should be choice of coords based on player' coords and start of item's duration timer.
        # Will be realized after realization of Player class.
        raise NotImplementedError('Class Item, method move_to_ground')

    def move_in_inventory(self, x, y):
        # Here should be coords check and changing coords of item in Player's inventory too.
        if True:
            raise NotImplementedError('Class Item, method move_in_inventory')
        self.coords = (self.coords[BASE_X] + x, self.coords[BASE_Y] + y)


def init_screen(width=WIDTH, height=HEIGHT):
    pygame.init()
    size = [width, height]
    return pygame.display.set_mode(size)


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

    # need optimization
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
    hero = MainHero(creature='lil_hero', coordinates=BASE_HERO_COORDINATES)
    while True:
        just_world.infinity_loop(hero)


try:
    main()
except NotImplementedError as error:
    print 'Oops! You caught some bug:', error.args
