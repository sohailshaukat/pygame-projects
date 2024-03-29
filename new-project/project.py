import pygame
pygame.init()

screen = {"width": 1024, "height": 1024}

win = pygame.display.set_mode((screen["width"], screen["height"]))

pygame.display.set_caption("Trial Test")

#LOADING IMAGES

walkRight = [pygame.image.load('images\pixil-frame-right-1.png'),pygame.image.load('images\pixil-frame-right-2.png'),pygame.image.load('images\pixil-frame-right-3.png'),pygame.image.load('images\pixil-frame-right-4.png'),pygame.image.load('images\pixil-frame-right-5.png'),pygame.image.load('images\pixil-frame-right-6.png')]
walkLeft = [pygame.image.load('images\pixil-frame-left-1.png'),pygame.image.load('images\pixil-frame-left-2.png'),pygame.image.load('images\pixil-frame-left-3.png'),pygame.image.load('images\pixil-frame-left-4.png'),pygame.image.load('images\pixil-frame-left-5.png'),pygame.image.load('images\pixil-frame-left-6.png')]
standing = pygame.image.load('images/trial-1-standing.png')
jumping = pygame.image.load('images/trial-1-jumping.png')
bg = pygame.image.load('images/bg.jpg')


# ATTRIBUTES
clock = pygame.time.Clock()
x = 0
y = 420
height = 64
width = 64
velocity = 10

isJump = False
jumpCount = 10

left =False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg,(0,0))
    if walkCount +1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount%6], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount%6], (x,y))
        walkCount += 1
    else :
        win.blit(standing, (x,y))
    pygame.display.update()

run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >= velocity:
        x -= velocity
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x <= screen["width"] - width - velocity:
        x += velocity
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0
    if not isJump:
        if keys[pygame.K_UP]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0 :
                neg = -1
            y -= (jumpCount ** 2) *0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()

pygame.quit()
