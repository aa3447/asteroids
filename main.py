import pygame
import constants
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    delta_time = 0
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
 
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(delta_time)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        delta_time = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()