import pygame
import circleshape
import constants
import random
import math

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius, score=100):
        super().__init__(x, y, radius)
        self.score = score
        self.lines = []
        self.radiuses = []
        self.loop_range = constants.ASTEROID_RESOLUTION
        self.half_loop_range = self.loop_range/2
        
        for line in range(self.loop_range):
            random_x = self.radius
            random_y = self.radius
            #TODO: Random spiikyness
            if line % constants.ASTEROID_SPICKYNESS == 0:
                random_x = random.uniform(constants.ASTEROID_SPICKYNESS_FACTOR*self.radius, self.radius)
                random_y = random.uniform(constants.ASTEROID_SPICKYNESS_FACTOR*self.radius, self.radius) 
            offset_x = self.position.x + random_x * math.cos(line*math.pi/self.half_loop_range)
            offset_y = self.position.y + random_y * math.sin(line*math.pi/self.half_loop_range)
            self.lines.append([offset_x,offset_y])
            self.radiuses.append([random_x,random_y])

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

    def check_screen_wrap(self):
        if self.position.x < -constants.ASTEROID_MAX_RADIUS:
            self.set_position(constants.SCREEN_WIDTH, self.position.y)
        elif self.position.x > constants.SCREEN_WIDTH:
            self.set_position(0, self.position.y)
        elif self.position.y < -constants.ASTEROID_MAX_RADIUS:
            self.set_position(self.position.x, constants.SCREEN_HEIGHT)
        elif self.position.y > constants.SCREEN_HEIGHT:
            self.set_position(self.position.x, 0)
    
    def draw(self, screen):    
        self.check_screen_wrap() 
        incra = 1
        for (line, radius) in zip(self.lines,self.radiuses):
            line[0] = self.position.x + radius[0] * math.cos(incra*math.pi/self.half_loop_range)
            line[1] = self.position.y + radius[1] * math.sin(incra*math.pi/self.half_loop_range)
            incra += 1

        pygame.draw.lines(screen, (255, 255, 255 ), True, self.lines, 2)
        #pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

