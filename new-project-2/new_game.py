import pygame
pygame.init()

screen = {"width":480, "height":270}
win = pygame.display.set_mode((screen["width"], screen["height"]))
pygame.display.set_caption("MONOPOD MANIA")
clock = pygame.time.Clock()

#LOADING IMAGES
goRight = pygame.image.load('images/base-right.png')
goLeft = pygame.image.load('images/base.png')
char = pygame.image.load('images/base.png')
bg = pygame.image.load('images/bg.jpg')
jumping = pygame.image.load('images/base3.png')

class player(object):

    def __init__(self, x, y, width, height):
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
        self.standing = True

    def draw(self, win):
        if self.walkCount +1 >= 27:
            self.walkCount = 0
        if not self.standing:
            if self.isJump:
                win.blit(jumping, (self.x, self.y))
                self.walkCount = 0
            elif self.left:
                win.blit(goLeft, (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(goRight, (self.x, self.y))
                self.walkCount += 1
        else:
            win.blit(char, (self.x,  self.y))

def redrawGameWindow():
    win.blit(bg, (0,0))
    robot.draw(win)
    pygame.display.update()


#MAIN LOOP
run = True
robot = player(300,200,64,64)
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and robot.x >= robot.vel:
        robot.x -= robot.vel
        robot.left = True
        robot.right = False
        robot.standing = False
    elif keys[pygame.K_RIGHT] and robot.x <= screen["width"] - robot.width - robot.vel:
        robot.x += robot.vel
        robot.left = False
        robot.right = True
        robot.standing = False
    else:
        robot.left = False
        robot.right = False
        robot.standing = True
        robot.walkCount = 0

    if not robot.isJump:
        if keys[pygame.K_UP]:
            robot.isJump = True
            robot.right = False
            robot.left = False
            robot.standing = False
            robot.walkCount = 0
    else:
        if robot.jumpCount >= -10:
            neg = 1
            if robot.jumpCount < 0:
                neg = -1
            robot.y -= (robot.jumpCount ** 2) *0.5 * neg
            robot.jumpCount -= 1
        else:
            robot.isJump = False
            robot.jumpCount = 10

    redrawGameWindow()

pygame.quit()
