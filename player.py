# in the player class
import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Dont need to set the x and y again since the parent class handles it
        # self.x = x
        # self.y = y
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Draws a triangle representing player, overrides circleshape method
    def draw(self,screen):
        points = self.triangle()
        pygame.draw.polygon(screen, 'white', points, 2)
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    # Overrides circleshape method
    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        # Move up
        if keys[pygame.K_w]:
            self.move(dt)
        # Move down
        if keys[pygame.K_s]:
            self.move(-dt)
        # Rotate left
        if keys[pygame.K_a]:
            self.rotate(-dt)
        # Rotate right
        if keys[pygame.K_d]:
           self.rotate(dt)
        #Shoot projectile
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):       
        if self.timer > 0:
            return
        
        self.timer = PLAYER_SHOOT_COOLDOWN    
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = (pygame.Vector2(0,1).rotate(self.rotation)) * PLAYER_SHOOT_SPEED



