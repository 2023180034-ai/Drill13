import game_framework
from pico2d import *

image = None


def init():
    global image
    game_framework.stack[-2].boy.clear_movement_input()
    image = load_image('item_select.png')


def finish():
    global image
    del image


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type == SDL_KEYDOWN and
              event.key in (SDLK_ESCAPE, SDLK_i)):
            game_framework.pop_mode()
        elif (event.type == SDL_KEYDOWN and
              event.key in (SDLK_0, SDLK_1, SDLK_2)):
            boy = game_framework.stack[-2].boy
            if event.key == SDLK_0:
                boy.ball_size = None
            elif event.key == SDLK_1:
                boy.ball_size = 21
            elif event.key == SDLK_2:
                boy.ball_size = 41
            game_framework.pop_mode()


def update():
    game_framework.stack[-2].update()


def render():
    game_framework.stack[-2].render_scene()
    image.draw(400, 390, 480, 380)
    update_canvas()
