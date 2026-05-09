import pygame


pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
x = 50
y = 400
isJump = False
width = 5
height = 10
jumpCount = 10
vel = 5
run = True
wordCount = 0 #Mistakenly declared no. of walks as word count
left = False
right = False

def redrawGamewindow():
    global wordCount
    screen.blit(bg,(0,0)) 
    if wordCount+1>=27:
        wordCount = 0
    if left:
        screen.blit(walkLeft[wordCount//3],(x,y))
        wordCount += 1        
    elif right:
        screen.blit(walkRight[wordCount//3],(x,y))
        wordCount += 1  
    else:
        screen.blit(char,(x,y))   
    pygame.display.update()
while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT ] and x <500-width-vel:
        x+=vel   
        left = False
        right = True
    elif keys[pygame.K_LEFT] and x > vel:
        x-=vel
        left = True
        right = False
    else:
        left = False
        right = False
        wordCount = 0
    if not(isJump):
        
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            wordCount = 0
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
    redrawGamewindow()
pygame.quit