from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024



def mouse_handle_events():
    global running
    global mx,my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
           running = False
        elif event.type == SDL_MOUSEMOTION:
              mx, my = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
              running = False

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mx, my = KPU_WIDTH // 2, KPU_HEIGHT // 2
x2, y2 = KPU_WIDTH // 2, KPU_HEIGHT // 2

show_cursor()
size =999
p1 = [(random.randint(-500, 500) ) for i in range(size)]
p2 = [(random.randint(-500, 500)) for i in range(size)]

while True:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.clip_draw(0,0,50,50,mx,my)
    update_canvas()
    mouse_handle_events()
    p1[0] = (mx,my)
    p2[0] = (mx,my)
    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]
        character.clip_draw(100, 100 * 1, 100, 100, x, y)
        update_canvas()


close_canvas()



