import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Ball settings
RADIUS = 25
ball_color = (255, 0, 0)  # Red
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
STEP = 20  # Move step

# Background color
bg_color = (255, 255, 255)  # White

# Main game loop
running = True
while running:
    screen.fill(bg_color)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), RADIUS)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move the ball based on key press, with boundary checks
    if keys[pygame.K_UP] and ball_y - RADIUS - STEP >= 0:
        ball_y -= STEP
    if keys[pygame.K_DOWN] and ball_y + RADIUS + STEP <= HEIGHT:
        ball_y += STEP
    if keys[pygame.K_LEFT] and ball_x - RADIUS - STEP >= 0:
        ball_x -= STEP
    if keys[pygame.K_RIGHT] and ball_x + RADIUS + STEP <= WIDTH:
        ball_x += STEP

    # Delay to control frame rate
    pygame.time.delay(100)

# Quit pygame
pygame.quit()
sys.exit()
