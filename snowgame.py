import pgzrun
import random
from pygame import Surface
from pygame.draw import line

WIDTH = 350
HEIGHT = 200
BOTTOM_COLOUR = (255,0,0)
BLACK = (0, 0, 0)
drag_start = None
current_mouse = None

scorel = 0
scorer = 0
snow_color = (255, 255, 255)
guide_line = (0, 255, 0)
snow_particles = []
settled = Surface((WIDTH, HEIGHT))


logo = Actor('python', center=(WIDTH / 2, HEIGHT / 2))
settled.blit(images.python, logo.topleft)

line(settled, BOTTOM_COLOUR, (0, HEIGHT - 1), (WIDTH / 4 - 10, HEIGHT - 1))
line(settled, BOTTOM_COLOUR, (3* WIDTH / 4 - 10, HEIGHT - 1), (WIDTH / 4 + 10, HEIGHT - 1))
line(settled, BOTTOM_COLOUR, (WIDTH, HEIGHT - 1), (3* WIDTH / 4 + 10, HEIGHT - 1))

def update():
    global scorel, scorer
    pixels = []
    for x, y in snow_particles:
        nexty = y+1
        if nexty >= HEIGHT:
            if x > WIDTH // 2:
                scorer += 1
            else:
                scorel += 1
            continue
        # if nexty == HEIGHT:
            # settled.set_at((x,y), snow_color)
        elif settled.get_at((x, nexty)) != BLACK:
            left = x - 1
            right = x + 1
            drift = [(left, nexty), (right, nexty)]
            valid_drift = []
            for new_x, new_y in drift:
                if 0 <= new_x < WIDTH:
                    if settled.get_at((new_x, new_y)) == BLACK and \
                            settled.get_at((new_x, y)) == BLACK:
                        valid_drift.append((new_x, new_y))
            if not valid_drift:
                settled.set_at((x,y), snow_color)
            else:
                pixels.append(random.choice(valid_drift))
        else:
            pixels.append((x, nexty))
    snow_particles[:] = pixels

def on_mouse_down(pos):
    global drag_start
    drag_start = pos

def on_mouse_up(pos):
    global drag_start
    line(settled, BOTTOM_COLOUR, drag_start, pos)
    drag_start = None
    current_mouse = None

def on_mouse_move(pos, rel, buttons):
    global current_mouse
    current_mouse = pos


def create_particle():
    x = random.randrange(0, WIDTH)
    y = 0
    snow_particles.append((x, y))

def draw():
    screen.blit(settled, (0, 0))
    for part in snow_particles:
        screen.surface.set_at(part, snow_color)

    if drag_start:
        line(screen.surface, guide_line, drag_start, current_mouse)

    screen.draw.text(str(scorel), (10, 10), color="orange")
    screen.draw.text(str(scorer), topright = (WIDTH - 10, 10), color="orange")

clock.schedule_interval(create_particle, .01)

pgzrun.go()
