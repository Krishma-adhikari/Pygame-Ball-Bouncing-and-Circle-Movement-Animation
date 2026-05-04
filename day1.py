import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("First day") # Added quotes

x = 50
y = 50
width = 45
height = 50
vel = 7

run = True
while run:
    pygame.time.delay(50) # Reduced delay for smoother movement
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    # Changed () to [] for keys
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    screen.fill((0,0,0)) 
    pygame.draw.rect(screen, (125,125,125), (x, y, width, height))
    pygame.display.update()

pygame.quit()