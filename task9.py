"""
#Racer
import pygame, random

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load images
player_img = pygame.Surface((50, 50))
player_img.fill((0, 255, 0))
enemy_img = pygame.Surface((50, 50))
enemy_img.fill((255, 0, 0))
coin_img = pygame.Surface((30, 30))
coin_img.fill((255, 255, 0))

player = pygame.Rect(225, 500, 50, 50)
enemy = pygame.Rect(225, 0, 50, 50)
enemy_speed = 3

coins = []
coin_weights = []
score = 0
COIN_TARGET = 10

running = True
while running:
    screen.fill((0, 0, 0))
    
    # Draw player and enemy
    screen.blit(player_img, player)
    screen.blit(enemy_img, enemy)
    
    # Randomly generate coins
    if random.randint(1, 30) == 1:
        x = random.randint(0, WIDTH - 30)
        weight = random.randint(1, 5)
        coins.append(pygame.Rect(x, 0, 30, 30))
        coin_weights.append(weight)
    
    # Move coins
    for i in range(len(coins)):
        coins[i].move_ip(0, 4)
        screen.blit(coin_img, coins[i])
    
    # Move enemy
    enemy.move_ip(0, enemy_speed)
    if enemy.top > HEIGHT:
        enemy.top = 0
    
    # Coin collision
    new_coins = []
    new_weights = []
    for i, coin in enumerate(coins):
        if player.colliderect(coin):
            score += coin_weights[i]
            if score >= COIN_TARGET:
                enemy_speed += 1
                COIN_TARGET += 10
        else:
            new_coins.append(coin)
            new_weights.append(coin_weights[i])
    coins = new_coins
    coin_weights = new_weights
    
    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.move_ip(5, 0)
    
    # Event quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
"""

#Snake
"""
import pygame, random, time

pygame.init()
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = [(100, 100)]
direction = (20, 0)
food = None
food_weight = 1
food_timer = 0
score = 0

def spawn_food():
    global food, food_weight, food_timer
    food = (random.randint(0, 19)*20, random.randint(0, 19)*20)
    food_weight = random.randint(1, 5)
    food_timer = pygame.time.get_ticks()

running = True
spawn_food()
while running:
    screen.fill((0, 0, 0))
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, 20, 20))
    
    # Draw food
    if food:
        pygame.draw.rect(screen, (255, 255, 0), (*food, 20, 20))
    
    # Move snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake = [new_head] + snake[:-1]
    
    # Check collision with food
    if food and new_head == food:
        score += food_weight
        snake.append(snake[-1])
        food = None
        spawn_food()
    
    # Timer for food
    if food and pygame.time.get_ticks() - food_timer > 3000:
        food = None
        spawn_food()
    
    # Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = (0, -20)
    if keys[pygame.K_DOWN]:
        direction = (0, 20)
    if keys[pygame.K_LEFT]:
        direction = (-20, 0)
    if keys[pygame.K_RIGHT]:
        direction = (20, 0)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()"""

#Paint
"""
import pygame, sys
pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

drawing = False
start_pos = None
shape = "square"  # change to 'triangle', 'equilateral', 'rhombus'

def draw_shape(start, end, shape):
    if shape == "square":
        side = min(abs(end[0]-start[0]), abs(end[1]-start[1]))
        rect = pygame.Rect(start[0], start[1], side, side)
        pygame.draw.rect(screen, (0, 255, 0), rect, 2)

    elif shape == "triangle":
        points = [start, end, (start[0], end[1])]
        pygame.draw.polygon(screen, (255, 0, 0), points, 2)

    elif shape == "equilateral":
        side = abs(end[0] - start[0])
        height = (3**0.5 / 2) * side
        points = [start, (start[0] + side, start[1]), (start[0] + side/2, start[1] - height)]
        pygame.draw.polygon(screen, (0, 0, 255), points, 2)

    elif shape == "rhombus":
        dx = abs(end[0] - start[0]) // 2
        dy = abs(end[1] - start[1]) // 2
        center = ((start[0]+end[0])//2, (start[1]+end[1])//2)
        points = [
            (center[0], center[1] - dy),
            (center[0] + dx, center[1]),
            (center[0], center[1] + dy),
            (center[0] - dx, center[1])
        ]
        pygame.draw.polygon(screen, (255, 255, 0), points, 2)

shape_list = ["square", "triangle", "equilateral", "rhombus"]
shape_index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pygame.mouse.get_pos()
            draw_shape(start_pos, end_pos, shape_list[shape_index])
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shape_index = (shape_index + 1) % 4  # change shape

    pygame.display.flip()
    clock.tick(30)
"""
#Paint
import pygame, sys
pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

drawing = False
start_pos = None
shape = "square"  # change to 'triangle', 'equilateral', 'rhombus'

def draw_shape(start, end, shape):
    if shape == "square":
        side = min(abs(end[0]-start[0]), abs(end[1]-start[1]))
        rect = pygame.Rect(start[0], start[1], side, side)
        pygame.draw.rect(screen, (0, 255, 0), rect, 2)

    elif shape == "triangle":
        points = [start, end, (start[0], end[1])]
        pygame.draw.polygon(screen, (255, 0, 0), points, 2)

    elif shape == "equilateral":
        side = abs(end[0] - start[0])
        height = (3**0.5 / 2) * side
        points = [start, (start[0] + side, start[1]), (start[0] + side/2, start[1] - height)]
        pygame.draw.polygon(screen, (0, 0, 255), points, 2)

    elif shape == "rhombus":
        dx = abs(end[0] - start[0]) // 2
        dy = abs(end[1] - start[1]) // 2
        center = ((start[0]+end[0])//2, (start[1]+end[1])//2)
        points = [
            (center[0], center[1] - dy),
            (center[0] + dx, center[1]),
            (center[0], center[1] + dy),
            (center[0] - dx, center[1])
        ]
        pygame.draw.polygon(screen, (255, 255, 0), points, 2)

shape_list = ["square", "triangle", "equilateral", "rhombus"]
shape_index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = pygame.mouse.get_pos()
            draw_shape(start_pos, end_pos, shape_list[shape_index])
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shape_index = (shape_index + 1) % 4  # change shape

    pygame.display.flip()
    clock.tick(30)
