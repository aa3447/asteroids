import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def get_position(self):
        return self.position
    
    def set_position(self, x, y):
        self.position = pygame.Vector2(x, y)
    
    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius
    
    def check_screen_wrap(self):
        # sub-classes must override
        pass

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
