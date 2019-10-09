import sys, logging, os, random, open_color, arcade

version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)




SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MARGIN = 30
SCREEN_TITLE = "Particle Exercise"

PARTICLE_MIN_SCALE = 0.01
PARTICLE_MAX_SCALE = 0.08
PARTICLE_MIN_X = -20
PARTICLE_MAX_X = 20
PARTICLE_VELOCITY_X = 0
PARTICLE_VELOCITY_Y = 4
PARTICLE_MIN_AX = -0.1
PARTICLE_MAX_AX = 0.1
PARTICLE_MIN_AY = -0.1
PARTICLE_MAX_AY = 0.1
PARTICLE_MIN_DECAY = 0.001
PARTICLE_MAX_DECAY = 0.01


class Particle(arcade.Sprite):
    def __init__(self, asset, scale, x, y, dx, dy, ax, ay, decay):
        super().__init__("assets/star_06.png".format(asset), scale)
        self.center_x = x
        self.center_y = y
        self.dx = dx
        self.dy = dy
        self.ax = ax
        self.ay = ay
        self.decay = decay
        self.color_pos = 0

        self.particle_colors = [
            (open_color.green_7, 4)
            ,(open_color.green_5, 5)
            ,(open_color.green_4, 6)
            ,(open_color.green_3, 7)
            ,(open_color.green_2, 8)
            ,(open_color.teal_1, 8)
            ,(open_color.teal_2, 7)
            ,(open_color.teal_3, 6)
            ,(open_color.teal_4, 5)
            ,(open_color.teal_5, 4)
        ]
        (self.color, self.lifetime) = self.particle_colors[self.color_pos]
        self.alive = True
        
    
    def update(self):
        self.dx += self.ax
        self.dy += self.ay
        self.center_x += self.dx
        self.center_y += self.dy
        self.scale -= self.decay
        if self.scale < self.decay:
            self.scale = self.decay
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.color_pos += 1
            if self.color_pos >= len(self.particle_colors):
                self.alive = False
            else:
                (self.color, self.lifetime) = self.particle_colors[self.color_pos]

class Particle2(arcade.Sprite):
    def __init__(self, asset, scale, x, y, ax, ay, decay):
        super().__init__("assets/spark_05.png".format(asset), scale)
        self.center_x = x
        self.center_y = y
        self.ax = ax
        self.ay = ay
        self.decay = decay
        self.color_pos = 0

        self.particle2_colors = [
            (open_color.indigo_9, 4)
        ]
        (self.color, self.lifetime) = self.particle2_colors[self.color_pos]
        self.alive = True
        
    
    def update(self):
        self.scale -= self.decay
        if self.scale < self.decay:
            self.scale = self.decay
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.color_pos += 1
            if self.color_pos >= len(self.particle2_colors):
                self.alive = False
            else:
                (self.color, self.lifetime) = self.particle2_colors[self.color_pos]

class Particle3(arcade.Sprite):
    def __init__(self, asset, scale, x, y, dx, dy, ax, ay, decay):
        super().__init__("assets/muzzle_02.png".format(asset), scale)
        self.center_x = x
        self.center_y = y
        self.dx = dx
        self.dy = dy
        self.ax = ax
        self.ay = ay
        self.decay = decay
        self.color_pos = 0

        self.particle3_colors = [
            (open_color.orange_5, 4)
            ,(open_color.green_5, 5)
            ,(open_color.blue_5, 6)
            ,(open_color.red_5, 7)
            ,(open_color.indigo_5, 8)
            ,(open_color.teal_1, 8)
            ,(open_color.teal_2, 7)
            ,(open_color.teal_3, 6)
            ,(open_color.teal_4, 5)
            ,(open_color.teal_5, 4)
        ]
        (self.color, self.lifetime) = self.particle3_colors[self.color_pos]
        self.alive = True
        
    
    def update(self):
        self.dx += self.ax
        self.dy += self.ay
        self.center_x += self.dx
        self.center_y += self.dy
        self.scale -= self.decay
        if self.scale < self.decay:
            self.scale = self.decay
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.color_pos += 1
            if self.color_pos >= len(self.particle3_colors):
                self.alive = False
            else:
                (self.color, self.lifetime) = self.particle3_colors[self.color_pos]
class Particle4(arcade.Sprite):
    def __init__(self, asset, scale, x, y, dx, dy, ax, ay, decay):
        super().__init__("assets/fire_01.png".format(asset), scale)
        self.center_x = x
        self.center_y = y
        self.dx = dx
        self.dy = dy
        self.ax = ax
        self.ay = ay
        self.decay = decay
        self.color_pos = 0

        self.particle4_colors = [
            (open_color.orange_5, 4)
            ,(open_color.orange_4, 5)
            ,(open_color.orange_6, 6)
            ,(open_color.orange_2, 7)
            ,(open_color.orange_1, 8)
            ,(open_color.teal_1, 8)
            ,(open_color.teal_2, 7)
            ,(open_color.teal_3, 6)
            ,(open_color.teal_4, 5)
            ,(open_color.teal_5, 4)
        ]
        (self.color, self.lifetime) = self.particle4_colors[self.color_pos]
        self.alive = True
        
    
    def update(self):
        self.dx += self.ax
        self.dy += self.ay
        self.center_x += self.dx
        self.center_y += self.dy
        self.scale -= self.decay
        if self.scale < self.decay:
            self.scale = self.decay
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.color_pos += 1
            if self.color_pos >= len(self.particle4_colors):
                self.alive = False
            else:
                (self.color, self.lifetime) = self.particle4_colors[self.color_pos] 


