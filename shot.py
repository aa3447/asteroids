import pygame
import circleshape
import constants

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.wrap_count = 0

    def check_screen_wrap(self):
        if self.wrap_count > 1:
            self.kill()
        elif self.position.x < 0:
            self.set_position(constants.SCREEN_WIDTH, self.position.y)
            self.wrap_count += 1
        elif self.position.x > constants.SCREEN_WIDTH:
            self.set_position(0, self.position.y)
            self.wrap_count += 1
        elif self.position.y < 0:
            self.set_position(self.position.x, constants.SCREEN_HEIGHT)
            self.wrap_count += 1
        elif self.position.y > constants.SCREEN_HEIGHT:
            self.set_position(self.position.x, 0)
            self.wrap_count += 1

    def draw(self, screen):
        self.check_screen_wrap()
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt