import pygame
import circleshape

class PowerUp(circleshape.CircleShape):
    def __init__(self, x, y, radius,type):
        super().__init__(x, y, radius)
        self.type = type[0]
        self.color = type[1]

    def apply_powerup(self, player, lives):
        temp_type = self.type
        if temp_type == "extra_life":
            lives.add_life()
        elif temp_type == "shield":
            player.set_shield(True)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)