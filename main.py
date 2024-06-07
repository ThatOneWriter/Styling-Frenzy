import pygame
import random
from button import Button
from background import Background
from cursor import Cursor
from meat import Meat

pygame.init()
font = pygame.font.SysFont('Go chi Hand', 24)
login_font = pygame.font.SysFont('Go chi Hand', 60)
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1030


size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("")

timer = pygame.time.Clock()
messages = ['~Click the start button to begin~', 'Ready to play?',
            'Are you sure?',
            'No turning back you know.',
            '.', '..', '...',
            'Alright alright, quit being so impatient..', 'Jeez, kids these days...']
t = font.render('', True, 'white')
touch_message = 0
message = messages[touch_message]
count = 0
sp = 4
done = False


r = 103
g = 68
b = 59


click_button = Button("click", 430, 470)
c = Cursor(400, 89)
bg = Background(210, 120)
m = Meat(50, 60)

run = True

while run:
    movement = pygame.mouse.get_pos()
    begin = "Welcome to: "
    display_begin = login_font.render(begin, True, (255, 255, 255))

    screen.fill((r, g, b))
    timer.tick(60)
    if count < sp * len(message):
        count += 1
    elif count >= sp * len(message):
        done = True

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user  clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if done and touch_message < len(messages):
                touch_message += 1
                done = False
                message = messages[touch_message]
                count = 0
                screen.blit(m.image, m.rect)
        if m.rect.collidepoint(movement):
            m.move(m.x + 3, m.y + 3)
            m = Meat(random.randint(15, 450), random.randint(24, 310))
    snip = font.render(message[0:count//sp], True, "white")

    screen.blit(snip, (400, 89))
    screen.blit(click_button.image, click_button.rect)
    screen.blit(bg.image, bg.rect)
    screen.blit(display_begin, (200, 45))
    screen.blit(c.image, movement)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
