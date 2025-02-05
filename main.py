import sys
import pygame
import constants
import player
import asteroid
import asteroidfield
import shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    delta_time = 0
    score = 0
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (updatable, drawable, shots)
    
    current_player = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    asteroidfield.AsteroidField()
 
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Final score: {score}")
                return
        
        screen.fill((0, 0, 0))
        updatable.update(delta_time)
        
        for rock in asteroids:
            if rock.collides_with(current_player):
                print(f"Final score: {score}")
                sys.exit("Game Over!")
            for bullet in shots:
                if rock.collides_with(bullet):
                    score += rock.split()
                    print(f"Score: {score}")
                    bullet.kill()
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        delta_time = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()