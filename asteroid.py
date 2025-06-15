from circleshape import *
from constants import * 
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(random_angle) * 1.2
        vector_2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius, vector_1)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius, vector_2)
        return new_asteroid_1, new_asteroid_2