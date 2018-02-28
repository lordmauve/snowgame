import random

WIDTH = 300
snow_particles = []

def update():
    pixels = []
    for x, y in snow_particles:
        pixels.append((x, y+1))
    snow_particles[:] = pixels

def create_particle():
    x = random.randint(0, WIDTH)
    y = 0
    snow_particles.append((x, y))

def draw():
    screen.fill('blue')
    for part in snow_particles:
        screen.surface.set_at(part, (255, 255, 255))

clock.schedule_interval(create_particle, .05)
