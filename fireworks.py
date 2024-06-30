import pygame
import random
import math

N_PARTICLES = 10000
EXPLOSION_SIZE_MIN = 50
EXPLOSION_SIZE_MAX = 700
particles = []




def project(x: float, screen_width: int) -> int:
    """Projects a float in the range [0, 1] to the screen width."""
    return int(x * screen_width)

class Particle:
    def __init__(self, x: float, y: float, dx: float, dy: float, color, size):
        """Initializes a particle with position, velocity, color, and size.
        All x, y, dx, dy, and size are floats."""
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.size = size

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += 0.0005
        self.dx *= 0.999

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, 
                           (project(self.x, width/aspect), project(self.y, height)), 
                           self.size)


def resurrect_for_fireworks():
    """This function resurrects particles for fireworks. It picks fireworks that are below the screen and moves
    them close to where the fireworks are launched."""
    explosion_size = random.randint(EXPLOSION_SIZE_MIN, EXPLOSION_SIZE_MAX)
    explosion_center_x = random.uniform(0.0, aspect)
    explosion_center_y = random.uniform(0.0, 1.0)
    for particle in particles:
        """Note that particles x,y,dx and dy are floats."""
        if particle.y > 1.0: # or particle.x < 0.0 or particle.x > 1.0:
            angle = random.uniform(0, 2 * 3.14159)
            distance = random.uniform(0, 0.01)
            particle.x = explosion_center_x + distance * math.cos(angle) 
            particle.y = explosion_center_y + distance * math.sin(angle)
            launch_angle = random.uniform(0, 2 * 3.14159)
            launch_speed = random.uniform(0.0, 1.0/60)
            particle.dx = launch_speed * math.cos(launch_angle)
            particle.dy = launch_speed * math.sin(launch_angle)
            particle.size = random.randint(1, 5)
            explosion_size -= 1
            if explosion_size == 0:
                return



def init():
    for i in range(N_PARTICLES):
        yellow = random.randint(0, 255)
        particles.append(Particle(2.0, 1.1, 0, 0, pygame.Color(random.randint(0, 255),
                                                           random.randint(0, 255),
                                                           random.randint(0, 255)) , 0))

def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    global width, height, aspect
    width = screen.get_width()
    height = screen.get_height()
    aspect = width / height
    clock = pygame.time.Clock()
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        for particle in particles:
            particle.move()
            particle.draw(screen)
        # Resurrect particles to be part of a new firework
        if random.random() < 0.05:
            resurrect_for_fireworks()
        clock.tick_busy_loop(60)
        pygame.display.flip()
        


if __name__ == "__main__":
    main()