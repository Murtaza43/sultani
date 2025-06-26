import pygame
import sys
from datetime import datetime

# initial pygame setup
pygame.init()
WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# loading the image
bg = pygame.image.load("background.png").convert_alpha()
right_hand = pygame.image.load("right_hand.png").convert_alpha()  # minute
left_hand = pygame.image.load("left_hand.png").convert_alpha()    # second

# adjust the center of rotation
def blit_rotate_center(surf, image, top_left, angle):
    rotated = pygame.transform.rotate(image, angle)
    new_rect = rotated.get_rect(center=image.get_rect(topleft=top_left).center)
    surf.blit(rotated, new_rect.topleft)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # get the currint time
    now = datetime.now()
    minute = now.minute
    second = now.second

    # calculating of angles
    minute_angle = -minute * 6       # 360 / 60 = 6 degrees for each minutes
    second_angle = -second * 6

    # drawing
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))

    # right hand for minutes
    blit_rotate_center(screen, right_hand, CENTER, minute_angle)
    # left hand for seconds
    blit_rotate_center(screen, left_hand, CENTER, second_angle)

    pygame.display.update()
    clock.tick(60)