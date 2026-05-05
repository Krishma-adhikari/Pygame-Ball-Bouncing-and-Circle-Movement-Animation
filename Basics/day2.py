#Jumping and Boudaries
import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
run = True
x = 50
y = 70
vel = 7
radius = 30
isJump = False
jumpCount = 10
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < 500-radius:
         x+=vel
    if keys[pygame.K_LEFT]and x > radius:
         x-=vel
    if not(isJump):
        if keys[pygame.K_DOWN] and y < 500-radius-vel:
          y += vel
        if keys[pygame.K_UP] and y > radius:
         y-=vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount>=-10:
            neg = 1
            if(jumpCount<0):
                neg = -1
            y-=(jumpCount ** 2)*0.5*neg
            jumpCount-=1
        else:
            isJump = False
            jumpCount = 10
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(125,125,0),(x,y),radius)
    pygame.display.update()
pygame.quit
