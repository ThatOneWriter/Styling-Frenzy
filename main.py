import pygame
from background import Background

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1030


size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("")

run = True

while run:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
