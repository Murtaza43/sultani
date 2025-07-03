#Snake
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

pygame.quit()