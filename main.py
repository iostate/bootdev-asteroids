import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill screen with black
        screen.fill("black")

        # Tells us time before last refresh
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
        # Draw player object in the center
        player.draw(screen)
        player.update(dt)
        
        # Refresh screen, should always be called last
        pygame.display.flip()


if __name__ == "__main__":
    main()