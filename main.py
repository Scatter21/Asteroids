# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Shot.containers = (updatable, drawable, shots)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    
    while True:
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        pygame.Surface.fill(screen, (0, 0, 0))
        
        for item in drawable:
            item.draw(screen)

        for item in asteroids:
            if item.col_check(player):
                sys.exit("Game over!")

        for item in asteroids:
            for shot in shots:
                if item.col_check(shot):
                    item.split()
                    shot.kill()
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
