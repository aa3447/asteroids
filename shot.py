import pygame
import circleshape
import constants

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)

    def check_screen_wrap(self):
        if self.position.x < 0:
            self.set_position(constants.SCREEN_WIDTH, self.position.y)
        elif self.position.x > constants.SCREEN_WIDTH:
            self.set_position(0, self.position.y)
        elif self.position.y < 0:
            self.set_position(self.position.x, constants.SCREEN_HEIGHT)
        elif self.position.y > constants.SCREEN_HEIGHT:
            self.set_position(self.position.x, 0)

    def draw(self, screen):
        self.check_screen_wrap()
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt