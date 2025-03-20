import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def collides_with(self, target):
        return super().collides_with(target)
    
    def split(self):
        self.kill() # think about it, we have to kill the current asteroid, THEN create new ones
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        old_radius = self.radius
        
        random_angle = random.uniform(20,50)
        direction_of_new_asteroid_one = self.velocity.rotate(random_angle)
        direction_of_new_asteroid_two = self.velocity.rotate(-random_angle)
        new_asteroid_radius = old_radius - ASTEROID_MIN_RADIUS
        
        asteroid = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid.velocity = direction_of_new_asteroid_one * 1.2
        asteroid_two = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_two.velocity = direction_of_new_asteroid_two * 1.2