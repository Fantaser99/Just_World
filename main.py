from Game import *


def main():
    just_world = Game()
    hero = MainHero(creature='lil_hero', coordinates=BASE_HERO_COORDINATES)
    while True:
        just_world.infinity_loop(hero)


try:
    main()
except NotImplementedError as error:
    print 'Oops! You caught some bug:', error.args
