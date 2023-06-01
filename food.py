import pygame
from random import randrange

class Food:
    """Defines the food class."""

    def __init__(self, game_obj):
        self.screen =  game_obj.screen
        self.screen_rect = self.screen.get_rect()

        self.f_image = pygame.image.load('images/food.png')
        self.f_rect = self.f_image.get_rect()

        x = randrange(350, 900)
        y = randrange(250, 500)
        self.f_rect.center = (x, y)

    def blitme(self):
        self.screen.blit(self.f_image, self.f_rect)
