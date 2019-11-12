from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (30.0 / 0.1)  # 30 pixel 10 cm
RUN_SPEED_KMPH = 4.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# 184 *168.6666
# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 /TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Bird:
    image = None

    def __init__(self, x=400, y=300, velocity=1):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.dir = 1
        self.frame = 0
        self.frame_x = 0
        self.frame_y = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame_x) * 182, int(self.frame_y) * 167, 182, 167, 0,
                                           '', self.x, self.y, 182, 167)
        else:
            self.image.clip_composite_draw(int(self.frame_x) * 182, int(self.frame_y) * 167, 182, 167, 0,
                                           'h', self.x, self.y, 182, 167)

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.frame_x = self.frame % 5
        self.frame_y = (15-self.frame) / 5
        if self.dir == 1:
            self.velocity = RUN_SPEED_PPS
        if self.dir == 2:
            self.velocity = -RUN_SPEED_PPS

        if self.x > 1500:
            self.dir = 2
        if self.x < 100:
            self.dir = 1
