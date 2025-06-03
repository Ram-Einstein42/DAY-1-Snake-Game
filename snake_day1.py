# 🐍 Snake Game - Day 1

import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control frame rate
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw grid (for visualization)
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GREEN, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GREEN, (0, y), (WIDTH, y))

    pygame.display.flip()
    clock.tick(10)  # 10 frames per second

pygame.quit()
sys.exit()
