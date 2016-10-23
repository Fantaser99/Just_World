import pygame

CREATURE_COORD = CREATURE_COORD_X, CREATURE_COORD_Y = 200, 100
CREATURE_HOME = FIRST_HOME_COORD, SECOND_HOME_COORD = [0, 0], [300, 200]
SCREEN_SIZE = WIDTH, HEIGHT = 800, 600

# hp, speed, danger level, damage, armor
bestiary = {
    'dummy': [5, 5, 0, 0, 0]
}

# forward, (left, backward, right)
images = {
    'dummy': ['dummy.png']
}


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


class Creature:
    def __init__(self, creature='dummy', coordinates=CREATURE_COORD,
                 home_location=CREATURE_HOME, direction='forward'):
        self.max_health_points = bestiary[creature][0]
        self.health_points = self.max_health_points
        self.move_speed = bestiary[creature][1]
        self.danger_level = bestiary[creature][2]
        self.attack_strength = bestiary[creature][3]
        self.damage_resist = bestiary[creature][4]
        self.forward_image = pygame.image.load(images[creature][0])
        self.forward_rect = self.forward_image.get_rect()
        self.state = 'still'
        if coordinates[0] < 0 or coordinates[1] < 0:
            print 'In class Creature __init__():'
            print 'Negative coordinates of creature do not have to be used.', coordinates
            self.coordinates = [CREATURE_COORD_X, CREATURE_COORD_Y]
            print 'Coordinates are', self.coordinates
        self.direction = direction
        if home_location[0][0] < 0 or home_location[0][1] < 0 or home_location[1][0] < 0 or home_location[1][1] < 0:
            print 'In class Creature __init__():'
            print 'Negative coordinates of home location do not have to be used.', home_location
            self.home_location = CREATURE_HOME
            print 'Coordinates are', self.home_location

    def state_edit(self, direction='not_chosen'):
        if direction in ('left', 'right', 'up', 'down'):
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
        elif self.state == 'left':
            move_shift = [-self.move_speed, 0]
        elif self.state == 'down':
            move_shift = [0, self.move_speed]
        elif self.state == 'up':
            move_shift = [0, -self.move_speed]
        elif self.state == 'still':
            move_shift = [0, 0]
        if move_shift != [0, 0]:
            self.forward_rect = self.forward_rect.move(move_shift)
            self.forward_rect = base_move_correction(self.forward_rect)

    def deal_damage(self):
        raise NotImplementedError('class Creature def deal_damage')

    def take_damage(self):
        raise NotImplementedError('class Creature def take_damage')

    def __del__(self):
        # here's just nothing to do now
        pass


def main():
        pygame.init()
        test = Creature(coordinates=[300, 200])
        screen = pygame.display.set_mode(SCREEN_SIZE)
        pressed_arrows = ['still']
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        test.state_edit('up')
                        pressed_arrows.append('up')
                    if event.key == pygame.K_DOWN:
                        test.state_edit('down')
                        pressed_arrows.append('down')
                    if event.key == pygame.K_LEFT:
                        test.state_edit('left')
                        pressed_arrows.append('left')
                    if event.key == pygame.K_RIGHT:
                        test.state_edit('right')
                        pressed_arrows.append('right')
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        pressed_arrows.remove('up')
                        test.state_edit(pressed_arrows[len(pressed_arrows) - 1])
                    if event.key == pygame.K_DOWN:
                        pressed_arrows.remove('down')
                        test.state_edit(pressed_arrows[len(pressed_arrows) - 1])
                    if event.key == pygame.K_LEFT:
                        pressed_arrows.remove('left')
                        test.state_edit(pressed_arrows[len(pressed_arrows) - 1])
                    if event.key == pygame.K_RIGHT:
                        pressed_arrows.remove('right')
                        test.state_edit(pressed_arrows[len(pressed_arrows) - 1])
            test.moving()
            screen.fill([0, 0, 0])
            screen.blit(test.forward_image, test.forward_rect)
            pygame.display.flip()
            pygame.display.update()
            pygame.time.wait(40)

try:
    main()
except NotImplementedError as error:
    print 'Oops! You used not finished function in', error.args