class Window(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.set_mouse_visible(True)

        arcade.set_background_color(open_color.black)

        self.particle_list = arcade.SpriteList()
        self.particle2_list=arcade.SpriteList()
        self.particle3_list=arcade.SpriteList()
        self.particle4_list=arcade.SpriteList()
        self.mouse_down = False
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2

    def setup(self):
        pass

    def update(self, delta_time):
        self.particle_list.update()
        self.particle2_list.update()
        self.particle3_list.update()
        self.particle4_list.update()
        if self.mouse_down:
            #generate a new particle
            x = self.x + random.uniform(PARTICLE_MIN_X, PARTICLE_MAX_X)
            y = self.y
            dx = PARTICLE_VELOCITY_X
            dy = PARTICLE_VELOCITY_Y
            ax = random.uniform(PARTICLE_MIN_AX,PARTICLE_MAX_AX)
            ay = random.uniform(PARTICLE_MIN_AY,PARTICLE_MAX_AY)
            decay = random.uniform(PARTICLE_MIN_DECAY,PARTICLE_MAX_DECAY)
            scale = random.uniform(PARTICLE_MIN_SCALE,PARTICLE_MAX_SCALE)
            #Particle(asset, sprite scale, initial position [x], initial position [y], velocity [x], velocity [y], acceleration [x], acceleration [y], scale decay)
            particle = Particle('circle_05',scale,x,y,dx,dy,ax,ay,decay)

            self.particle_list.append(particle)

        for p in self.particle_list:
            #if the particle is off the edge of the screen, kill it
            if p.center_x < -50 or p.center_x > SCREEN_WIDTH + 50 or p.center_y < -50 or p.center_y > SCREEN_HEIGHT + 50:
                p.kill()
            #if it has reached the end of its life
            if not p.alive:
                p.kill


    def on_draw(self):
        arcade.start_render()
        self.particle_list.draw()
        self.particle2_list.draw()
        self.particle3_list.draw()
        self.particle4_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        self.x = x
        self.y = y
        self.mouse_down = True
        px = random.uniform(50,750)
        py = 300
        ax = random.uniform(PARTICLE_MIN_AX,PARTICLE_MAX_AX)
        ay = random.uniform(PARTICLE_MIN_AY,PARTICLE_MAX_AY)
        decay = random.uniform(PARTICLE_MIN_DECAY,PARTICLE_MAX_DECAY)
        scale = 1.25
        particle = Particle2('circle_05',scale,px,py,ax,ay,decay)
        self.particle2_list.append(particle)
        for p in self.particle2_list:
            if p.center_x < -50 or p.center_x > SCREEN_WIDTH + 50 or p.center_y < -50 or p.center_y > SCREEN_HEIGHT + 50:
                p.kill()
            if not p.alive:
                p.kill

    def on_mouse_release(self, x, y, button, modifiers):
        self.x = x
        self.y = y
        self.mouse_down = False
        px = random.uniform(50,750)
        py = 580
        dx = -PARTICLE_VELOCITY_X
        dy = -PARTICLE_VELOCITY_Y
        ax = random.uniform(PARTICLE_MIN_AX,PARTICLE_MAX_AX)
        ay = random.uniform(PARTICLE_MIN_AY,PARTICLE_MAX_AY)
        decay = random.uniform(PARTICLE_MIN_DECAY,PARTICLE_MAX_DECAY)
        scale = 0.5
        particle = Particle3('circle_05',scale,px,py,dx,dy,ax,ay,decay)
        self.particle3_list.append(particle)
        for p in self.particle3_list:
            if p.center_x < -50 or p.center_x > SCREEN_WIDTH + 50 or p.center_y < -50 or p.center_y > SCREEN_HEIGHT + 50:
                p.kill()
            if not p.alive:
                p.kill

    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y
        px = self.x
        py = self.y
        dx = PARTICLE_VELOCITY_X
        dy = PARTICLE_VELOCITY_Y
        ax = random.uniform(PARTICLE_MIN_AX,PARTICLE_MAX_AX)
        ay = random.uniform(PARTICLE_MIN_AY,PARTICLE_MAX_AY)
        decay = random.uniform(PARTICLE_MIN_DECAY,PARTICLE_MAX_DECAY)
        scale = random.uniform(PARTICLE_MIN_SCALE,PARTICLE_MAX_SCALE)
        particle = Particle4('circle_05',scale,px,py,dx,dy,ax,ay,decay)
        self.particle4_list.append(particle)
        for p in self.particle4_list:
            if p.center_x < -50 or p.center_x > SCREEN_WIDTH + 50 or p.center_y < -50 or p.center_y > SCREEN_HEIGHT + 50:
                p.kill()
            if not p.alive:
                p.kill


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()