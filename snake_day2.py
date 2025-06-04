# 🐍 Snake Game - Day 2: Drawing and Moving the Snake
# Learn to draw the snake and move it using arrow keys

import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions and cell size
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

# Create game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control frame rate
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Snake initial position
snake_pos = [100, 50]

# Snake body seagments
snake_body = [
    [100, 50],
    [80, 50],
    [60, 50]
]

# Direction of the snake
direction = 'RIGHT'

# store new direction based on key press
change_to = direction

# speed of the snake
speed = 10

# Main loop
while True:
    # Event loop — listens for user inputs (like keypress or quit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
    # Update direction
    direction = change_to

    # Update snake position based on direction
    if direction == 'UP':
        snake_pos[1] -= CELL_SIZE
    elif direction == 'DOWN':
        snake_pos[1] += CELL_SIZE
    elif direction == 'LEFT':
        snake_pos[0] -= CELL_SIZE
    elif direction == 'RIGHT':
        snake_pos[0] += CELL_SIZE

    # Insert new position at the front of the snake body
    snake_body.insert(0, list(snake_pos))

    # Remove the last segment of the snake body
    snake_body.pop()

    # Fill the screen with black color
    screen.fill(BLACK)

    # Draw the snake
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))
        
    # Refresh the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(speed)