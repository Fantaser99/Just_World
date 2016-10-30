from constants import *
from glossary import *


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


def init_screen(width=WIDTH, height=HEIGHT):
    pygame.init()
    size = [width, height]
    return pygame.display.set_mode(size)
