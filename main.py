import pygame
import math

pygame.init()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('assets/font/myFont.ttf', 32)
WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bgs = []
banners = []
guns = []
target_images = [[], [], []]
targets = {1: [10, 5, 3],
           2: [12, 8, 5],
           3: [15, 12, 8, 3]}
level = 1
for i in range(1, 4):
    bgs.append(pygame.image.load(f'assets/bgs/{i}.png'))
    banners.append(pygame.image.load(f'assets/banners/{i}.png'))
    guns.append(pygame.transform.scale(pygame.image.load(f'assets/guns/{i}.png'), (100, 100)))
    if i < 3:
        for j in range(1, 4):
            target_images[i - 1].append(pygame.transform.scale(pygame.image
                                                               .load(f'assets/targets/{i}/{j}.png'),
                                                               (120 - (j * 18), 80 - (j * 12))))
    else:
        for j in range(1, 5):
            target_images[i - 1].append(pygame.transform.scale(pygame.image
                                                               .load(f'assets/targets/{i}/{j}.png'),
                                                               (120 - (j * 18), 80 - (j * 12))))


def draw_gun():
    mouse_pos = pygame.mouse.get_pos()
    gun_point = (WIDTH / 2, HEIGHT - 200)
    lasers = ['red', 'purple', 'green']
    clicks = pygame.mouse.get_pressed()
    if mouse_pos[0] != gun_point[0]:
        slope = (mouse_pos[1] - gun_point[1]) / (mouse_pos[0] - gun_point[0])
    else:
        slope = -10000
    angle = math.atan(slope)
    rotation = math.degrees(angle)
    if mouse_pos[0] < WIDTH / 2:
        gun = pygame.transform.flip(guns[level - 1], True, False)
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(gun, 90 - rotation), (WIDTH / 2 - 90, HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)
    else:
        gun = guns[level - 1]
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(gun, 270 - rotation), (WIDTH / 2 - 30, HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)


def draw_level(coords):
    if level == 1 or level == 2:
        target_rects = [[], [], []]
    else:
        target_rects = [[], [], [], []]
    for in_range in range(len(coords)):
        for jrange in range(len(coords[in_range])):
            target_rects[in_range].append(pygame.rect.Rect((coords[in_range][jrange][0] + 20, coords[in_range][jrange][1]), (60 - in_range * 12, 60 - in_range * 12)))
            screen.blit(target_images[level - 1][in_range], coords[in_range][jrange])
    return target_rects


# initialize enemy coordinates

one_coords = [[], [], []]
two_coords = [[], [], []]
three_coords = [[], [], [], []]
for i in range(3):
    my_list = targets[1]
    for j in range(my_list[i]):
        one_coords[i].append(((WIDTH//my_list[i]) * j, 300 - (i * 150) + 30 * (j % 2)))
for i in range(3):
    my_list = targets[2]
    for j in range(my_list[i]):
        two_coords[i].append(((WIDTH//my_list[i]) * j, 300 - (i * 150) + 30 * (j % 2)))
for i in range(4):
    my_list = targets[3]
    for j in range(my_list[i]):
        three_coords[i].append(((WIDTH//my_list[i]) * j, 300 - (i * 100) + 30 * (j % 2)))


run = True

while run:
    timer.tick(fps)

    screen.fill('black')
    screen.blit(bgs[level - 1], (0, 0))
    screen.blit(banners[level - 1], (0, HEIGHT - 200))
    if level == 1:
        target_boxes = draw_level(one_coords)
    elif level == 2:
        target_boxes = draw_level(two_coords)
    else:
        target_boxes = draw_level(three_coords)

    if level > 0:
        draw_gun()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
