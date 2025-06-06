# 🐍 Snake Game - Day 5: Restart Option & Game Reset
import pygame
import sys
import random

pygame.init()

# Screen and grid setup
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)

def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))

def draw_food(food_pos):
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

def draw_score(score):
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over_screen(score):
    screen.fill(BLACK)
    msg = font.render(f'Game Over! Final Score: {score}', True, WHITE)
    replay = font.render('Press R to Restart or Q to Quit', True, WHITE)
    screen.blit(msg, msg.get_rect(center=(WIDTH//2, HEIGHT//2 - 20)))
    screen.blit(replay, replay.get_rect(center=(WIDTH//2, HEIGHT//2 + 20)))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # restart
                elif event.key == pygame.K_q:
                    pygame.quit(); sys.exit()

# 🌀 Main Game Loop (with restart capability)
while True:
    # 🧼 Reset all game state
    snake_pos = [100, 50]
    snake_body = [[100, 50], [80, 50], [60, 50]]
    direction = 'RIGHT'
    change_to = direction
    food_pos = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
    food_spawned = True
    score = 0
    speed = 10

    # 🕹 In-game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
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

        # Move snake
        if direction == 'UP': snake_pos[1] -= CELL_SIZE
        if direction == 'DOWN': snake_pos[1] += CELL_SIZE
        if direction == 'LEFT': snake_pos[0] -= CELL_SIZE
        if direction == 'RIGHT': snake_pos[0] += CELL_SIZE

        # Insert head
        snake_body.insert(0, list(snake_pos))

        # Check for food
        if snake_pos == food_pos:
            score += 1
            food_spawned = False
        else:
            snake_body.pop()

        if not food_spawned:
            food_pos = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
            food_spawned = True

        # 🚨 Game Over conditions
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT or
            snake_pos in snake_body[1:]):
            break  # exit inner loop to show Game Over screen

        # 🖼 Draw everything
        screen.fill(BLACK)
        draw_snake(snake_body)
        draw_food(food_pos)
        draw_score(score)
        pygame.display.flip()
        clock.tick(speed)

    # 💀 Game Over — show restart options
    if not game_over_screen(score):
        break  # only reached if player quits
