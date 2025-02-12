import pygame
import constants
import random
import powerup

class PowerUpSpawner(pygame.sprite.Sprite):
    powerups = [("extra_life" , [0,255,0]), ("shield" , [0,226,225])]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.powerup_count = 0

    def set_powerup_count(self, value):
        self.powerup_count = value

    def spawn(self,position):
        new_powerup = powerup.PowerUp(position.x,position.y, constants.POWERUP_RADIUS, random.choice(self.powerups))
    
    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > constants.POWERUP_SPAWN_RATE and self.powerup_count < constants.POWERUP_MAX_SPAWN:
            self.spawn_timer = 0

            # spawn a new powerup at a random position
            position = pygame.Vector2(random.uniform(0, constants.SCREEN_WIDTH), random.uniform(0, constants.SCREEN_HEIGHT))
            self.spawn(position)