import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

# Main

def main():
    #screen initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clk = pygame.time.Clock()

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    dt = 0

    #game loop
    while True:

        #close window event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Color screen
        pygame.Surface.fill(screen,"#000000")
        
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        
        #end of frame
        pygame.display.flip()
        dt = (pygame.time.Clock.tick(clk, 60)) / 1000




if __name__ == "__main__":
    main()