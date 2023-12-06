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
clock = pygame.time.Clock()

# importing images
ship_surf = pygame.image.load(PATH + '/graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT))
bg_surf = pygame.image.load(PATH + '/graphics/background.png').convert()

# import text
font = pygame.font.Font(PATH + '/graphics/subatomic.ttf', FONT_SIZE)
text_surf = font.render('Space', True, 'white')
text_rect = text_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 80))

# main game loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # framerate limit
    clock.tick(120)
            
    # mouse input
    ship_rect.center = pygame.mouse.get_pos()
    
    # updates
    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_surf,(0, 0))
    
    display_surface.blit(ship_surf,ship_rect)
    display_surface.blit(text_surf,text_rect)
    
    pygame.display.update()