import pygame
from button import Button
from background import Background


pygame.init()
font = pygame.font.Font('Arial', 24)
timer = pygame.time.Clock()
message = "Ready to play?"
t = font.render('', True, 'white')
count = 0
sp = 3
done = False
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1030


size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Styling Frenzy")


r = 209
g = 237
b = 242


click_button = Button("click", 430, 470)

bg = Background(210, 120)


run = True

while run:
    screen.fill((r, g, b))
    timer.tick(60)
    if count < sp * len(message):
        count += 1

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.blit(click_button.image, click_button.rect)
    screen.blit(bg.image, bg.rect)
    pygame.display.update()


pygame.quit()
