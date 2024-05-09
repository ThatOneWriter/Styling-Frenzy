import pygame
from background import Background

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1030


size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("")

r = 209
g = 237
b = 242

bg = pygame.image.load("blue-background.jpg")
run = True

while run:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((r, g, b))
    screen.blit(bg, (210, 100))

    pygame.display.update()


pygame.quit()
