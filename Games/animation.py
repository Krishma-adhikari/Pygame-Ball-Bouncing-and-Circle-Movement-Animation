import pygame
import time

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
x = 0
running = True
while running:
  screen.fill((250, 250, 250))
  pygame.draw.circle(screen, (255, 0, 0), (x, 250), 20)
  x = x + 1
  clock.tick(60)
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
pygame.quit()
