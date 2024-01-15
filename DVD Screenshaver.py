import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DVD Text Animation")

# Set up the font
font_path = "path_to_your_font.ttf"  # Replace with the path to your font file
font_size = 30
font = pygame.font.Font(font_path, font_size)

# Set up the initial position of the animated text
text = "DVD"
text_color = (255, 255, 255)
text_surface = font.render(text, True, text_color)
text_rect = text_surface.get_rect(center=(random.randint(0, width), random.randint(0, height)))

# Set up the initial speed of the animation
speed_x, speed_y = 5, 5

# Set up colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Choose a random initial color
current_color = random.choice(colors)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the position of the animated text
    text_rect.x += speed_x
    text_rect.y += speed_y

    # Change color when hitting the window borders
    if text_rect.left <= 0 or text_rect.right >= width:
        speed_x = -speed_x
        current_color = random.choice(colors)
    if text_rect.top <= 0 or text_rect.bottom >= height:
        speed_y = -speed_y
        current_color = random.choice(colors)

    # Fill the screen with a black background
    screen.fill((0, 0, 0))

    # Draw the animated text with the current color
    text_surface = font.render(text, True, current_color)
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

    # Control the speed of the animation
    pygame.time.Clock().tick(30)
