import game_framework
from pico2d import *


class Block:
    def __init__(self):
        self.x, self.y = 800, 170
        self.image = load_image('brick180x40.png')
        self.velocity = 1
        self.dir = 1

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def update(self):
        if self.x < 90:
            self.dir = 1
        elif self.x > 1600 - 90:
            self.dir = -1
        self.x += self.dir * self.velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
