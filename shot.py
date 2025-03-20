from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
    def check_collission(self, other):
        return super().check_collission(other)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt