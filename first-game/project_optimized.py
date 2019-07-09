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
        self.velocity = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self,win):
        if self.walkCount +1 >= 27:
            self.walkCount = 0
        if not self.standing:
            if man.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif man.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else :
            if self.right:
                win.blit(walkRight[0], (self.x,self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

class projectile(object):
    def __init__(self,x,y,radius,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (0,0,0)
        self.facing = facing
        self.velocity = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.blit(bg,(0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

# MAIN LOOP
run = True
man = player(300,420,64,64)
bullets = []
while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < screen["width"] and bullet.x > 0:
            bullet.x += bullet.velocity
        else :
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(man.x+man.width//2), round(man.y+man.height//2), 6, facing))

    if keys[pygame.K_LEFT] and man.x >= man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x <= screen["width"] - man.width - man.velocity:
        man.x += man.velocity
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

############

    if not man.isJump :
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
            man.y -= (man.jumpCount ** 2) *0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
