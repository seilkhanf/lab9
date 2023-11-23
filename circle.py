import pygame
import sys, time

window_width, window_height = 500, 500
screen = pygame.display.set_mode((window_width, window_height))

bg_color = (255,255,255)
circle_color = (255,0,0)

circle_radius = 25
circle_x = window_width // 2
circle_y = window_height // 2
movement_speed = 20
game_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and circle_y > 0:
        circle_y -= movement_speed
    if keys[pygame.K_DOWN] and circle_y < window_height:
        circle_y += movement_speed
    if keys[pygame.K_LEFT] and circle_x > 0:
        circle_x -= movement_speed
    if keys[pygame.K_RIGHT] and circle_x < window_width:
        circle_x += movement_speed
    
    screen.fill(bg_color)
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
    pygame.display.flip()
    game_clock.tick(30)
