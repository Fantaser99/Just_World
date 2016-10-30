import pygame

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
