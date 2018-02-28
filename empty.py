import random
from pygame import Surface

WIDTH = 300
HEIGHT = 600

BLACK = (0, 0, 0)
snow_color = (255, 255, 255)
snow_particles = []
settled = Surface((WIDTH, HEIGHT))

logo = Actor('python', center=(WIDTH / 2, HEIGHT / 2))
settled.blit(images.python, logo.topleft)


def update():
    pixels = []
    for x, y in snow_particles:
        if y+1 > HEIGHT:
            continue
        if y+1 == HEIGHT or settled.get_at((x, y+1)) != BLACK:
            settled.set_at((x,y), snow_color)
        else:
            pixels.append((x, y+1))
    snow_particles[:] = pixels

def create_particle():
    x = random.randrange(0, WIDTH)
    y = 0
    snow_particles.append((x, y))

def draw():
    screen.blit(settled, (0, 0))
    for part in snow_particles:
        screen.surface.set_at(part, snow_color)

clock.schedule_interval(create_particle, .05)
