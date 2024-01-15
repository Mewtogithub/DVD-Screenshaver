import pygame
import sys
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DVD Text Animation")
font = pygame.font.Font(None, 30)
text = "DVD"
text_color = (255, 255, 255)
text_surface = font.render(text, True, text_color)
text_rect = text_surface.get_rect(center=(random.randint(0, width), random.randint(0, height)))
speed_x, speed_y = 5, 5
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
current_color = random.choice(colors)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    text_rect.x += speed_x
    text_rect.y += speed_y
    if text_rect.left <= 0 or text_rect.right >= width:
        speed_x = -speed_x
        current_color = random.choice(colors)
    if text_rect.top <= 0 or text_rect.bottom >= height:
        speed_y = -speed_y
        current_color = random.choice(colors)
    screen.fill((0, 0, 0))
    text_surface = font.render(text, True, current_color)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(30)
