# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *


def main():
    # Creates the black screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    # Create groups for managing updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add to all instances of these groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Remember to make containers first then create player object, 
    # otherwise you get a blank screen for player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y,PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    while(True):
        # Makes the close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Calls the player object directly   
        # player.update(dt)

        # Updates on updatable groups(containers)
        updatable.update(dt)


        
        for asteroid in asteroids:
            # Check to see if player hits asteroids
            if asteroid.colliding(player):
                print('Game over')
                sys.exit()
            # Check to see if projectile hits asteroids
            for shot in shots:
                if asteroid.colliding(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        # Calls the player object directly
        # player.draw(screen)

        # Iterates over drawable groups(containers)
        for drawing in drawable:
            drawing.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        delta_time = clock.tick(60)
        dt = delta_time/1000
    

if __name__ == "__main__":
    main()