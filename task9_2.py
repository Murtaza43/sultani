
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

