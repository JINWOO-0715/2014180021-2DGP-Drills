from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024



open_canvas(KPU_WIDTH,  KPU_HEIGHT)


# fill here
kpu_ground = load_image("KPU_GROUND.png")
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

size =10
points = [(random.randint(0,800),random.randint(0,800)) for i in range(size)]
clear_canvas()
kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

for j in range(size):
    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * points[j%size][0] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[(j+1)%size][0] + (-3 * t ** 3 + 4 * t ** 2 + t) * points[(j+2)%size][0] + (t ** 3 - t ** 2) * points[(j+3)%size][0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * points[j%size][1] + (3 * t ** 3 - 5 * t ** 2 + 2) * points[(j+1)%size][1] + (-3 * t ** 3 + 4 * t ** 2 + t) * points[(j+2)%size][1] + (t ** 3 - t ** 2) * points[(j+3)%size][1]) / 2
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()








