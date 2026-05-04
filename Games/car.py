import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
x = 40
y = 70

speed = 5
running = True
while running: 


 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   running = False

 x += speed

 tier_x1 = x + 40
 tier_y1 = y + 140
 tier_x2 = x + 100
 tier_y2 = y + 140
 if(x > 800):
  x = -140

 
 screen.fill((0, 255, 255))

 #For full body filling
 pygame.draw.polygon(screen, (255,0,0), [
    (x, y + 140),
    (x, y + 70),
    (x + 80, y + 70),
    (x + 80, y + 75),
    (x + 90, y + 100),
    (x + 120, y + 100),
    (x + 140, y + 135),
    (x + 140, y + 140),
    (x + 100, y + 140),
    (x + 90, y + 140),
    (x + 40, y + 140),
    (x, y + 140)
 ])
 pygame.draw.circle(screen,(255,0,0),(tier_x1,tier_y1),10)
 pygame.draw.circle(screen,(255,0,0),(tier_x2,tier_y2),10)





# For Boundary Filling
#  pygame.draw.line(screen,(0,0,250),(x,y+140),(x,y+70))
#  pygame.draw.line(screen,(0,0,250),(x,y+135),(x+140,y+135))
#  pygame.draw.line(screen,(0,0,250),(x+140,y+135),(x+120,y+100))
#  pygame.draw.line(screen,(0,0,250),(x+120,y+100),(x+90,y+100))
#  pygame.draw.line(screen,(0,0,250),(x+80,y+70),(x+90,y+100))
#  pygame.draw.line(screen,(0,0,250),(x,y+70),(x+80,y+70))

#  pygame.draw.circle(screen,(0,0,250),(tier_x1,tier_y1),10,3)
#  pygame.draw.circle(screen,(0,0,250),(tier_x2,tier_y2),10,3)

 pygame.display.update()
 clock.tick(50)
pygame.quit()
