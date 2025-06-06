import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions and cell size
# Screen and grid setup
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

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

# Score
score = 0
font = pygame.font.SysFont('Arial', 24)

# Show game over screen
def game_over():
    msg = font.render(f"Game Over! Final Score: {score}", True, WHITE)
    rect = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(msg, rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Game loop
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

    direction = change_to

    # Move the snake
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
        score += 1
        food_spawned = False
    else:
        snake_body.pop()

    # 🍎 Spawn new food if eaten
    if not food_spawned:
        food_pos = [
            random.randrange(0, WIDTH, CELL_SIZE),
            random.randrange(0, HEIGHT, CELL_SIZE)
        ]
        food_spawned = True

     
     # 🚨 Game Over: wall collision
    if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
        snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
        game_over()
    
    # 🚨 Game Over: self collision
    if snake_pos in snake_body[1:]:
        game_over()
    # Draw everything
    screen.fill(BLACK)

    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))
    # Display score
     # Draw score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)