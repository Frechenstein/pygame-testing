import pygame
import sys

pygame.init()

# constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
PATH = 'pygame-testing/Asteroid Shooter'
FONT_SIZE = 50

# initialize screen
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Asteriod Shooter')

# importing images
ship_surf = pygame.image.load(PATH + '/graphics/ship.png').convert_alpha()
bg_surf = pygame.image.load(PATH + '/graphics/background.png').convert()

# import text
font = pygame.font.Font(PATH + '/graphics/subatomic.ttf', FONT_SIZE)
text_surf = font.render('Space', True, 'white')


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # updates
    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_surf,(0, 0))
    display_surface.blit(ship_surf,(300, 500))
    display_surface.blit(text_surf,(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    
    pygame.display.update()