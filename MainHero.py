from Creature import *


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
