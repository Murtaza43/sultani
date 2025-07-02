import pygame
import random

pygame.init()

# Game screen settings
WIDTH = 400
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# machine setting
car_width = 50
car_height = 80
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 10
car_speed = 5

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)

# setting the FPS
clock = pygame.time.Clock()
FPS = 60

# Definition of coin class
class Coin:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = -random.randint(100, 300)
        self.radius = 10
        self.color = GOLD
        self.speed = 5

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.y += self.speed

# Coin list and points counter
coins = [Coin()]
score = 0
font = pygame.font.SysFont(None, 36)

# The main loop of the game
run = True
while run:
    clock.tick(FPS)
    win.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Moving the car with keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # Movement and coin collision analysis
    for coin in coins[:]:
        coin.move()
        coin.draw(win)
    # Simple collision based on the distance between the center of the coin and the center of the machine
        car_center_x = car_x + car_width // 2
        car_center_y = car_y + car_height // 2
        if abs(coin.x - car_center_x) < 30 and abs(coin.y - car_center_y) < 30:
            coins.remove(coin)
            score += 1

    # adding new coins every few frames
    if random.randint(0, 60) == 0:
        coins.append(Coin())

    # show the car image
    pygame.draw.rect(win, BLUE, (car_x, car_y, car_width, car_height))

    # showing the rewards top right
    score_text = font.render(f"Coins: {score}", True, BLACK)
    win.blit(score_text, (WIDTH - 140, 10))

    pygame.display.update()

pygame.quit()
