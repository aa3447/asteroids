import pygame
import circleshape
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius, score=100):
        super().__init__(x, y, radius)
        self.score = score

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return self.score
        new_angle = random.uniform(20, 50)
        split_angle_1 = self.velocity.rotate(new_angle)
        split_angle_2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        new_score = self.score * 2
        Asteroid(self.position.x, self.position.y, new_radius, new_score).velocity = split_angle_1 * 1.2
        Asteroid(self.position.x, self.position.y, new_radius, new_score).velocity = split_angle_2 * 1.2
        return self.score

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
