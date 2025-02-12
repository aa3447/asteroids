import sys
import pygame
import constants
import player
import asteroid
import asteroidfield
import shot
import score
import lives
import powerupspawner
import powerup

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    delta_time = 0
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    asteroidfield.AsteroidField.containers = (updatable)
    powerupspawner.PowerUpSpawner.containers = (updatable)
    powerup.PowerUp.containers = (drawable, powerups)
    shot.Shot.containers = (updatable, drawable, shots)
    
    current_player = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    scoring = score.Score()
    current_field = asteroidfield.AsteroidField()
    powerup_spawner = powerupspawner.PowerUpSpawner()
    player_lives = lives.Lives()
 
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        scoring.add_time(delta_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Time bonus: {scoring.get_time_bonus()}")
                print(f"Final score: {scoring.get_score()}")
                return
        
        screen.fill((0, 0, 0))
        updatable.update(delta_time)

        current_field.set_asteroid_count(len(asteroids.sprites()))
        powerup_spawner.set_powerup_count(len(powerups.sprites()))
        player_lives.score_extra_life(scoring.get_score())
        
        for rock in asteroids:
            
            if rock.collides_with(current_player):
                if not current_player.get_shield():
                    player_lives.lose_life()
                    if not player_lives.is_alive():
                        print(f"Time bonus: {scoring.get_time_bonus()}")
                        print(f"Final score: {scoring.get_score()}")
                        sys.exit("Game Over!")
                    current_player  = reset_game(drawable, asteroids, shots, updatable, current_field, powerups, powerup_spawner)
                    break
                else:
                    rock.kill()
                    current_player.set_shield(False)

            for bullet in shots:
                if rock.collides_with(bullet):
                    scoring.add_score(rock.split())
                    print(f"Score: {scoring.get_score()}")
                    bullet.kill()

            for pup in powerups:
                if pup.collides_with(current_player):
                    pup.apply_powerup(current_player, player_lives)
                    pup.kill()

        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        delta_time = game_clock.tick(60)/1000

def reset_game(drawable, asteroids, shots, updatable, current_field, powerups, powerup_spawner):
    drawable.empty()
    asteroids.empty()
    shots.empty()
    powerups.empty()
    updatable.empty()
    updatable.add(current_field, powerup_spawner)
    return player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

if __name__ == "__main__":
    main()