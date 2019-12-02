from pico2d import *
import game_world
import game_framework
import random
import main_state

class Ball:
    image = None

    def __init__(self):

        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = random.randint(20, 1837 - 20)
        self.y = random.randint(20, 1109 - 20)

    def draw(self):
        cx, cy = self.x - main_state.boy.bg.window_left, self.y - main_state.boy.bg.window_bottom
        self.image.clip_draw(0, 0, 21, 21, cx, cy)

    def update(self):
        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2
