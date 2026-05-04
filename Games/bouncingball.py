import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((500,500))
x = 100
y = 100
dx = -1
dy = 2
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    screen.fill((0,0,0))

    pygame.draw.circle(screen,(250,250,0),(x,y),20)
    x += dx
    y += dy
    if x <= 20 or x >= 480:
        dx = -dx
    if y <= 20 or y >= 480:
        dy = -dy
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
