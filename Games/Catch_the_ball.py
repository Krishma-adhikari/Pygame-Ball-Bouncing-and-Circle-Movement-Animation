import pygame
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 450))
font = pygame.font.SysFont(None, 35)

def show_score(score):
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

bucket_x = 350
bucket_y = 350
bucket_width = 200
bucket_height = 50

ball_x = random.randint(50, 450)
ball_y = 0
speed = 5

ball_list = []
score = 0

def stored_balls(ball_list):
    for block in ball_list:
        pygame.draw.circle(screen, (255, 0, 0), (block[0], block[1]), 20)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bucket_x -= 50

            if event.key == pygame.K_RIGHT:
                bucket_x += 50

    # Ball falling
    ball_y += speed

    # If ball touches bucket
    if (ball_y + 20 >= bucket_y and
        bucket_x <= ball_x <= bucket_x + bucket_width):

        ball_list.append([ball_x, bucket_y - 20])
        score += 1


        ball_x = random.randint(50, 450)
        ball_y = 0
   

    screen.fill((0, 0, 0))

   
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), 20)

    # Bucket
    pygame.draw.rect(screen, (0, 125, 125),
                     (bucket_x, bucket_y, bucket_width, bucket_height))

    # Stored balls inside bucket
    stored_balls(ball_list)

    show_score(score)

    pygame.display.update()
    clock.tick(100)

pygame.quit()
