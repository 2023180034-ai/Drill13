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
        elif (event.type in (SDL_KEYDOWN, SDL_KEYUP) and
              event.key in (SDLK_LEFT, SDLK_RIGHT)):
            game_framework.stack[-2].boy.handle_event(event)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.pop_mode()


def update():
    game_framework.stack[-2].update()


def render():
    game_framework.stack[-2].render_scene()
    image.draw(400, 390, 480, 380)
    update_canvas()
