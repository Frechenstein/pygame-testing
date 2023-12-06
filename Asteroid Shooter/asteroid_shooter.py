import pygame
import sys
from random import randint, uniform

def laser_update(laser_list, speed):
    for rect in laser_list:
        rect.y -= speed * dt
        if rect.bottom < 0:
            laser_list.remove(rect)
            
def laser_upgrade(kills, laser_list):
    if kills %5 == 0 and kills != 0 and kills %10 != 0 and laser_list[2]:
        laser_list[1] += 100
        laser_list[2] = False
    elif kills %10 == 0 and kills != 0 and laser_list[2]:
        laser_list[0] -= 50
        laser_list[2] = False
    elif kills %5 != 0:
        laser_list[2] = True
    return laser_list
            
def meteor_update(meteor_list, speed = 200):
    for meteor_tuple in meteor_list:
        
        direction = meteor_tuple[1]
        meteor_rect = meteor_tuple[0]
        meteor_rect.center += direction * speed * dt
        if meteor_rect.top > SCREEN_HEIGHT:
            meteor_list.remove(meteor_tuple)

def display_score(kills):
    score_text = f'Time: {pygame.time.get_ticks() // 1000}   Score: {kills}'
    text_surf = font.render(score_text, True, 'white')
    text_rect = text_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 80))
    display_surface.blit(text_surf,text_rect)
    pygame.draw.rect(display_surface, 'white', text_rect.inflate(30, 30), width = 8, border_radius = 5)

def laser_timer(can_shoot, duration):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot

# constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FRAMERATE = 120
PATH = 'pygame-testing/Asteroid Shooter'
FONT_SIZE = 50

# game variables
LASER_COOLDOWN = 500    # in ms
LASER_SPEED = 300
LASER_R = True
LASER_LIST = [LASER_COOLDOWN, LASER_SPEED, LASER_R]
KILLS = 0

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

# laser timer
can_shoot = True
shoot_time = None

# background
bg_surf = pygame.image.load(PATH + '/graphics/background.png').convert()

# text import
font = pygame.font.Font(PATH + '/graphics/subatomic.ttf', FONT_SIZE)

# meteor
meteor_surf = pygame.image.load(PATH + '/graphics/meteor.png').convert_alpha()
meteor_list = []

# meteor timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

# import sound
laser_sound = pygame.mixer.Sound(PATH + '/sounds/laser.ogg')
explosion_sound = pygame.mixer.Sound(PATH + '/sounds/explosion.wav')
background_music = pygame.mixer.Sound(PATH + '/sounds/music.wav')
background_music.play()

# main game loop
while True:
    
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            
            # laser
            laser_rect = laser_surf.get_rect(midbottom = ship_rect.midbottom)
            laser_list.append(laser_rect)
            
            # timer
            can_shoot = False
            shoot_time = pygame.time.get_ticks()
            
            # play laser sound
            laser_sound.play()
            
        if event.type == meteor_timer:
            
            # random position
            x_pos = randint(-100,SCREEN_WIDTH + 100)
            y_pos = randint(-100, -50)
            
            # creating a rect
            meteor_rect = meteor_surf.get_rect(midbottom = (x_pos, y_pos))
            
            # create a random direction
            direction = pygame.math.Vector2(uniform(-0.5,0.5),1)
            
            meteor_list.append((meteor_rect, direction))
            
    # framerate limit
    dt = clock.tick(FRAMERATE) / 1000	

	# mouse input 
    ship_rect.center = pygame.mouse.get_pos()

	# update
    laser_update(laser_list, LASER_LIST[1])
    can_shoot = laser_timer(can_shoot, LASER_COOLDOWN)
    meteor_update(meteor_list)
    
    LASER_LIST = laser_upgrade(KILLS, LASER_LIST)
    print(LASER_LIST)
    
    # meteor ship collisions
    for meteor_tuple in meteor_list:
        meteor_rect = meteor_tuple[0]
        if ship_rect.colliderect(meteor_rect):
            pygame.quit()
            sys.exit()
    
    # laser meteor collision
    for laser_rect in laser_list:
        for meteor_tuple in meteor_list:
            if laser_rect.colliderect(meteor_tuple[0]):
                meteor_list.remove(meteor_tuple)
                laser_list.remove(laser_rect)
                explosion_sound.play()
                KILLS += 1
    
    # drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_surf,(0, 0))
    
    display_score(KILLS)
    
    for meteor_tuple in meteor_list:
        display_surface.blit(meteor_surf,meteor_tuple[0])
    
    for rect in laser_list:
        display_surface.blit(laser_surf,rect)
        
    display_surface.blit(ship_surf,ship_rect)
    
    # draw the final frame
    pygame.display.update()