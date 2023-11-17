import pygame
import sys

pygame.init()

# screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0])
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Link\'s Happy Day')

# sprites
bg = pygame.image.load('World_map.png')
walkDown = [pygame.image.load('Sprites/Link/D1.png'), pygame.image.load('Sprites/Link/D2.png')]
# walkUp = [pygame.image.load('Sprites/Link/U1.png'), pygame.image.load('Sprites/Link/U2.png')]
walkRight = [pygame.image.load('Sprites/Link/R1.png'), pygame.image.load('Sprites/Link/R2.png')]
# walkLeft = [pygame.image.load('Sprites/Link/L1.png'), pygame.image.load('Sprites/Link/L2.png')]

bg_x = 50
bg_y = 50
width = 150
height = 200
link_x = (500-width)/2
link_y = (500-height)/2
vel = 10
left = False
right = False
up = False
down = False
walkCount = 0
last_image = pygame.image.load('Sprites/Link/D1.png')


def redrawGameWindow():
    global walkCount
    global last_image
    screen.blit(bg, (bg_x, bg_y))
    # sprite animation
    if down:
        if walkCount < 15:
            screen.blit(walkDown[0], (link_x, link_y))
            last_image = walkDown[0]
            walkCount += 1
        elif 15 <= walkCount < 30:
            screen.blit(walkDown[1], (link_x, link_y))
            last_image = walkDown[1]
            walkCount += 1
        if walkCount == 30:
            walkCount = 0
    elif right:
        if walkCount < 15:
            screen.blit(walkRight[0], (link_x, link_y))
            last_image = walkRight[0]
            walkCount += 1
        elif 15 <= walkCount < 30:
            screen.blit(walkRight[1], (link_x, link_y))
            last_image = walkRight[1]
            walkCount += 1
        if walkCount == 30:
            walkCount = 0
    # elif up:
    #     if walkCount < 15:
    #         screen.blit(walkUp[0], (link_x, link_y))
    #         walkCount += 1
    #     elif 15 <= walkCount < 30:
    #         screen.blit(walkUp[1], (link_x, link_y))
    #         walkCount += 1
    #     if walkCount == 30:
    #         walkCount = 0
    # elif left:
    #     if walkCount < 15:
    #         screen.blit(walkLeft[0], (link_x, link_y))
    #         walkCount += 1
    #     elif 15 <= walkCount < 30:
    #         screen.blit(walkLeft[1], (link_x, link_y))
    #         walkCount += 1
    #     if walkCount == 30:
    #         walkCount = 0
    else:
        screen.blit(last_image, (link_x, link_y))

    pygame.display.update()
    pygame.time.Clock().tick(60)


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # camera movement
    keys = pygame.key.get_pressed()

    if link_x == (500-width)/2:
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            bg_x -= vel
            right = True
            left = False
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            bg_x += vel
            left = True
            right = False
        else:
            right, left = False, False

        if bg_x < -780:
            bg_x = -780
        if bg_x > 0:
            bg_x = 0

    if link_y == (500-height)/2:
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            bg_y -= vel
            down = True
            up = False
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            bg_y += vel
            up = True
            down = False
        else:
            up, down = False, False

        if bg_y < -139:
            bg_y = -139
        if bg_y > 0:
            bg_y = 0

    if bg_x == -780 or bg_x == 0:
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            link_x += vel
            right = True
            left = False
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            link_x -= vel
            left = True
            right = False
        else:
            right, left = False, False

        if link_x < 0:
            link_x = 0
        if link_x > 351:
            link_x = 350

    if bg_y == -139 or bg_y == 0:
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            link_y += vel
            down = True
            up = False
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            link_y -= vel
            up = True
            down = False
        else:
            up, down = False, False
        if link_y < 0:
            link_y = 0
        if link_y > 300:
            link_y = 300

    if bg_x == 0 and link_x > (500-width)/2:
        link_x = (500-width)/2
    if bg_y == 0 and link_y > (500-height)/2:
        link_y = (500-height)/2
    if bg_x == -780 and link_x < (500-width)/2:
        link_x = (500-width)/2
    if bg_y == -139 and link_y < (500-height)/2:
        link_y = (500-height)/2

    redrawGameWindow()
