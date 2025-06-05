# 🐍 Snake Game - Day 3: Food, Eating, and Snake Growth
import pygame
import sys
import random # needed to randomly place food

pygame.init()

# Screen & cell setup
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake setup
snake_pos = [100, 50]
snake_body = [[100, 50], [80, 50], [60, 50]]
direction = 'RIGHT'
change_to = direction
speed = 10

# Food setup

food_pos = [
    random.randrange(0, WIDTH, CELL_SIZE),
    random.randrange(0, HEIGHT, CELL_SIZE)
]

food_spawned = True

# Main loop

while True:
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

    # Update snake position
    if direction == 'UP':
        snake_pos[1] -= CELL_SIZE
    elif direction == 'DOWN':
        snake_pos[1] += CELL_SIZE
    elif direction == 'LEFT':
        snake_pos[0] -= CELL_SIZE
    elif direction == 'RIGHT':
        snake_pos[0] += CELL_SIZE

# Insert new head
    snake_body.insert(0, list(snake_pos))

    # 🍽️ Check if snake eats food
    if snake_pos == food_pos:
        food_spawned = False  # Don't remove tail = snake grows
    else:
        snake_body.pop()  # Remove tail if no food eaten

    # 🍎 Spawn new food if eaten
    if not food_spawned:
        food_pos = [
            random.randrange(0, WIDTH, CELL_SIZE),
            random.randrange(0, HEIGHT, CELL_SIZE)
        ]
        food_spawned = True

    # Draw background
    screen.fill(BLACK)

    # 🟩 Draw snake
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))

    # 🔴 Draw food
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    # Refresh screen
    pygame.display.flip()
    clock.tick(speed)
