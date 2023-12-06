import pygame
import sys

pygame.init()

# constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteriod Shooter")

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # updates
    display_surface.fill((0, 0, 0))
    
    pygame.display.update()