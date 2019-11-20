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
        self.sign = False

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if main_state.collide(main_state.zombie,self):
            main_state.zombie.hp +=100
            game_world.remove_object(self)
            self.sign =False
        if main_state.collide(main_state.boy,self):
            main_state.boy.hp +=100
            game_world.remove_object(self)
            self.sign = False

        pass

    def stop(self):
        self.fall_speed = 0



    def collide(a, b):
        # fill here
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

        return True



