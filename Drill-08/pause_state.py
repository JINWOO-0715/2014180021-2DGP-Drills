from pico2d import *

import game_framework
import main_state


name = "pause_state"
image = None
count = 0

def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()



def draw():
    global count
    if count%10 <=5:
        image.clip_draw(200, 200, 500, 500, 400, 300, 200, 200)
    else:
        pass
    count += 1
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






