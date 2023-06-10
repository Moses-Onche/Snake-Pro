import pygame
from random import randrange

class Food:
    """Defines the food class."""

    def __init__(self, game_obj):
        """Initialize the food parameters."""
        self.screen =  game_obj.screen

        self.f_image = pygame.image.load('images/food.png')
        self.f_rect = self.f_image.get_rect()
        self.f_rect.center = (randrange(350, 900), randrange(250, 500))

    def blit(self):
        """Draw the food in the window."""
        self.screen.blit(self.f_image, self.f_rect)
