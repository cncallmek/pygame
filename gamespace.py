import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([500, 500])
bg = pygame.image.load('World_map.png')

pygame.display.set_caption('Incomplete')



x = 50
y = 50
width = 20
height = 30
vel = 1


def redrawGameWindow():
    global walkCount
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    pygame.display.update()
    pygame.time.Clock().tick(165)


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]: x -= vel
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: x += vel
    if keys[pygame.K_UP] or keys[pygame.K_w]: y -= vel
    if keys[pygame.K_DOWN] or keys[pygame.K_s]: y += vel
    if x < 0: x = 0
    if x > (500 - width): x = (500 - width)
    if y < 0: y = 0
    if y > (500 - height): y = (500 - height)

    redrawGameWindow()
