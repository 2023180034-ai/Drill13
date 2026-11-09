import game_framework
from pico2d import *

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.pop_mode()


def update():
    pass


def render():
    game_framework.stack[-2].render_scene()
    image.draw(400, 390, 480, 380)
    update_canvas()
