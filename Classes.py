import pygame

CREATURE_COORD_X = 200
CREATURE_COORD_Y = 100

# hp, speed, danger level, damage, armor
bestiary = {
    'dummy': [5, 0, 0, 0, 0]
}

# forward, (left, backward, right)
images = {
    'dummy': ['dummy.png']
}


class Creature:
    def __init__(self, creature='dummy', coordinates=[CREATURE_COORD_X, CREATURE_COORD_Y], direction='forward'):
        self.max_health_points = bestiary[creature][0]
        self.health_points = self.max_health_points
        self.move_speed = bestiary[creature][1]
        self.danger_level = bestiary[creature][2]
        self.attack_strength = bestiary[creature][3]
        self.damage_resist = bestiary[creature][4]
        self.forward_image = pygame.image.load(images[creature][0])
        if coordinates[0] < 0 or coordinates[1] < 0:
            print 'In class Creature:'
            print 'Negative coordinates do not have to be used.', coordinates
            coordinates = [CREATURE_COORD_X, CREATURE_COORD_Y]
            print 'Coordinates are', coordinates
            # if
        self.coordinates = coordinates
        self.direction = direction
        self.home_location = [[0, 0], [1, 1]]

    def moving(self, coordinates=[0, 0]):
        raise NotImplementedError('class Creature def moving')

    def deal_damage(self):
        raise NotImplementedError('class Creature def deal_damage')

    def take_damage(self):
        raise NotImplementedError('class Creature def take_damage')

    def __del__(self):
        # here's just nothing to do now
        pass


def init_screen(height=600, width=800):
    pygame.init()
    size = [width, height]
    return pygame.display.set_mode(size)


def main():
        test = Creature(coordinates=[200, -300])
        screen = init_screen()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            screen.fill([0, 0, 0])
            screen.blit(test.forward_image, test.coordinates)
            pygame.display.update()
            pygame.time.delay(100)

try:
    main()
except NotImplementedError as error:
    print 'Oops! You used not finished function in', error.args
