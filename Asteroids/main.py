import pygame
from constants import *

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
    dt = 0

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,"#000000")
        pygame.display.flip()
        dt = (pygame.time.Clock.tick(clk, 60)) / 1000

if __name__ == "__main__":
    main()