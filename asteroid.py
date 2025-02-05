import pygame
import circleshape
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        split_angle_1 = self.velocity.rotate(new_angle)
        split_angle_2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius).velocity = split_angle_1 * 1.2
        Asteroid(self.position.x, self.position.y, new_radius).velocity = split_angle_2 * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
