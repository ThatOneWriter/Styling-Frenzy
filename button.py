import pygame


class Button:

    def __init__(self, but_ton, x, y):
        self.x = x
        self.y = y

        if but_ton == "click":
            self.image = pygame.image.load("start_button.png")
            self.image_size = self.image.get_size()
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def click_button(self):
        action = False
        position = pygame.mouse.get_pos()

