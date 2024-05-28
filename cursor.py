import pygame


class Cursor:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.transform.scale(pygame.image.load("start_button.png"), (30, 30))
