import pygame


class Cursor:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load("cursor.png"), (35, 35))
        self.image_size = self.image.get_size()








