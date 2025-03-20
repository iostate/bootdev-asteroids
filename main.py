import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Create groups of sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # You can iterate over objects in a group just like any other collection in Python:
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    
    # After changing a static field like containers, make sure to create all Player 
    # objects after the change. This way, they will be correctly added to the groups.
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Can call the .update() method for every member of a group by calling it on the group itself
        updatable.update(dt)
        
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
                
            for shot in shots:
                if asteroid.collides_with(shot):
                    print("Collission between bullet and asteroid!")
                    asteroid.kill()
                    shot.kill()
        
        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)

            
        pygame.display.flip()
        
        # Tells us time before last refresh
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()