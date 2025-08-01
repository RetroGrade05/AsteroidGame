import pygame
from constants import *
from player import *

# Main

def main():
    #starting prints
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #screen initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clk = pygame.time.Clock()

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (drawable, updatable)

    dt = 0
    player = Player(x = SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    

    #game loop
    while True:

        #close window event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Color screen
        pygame.Surface.fill(screen,"#000000")
        
        updatable.update(dt)
        player.draw(screen)
        
        #end of frame
        pygame.display.flip()
        dt = (pygame.time.Clock.tick(clk, 60)) / 1000




if __name__ == "__main__":
    main()