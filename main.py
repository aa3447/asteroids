import sys
import pygame
import constants
import player
import asteroid
import asteroidfield
import shot
import score

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    delta_time = 0
    total_time = 0
    lives = 3
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (updatable, drawable, shots)
    
    current_player = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    scoring = score.Score()
    current_field = asteroidfield.AsteroidField()
 
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        total_time += delta_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scoring.add_time(total_time)
                print(f"Time bonus: {scoring.get_time_bonus()}")
                print(f"Final score: {scoring.get_score()}")
                return
        
        screen.fill((0, 0, 0))
        updatable.update(delta_time)
        
        for rock in asteroids:
            if rock.collides_with(current_player):
                lives -= 1
                print(f"Lives: {lives}")
                if lives <= 0:
                    scoring.add_time(total_time)
                    print(f"Time bonus: {scoring.get_time_bonus()}")
                    print(f"Final score: {scoring.get_score()}")
                    sys.exit("Game Over!")
                current_player  = reset_game(drawable, asteroids, shots, updatable, current_field)
                break
            for bullet in shots:
                if rock.collides_with(bullet):
                    scoring.add_score(rock.split())
                    print(f"Score: {scoring.get_score()}")
                    bullet.kill()
                    
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        delta_time = game_clock.tick(60)/1000

def reset_game(drawable, asteroids, shots, updatable, current_field):
    drawable.empty()
    asteroids.empty()
    shots.empty()
    updatable.empty()
    updatable.add(current_field)
    return player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

if __name__ == "__main__":
    main()