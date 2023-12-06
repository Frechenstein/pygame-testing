import pygame
import sys

def laser_update(laser_list, speed = 300):
    for rect in laser_list:
        rect.y -= round(speed * dt)
        if rect.bottom < 0:
            laser_list.remove(rect)

# constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FRAMERATE = 120
PATH = 'pygame-testing/Asteroid Shooter'
FONT_SIZE = 50

# game init
pygame.init()
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Asteriod Shooter')
clock = pygame.time.Clock()

# ship import
ship_surf = pygame.image.load(PATH + '/graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

# laser import
laser_surf = pygame.image.load(PATH + '/graphics/laser.png').convert_alpha()
laser_list = []
# laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)

# background
bg_surf = pygame.image.load(PATH + '/graphics/background.png').convert()

# text import
font = pygame.font.Font(PATH + '/graphics/subatomic.ttf', FONT_SIZE)
text_surf = font.render('Space', True, 'white')
text_rect = text_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 80))

# main game loop
while True:
    
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
             print('laser')
             laser_rect = laser_surf.get_rect(midbottom = ship_rect.midbottom)
             laser_list.append(laser_rect)
            
    # framerate limit
    dt = clock.tick(FRAMERATE) / 1000	

	# mouse input 
    ship_rect.center = pygame.mouse.get_pos()

	# update
    laser_update(laser_list)
    
    # drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_surf,(0, 0))
    
    display_surface.blit(text_surf,text_rect)
    pygame.draw.rect(display_surface, 'white', text_rect.inflate(30, 30), width = 8, border_radius = 5)
    
    for rect in laser_list:
        display_surface.blit(laser_surf,rect)
        
    display_surface.blit(ship_surf,ship_rect)
    
    # draw the final frame
    pygame.display.update()