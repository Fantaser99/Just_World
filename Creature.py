from glossary import *
from Item import *
import pygame


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
