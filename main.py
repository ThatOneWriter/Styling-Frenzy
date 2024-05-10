import pygame
from background import Background
from button import Button

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1030


size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Styling Frenzy")

r = 209
g = 237
b = 242

click_button = Button("click", 210, 140)
bg = Background(210, 120)
run = True

while run:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((r, g, b))
    screen.blit(click_button.image, click_button.rect)
    screen.blit(bg.image, bg.rect)
    pygame.display.update()


pygame.quit()
