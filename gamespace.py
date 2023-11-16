import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([500, 500])
bg = pygame.image.load('World_map.png')
pygame.display.set_caption('Legend of Link')

link_x = 232
link_y = 232
x = 50
y = 50
width = 20
height = 30
vel = 1


def redrawGameWindow():
    screen.blit(bg, (x, y))
    pygame.draw.rect(screen, (255, 255, 255), (link_x, link_y, width, height))
    pygame.display.update()
    pygame.time.Clock().tick(165)


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # camera movement
    keys = pygame.key.get_pressed()

    if link_x == 232:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            x += vel
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x -= vel
        if x < -780:
            x = -780
        if x > 0:
            x = 0
    if link_y == 232:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            y += vel
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            y -= vel
        if y < -139:
            y = -139
        if y > 0:
            y = 0

    if x == -780 or x == 0:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            link_x -= vel
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            link_x += vel
        if link_x < 0:
            link_x = 0
        if link_x > 484:
            link_x = 484
    if y == -139 or y == 0:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            link_y -= vel
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            link_y += vel
        if link_y < 0:
            link_y = 0
        if link_y > 484:
            link_y = 484

    if x == 0 and link_x > 232:
        link_x = 232
    if y == 0 and link_y > 232:
        link_y = 232
    if x == -780 and link_x < 232:
        link_x = 232
    if y == -139 and link_y < 232:
        link_y = 232

    redrawGameWindow()
