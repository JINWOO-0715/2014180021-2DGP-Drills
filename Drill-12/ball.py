import random
from pico2d import *
import game_world
import game_framework
import main_state
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = random.randint(40,900)
        self.y = random.randint(40, 1200)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def stop(self):
        self.fall_speed = 0






