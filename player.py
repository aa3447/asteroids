import pygame
import circleshape
import constants
import shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.current_speed = 0
        self.shield = False
        self.speed_boost = 1
        self.speed_boost_timer = 0

    def set_shield(self, bool):
        if bool:
            print("Shield Gained!")
        else:
            print("Shield Lost!")
        self.shield = bool

    def get_shield(self):
        return self.shield
    
    def set_speed_boost(self,value):
        print("Speeeed Booooost!!")
        self.speed_boost = value
    
    def get_speed_boost(self):
        return self.speed_boost
    
    def set_speed_boost_timer(self , value):
        self.speed_boost_timer = value

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        adjusted_max_speed = constants.PLAYER_MAX_SPEED * self.speed_boost
        if self.current_speed > adjusted_max_speed:
            self.current_speed = adjusted_max_speed
        if self.current_speed < -adjusted_max_speed:
            self.current_speed = -adjusted_max_speed
        
        self.position += forward * self.current_speed * dt
    
    def momentum(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.current_speed * dt
        adjusted_acceleration = constants.PLAYER_ACCELERATION * self.speed_boost
        if self.current_speed > 0:
            self.current_speed -= adjusted_acceleration
        else:
            self.current_speed += adjusted_acceleration

    def shoot(self):
        bullet = shot.Shot(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
    
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
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.speed_boost > 1:
            self.speed_boost_timer -= dt
            print(self.speed_boost_timer)
            if self.speed_boost_timer <= 0:
                self.speed_boost = 1
                print("Speed Boost Over!")
                
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w] and not keys[pygame.K_s]:
            adjusted_acceleration = constants.PLAYER_ACCELERATION * self.speed_boost
            if self.current_speed < 0:
                self.current_speed += adjusted_acceleration * constants.PLAYER_DEACCELERATION
            else:
                self.current_speed += adjusted_acceleration
            self.move(dt)
        if keys[pygame.K_s] and not keys[pygame.K_w]:
            adjusted_acceleration = constants.PLAYER_ACCELERATION * self.speed_boost
            if self.current_speed > 0:
                self.current_speed -= adjusted_acceleration * constants.PLAYER_DEACCELERATION
            else:
                self.current_speed -= adjusted_acceleration
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shot_timer -= dt
            if self.shot_timer <= 0:
                self.shoot()
                self.shot_timer = constants.PLAYER_SHOOT_COOLDOWN
        if not (keys[pygame.K_w] or keys[pygame.K_s]):
            self.momentum(dt)