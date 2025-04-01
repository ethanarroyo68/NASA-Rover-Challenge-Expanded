import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))  # Width x Height
pygame.display.set_caption("Pygame Basics")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game loop flag
running = True

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw a red rectangle
    pygame.draw.rect(screen, RED, (100, 100, 200, 150))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()