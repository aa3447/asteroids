import pygame
import circleshape
import constants

class PowerUp(circleshape.CircleShape):
    def __init__(self, x, y, radius, type):
        super().__init__(x, y, radius)
        self.type = type[0]
        self.color = type[1]

    def apply_powerup(self, player, lives):
        if self.type == "extra_life":
            lives.add_life()
        elif self.type == "shield":
            player.set_shield(True)
        elif self.type == "speed_boost":
            player.set_speed_boost(constants.POWERUP_SPEED_BOOST)
            player.set_speed_boost_timer(constants.POWERUP_SPEED_BOOST_TIMER)

    def get_power_name(self):
        return self.type

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)