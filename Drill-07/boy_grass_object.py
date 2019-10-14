from pico2d import *
import random
# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
class Grass:
    def __init__(self):
        self.image = load_image('grass.png');

    def draw(self):
        self.image.draw(400,30)
class Boy :
    def __init__(self):
        self.x,self.y = random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame+1)%8
        self.x +=5
    def draw(self):
        self.image.clip_draw(self.frame*100 ,0,100,100,self.x,self.y)

class Ball:
    def __init__(self):
        self.x,self.y = random.randint(50,750),599
        self.image_small_ball = load_image('ball21x21.png')
        self.move_speed =  random.randint(3,12)
        self.image_big_ball = load_image('ball41x41.png')
        self.shape = random.randint(1,2)

    def update(self):
        if self.shape ==1 :
            if self.y <=70:
                self.y = 70
            else:
                self.y -= self.move_speed
        else:
            if self.y <=65:
                self.y =65
            else:
                self.y -= self.move_speed
    def draw(self):
        if(self.shape==1):
          self.image_big_ball.draw(self.x,self.y)
        else:
          self.image_small_ball.draw(self.x,self.y)

# initialization code
open_canvas()
boy = Boy()
grass = Grass()
ball = Ball()
team = [Boy() for i in range(11)]
running = True
Balls = [Ball() for i in range(20)]
# game main loop code
while running:
    handle_events() # 플레이어
    for boy in team:
        boy.update()
    for ball in Balls:
        ball.update()
    clear_canvas()
    for boy in team:
        boy.draw()
    for ball in Balls:
        ball.draw()

    grass.draw()
    update_canvas()

    delay(0.05)

# finalization code
close_canvas()
