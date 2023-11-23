import pygame
import sys
from datetime import datetime

pygame.init()

window_width, window_height = 1000, 800
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mickey Clock")

body_image = pygame.image.load("main-clock.png")  
left_hand_image = pygame.image.load("left-hand.png")  
right_hand_image = pygame.image.load("right-hand.png")  

game_clock = pygame.time.Clock()
is_running = True

def draw_timepiece(seconds_angle, minutes_angle):
    screen.fill((255, 255, 255))

    screen.blit(body_image, (window_width // 2 - body_image.get_width() // 2, window_height // 2 - body_image.get_height() // 2))

    left_hand_rotated = pygame.transform.rotate(left_hand_image, seconds_angle)
    right_hand_rotated = pygame.transform.rotate(right_hand_image, minutes_angle)

    screen.blit(left_hand_rotated, (window_width // 2 - left_hand_rotated.get_width() // 2, window_height // 2 - left_hand_rotated.get_height() // 2))
    screen.blit(right_hand_rotated, (window_width // 2 - right_hand_rotated.get_width() // 2, window_height // 2 - right_hand_rotated.get_height() // 2))

    pygame.display.flip()

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    current_time = datetime.now().time()
    current_seconds = current_time.second
    current_minutes = current_time.minute

    seconds_angle = -current_seconds * 6  
    minutes_angle = -current_minutes * 6  

    draw_timepiece(seconds_angle, minutes_angle)

    game_clock.tick(1)  

pygame.quit()
sys.exit()
