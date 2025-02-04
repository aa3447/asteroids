import pygame
import constants
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    delta_time = 0
    current_player = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        current_player.update(delta_time)
        current_player.draw(screen)
        pygame.display.flip()
        delta_time = game_clock.tick(60)/1000

if __name__ == "__main__":
    main()