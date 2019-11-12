from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.03)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 2  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# 184 *168.6666
# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 14


class Bird:
    image = None

    def __init__(self, x=400, y=300, velocity=1):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.dir = 1
        self.frame = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw((int(self.frame) % 5) * 182, (int((15 - self.frame) / 5)) * 167, 182, 167, 0,
                                           '', self.x, self.y, 182, 167)
        else:
            self.image.clip_composite_draw((int(self.frame) % 5) * 182, (int((15 - self.frame) / 5)) * 167, 182, 167, 0,
                                           'h', self.x, self.y, 182, 167)

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        if self.dir == 1:
            self.velocity = RUN_SPEED_PPS
        if self.dir == 2:
            self.velocity = -RUN_SPEED_PPS

        if self.x > 1500:
            self.dir = 2
        if self.x < 100:
            self.dir = 1
