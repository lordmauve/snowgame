import random
from pygame import Surface
from pygame.draw import line

WIDTH = 350
HEIGHT = 200
BOTTOM_COLOUR = (255,0,0)
BLACK = (0, 0, 0)
snow_color = (255, 255, 255)
snow_particles = []
settled = Surface((WIDTH, HEIGHT))

logo = Actor('python', center=(WIDTH / 2, HEIGHT / 2))
settled.blit(images.python, logo.topleft)

line(settled, BOTTOM_COLOUR, (0, HEIGHT - 1), (WIDTH / 2 - 10, HEIGHT - 1))
line(settled, BOTTOM_COLOUR, (WIDTH, HEIGHT - 1), (WIDTH / 2 + 10, HEIGHT - 1))

def update():
    pixels = []
    for x, y in snow_particles:
        nexty = y+1
        if nexty > HEIGHT:
            continue
        if nexty == HEIGHT:
            settled.set_at((x,y), snow_color)
        elif settled.get_at((x, nexty)) != BLACK:
            left = x - 1
            right = x + 1
            drift = [(left, nexty), (right, nexty)]
            valid_drift = []
            for new_x, new_y in drift:
                if 0 <= new_x < WIDTH:
                    if settled.get_at((new_x, new_y)) == BLACK:
                        valid_drift.append((new_x, new_y))
            if not valid_drift:
                settled.set_at((x,y), snow_color)
            else:
                pixels.append(random.choice(valid_drift))
        else:
            pixels.append((x, nexty))
    snow_particles[:] = pixels

def create_particle():
    x = random.randrange(0, WIDTH)
    y = 0
    snow_particles.append((x, y))

def draw():
    screen.blit(settled, (0, 0))
    for part in snow_particles:
        screen.surface.set_at(part, snow_color)

clock.schedule_interval(create_particle, .01)
