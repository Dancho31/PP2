import pygame
import random
import json
import os

pygame.init()

# Настройки
WIDTH, HEIGHT = 600, 400
BLOCK = 20
DATA_FILE = "snake_data.json"

# Цвета
WHITE, BLACK, RED, GREEN = (255, 255, 255), (0, 0, 0), (213, 50, 80), (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Expert')
clock = pygame.time.Clock()

font_s = pygame.font.SysFont("Verdana", 20)

def load_hs():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f: return json.load(f).get("hs", 0)
    return 0

def save_hs(val):
    with open(DATA_FILE, "w") as f: json.dump({"hs": val}, f)

def generate_food(snake_list):
    while True:
        fx = round(random.randrange(0, WIDTH - BLOCK) / BLOCK) * BLOCK
        fy = round(random.randrange(0, HEIGHT - BLOCK) / BLOCK) * BLOCK
        if [fx, fy] not in snake_list: return fx, fy

def gameLoop():
    high_score = load_hs()
    game_over = False
    x, y = WIDTH/2, HEIGHT/2
    dx, dy = 0, 0
    snake = []
    length = 1
    score = 0
    level = 1
    speed = 10
    fx, fy = generate_food(snake)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0: dx, dy = -BLOCK, 0
                elif event.key == pygame.K_RIGHT and dx == 0: dx, dy = BLOCK, 0
                elif event.key == pygame.K_UP and dy == 0: dy, dx = -BLOCK, 0
                elif event.key == pygame.K_DOWN and dy == 0: dy, dx = BLOCK, 0

        # СТОЛКНОВЕНИЕ СО СТЕНАМИ
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            if score > high_score: save_hs(score)
            game_over = True

        x += dx
        y += dy
        screen.fill(BLACK)
        
        pygame.draw.rect(screen, RED, [fx, fy, BLOCK, BLOCK])
        
        head = [x, y]
        snake.append(head)
        if len(snake) > length: del snake[0]

        # СТОЛКНОВЕНИЕ С СОБОЙ
        for segment in snake[:-1]:
            if segment == head: game_over = True

        for segment in snake:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], BLOCK, BLOCK])

        # ИНТЕРФЕЙС
        info = font_s.render(f"Score: {score} Lvl: {level} Best: {high_score}", True, WHITE)
        screen.blit(info, [5, 5])

        if x == fx and y == fy:
            fx, fy = generate_food(snake)
            length += 1
            score += 1
            # ПЕРЕХОД НА УРОВЕНЬ
            if score % 3 == 0:
                level += 1
                speed += 2

        pygame.display.update()
        clock.tick(speed)

    pygame.quit()

gameLoop()