import pygame
pygame.init()

screen = {"width": 500, "height" : 480}
win = pygame.display.set_mode((screen["width"], screen["height"]))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

# LOADING IMAGES
walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
bg = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self,win):
        if self.walkCount +1 >= 27:
            self.walkCount = 0
        if left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.))
            self.walkCount += 1
        else :
            win.blit(char, (self.x,self.y))

def redrawGameWindow():self.
    win.blit(bg,(0,0))
    man.draw(win)
    pygame.display.update()

# MAIN LOOP
run = True
man = player(300,420,64,64)
while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x >= velocity:
        man.x -= man.velocity
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and man.x <= screen["width"] - width - velocity:
        man.x += man.velocity
        man.left = False
        man.right = True
    else:
        man.left = False
        man.right = False
        man.walkCount = 0
    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0 :
                neg = -1
            y -= (man.jumpCount ** 2) *0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
