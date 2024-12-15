import pygame

pygame.init()

# Constants
WIDTH = 1600
HEIGHT = 800
FPS = 60
GRAVITY = 9.81 #Earth gravity
TIME_STEP = 1 / (GRAVITY / 2) # My custom formula

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Particle:
    def __init__(self, x, y, mass, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color
        self.vx = 0
        self.vy = 0

    def update(self):
        self.vy += GRAVITY * TIME_STEP

        self.x += self.vx * TIME_STEP
        self.y += self.vy * TIME_STEP

        # Check for bottom collision
        if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            damping = 0.8 / (self.mass / 10)
            self.vy = -self.vy * damping

        # Check for top collision
        elif self.y - self.radius < 0:
            self.y = self.radius
            self.vy = -self.vy * 0.8

        # Check for right collision
        if self.x + self.radius > WIDTH:
            self.x = WIDTH - self.radius
            damping = 0.8 / (self.mass / 10)
            self.vx = -self.vx * damping

        # Check for left collision
        elif self.x - self.radius < 0:
            self.x = self.radius
            self.vx = -self.vx * 0.8

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particles")

                   # x, y, mass, radius, color
particle = Particle(800, 400, 10, 30, RED)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: #Arrow up
                particle.vy -= 25
            if event.key == pygame.K_DOWN: #Arrow down
                particle.vy += 25
            if event.key == pygame.K_RIGHT: #Arrow right
                particle.vx += 25
            if event.key == pygame.K_LEFT: #Arrow left
                particle.vx -= 25
            if event.key == pygame.K_r: #'R' key
                particle.vx = 0
                particle.vy = 0
            if event.key == pygame.K_w: #'W' key
                particle.vy -= 250
            if event.key == pygame.K_s: #'S' key
                particle.vy += 250
            if event.key == pygame.K_d: #'D' key
                particle.vx += 250
            if event.key == pygame.K_a: #'A' key
                particle.vx -= 250

    screen.fill(WHITE) #Background color

    particle.update()
    particle.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()