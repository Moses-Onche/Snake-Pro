#!/usr/bin/python3

import pygame

class Maze:
    """Defines all the elements of the stage Maze."""

    def __init__(self, game_obj):
        """Initialize the maze and border parameters."""
        self.screen = game_obj.screen
        self.screen_rect = game_obj.screen.get_rect()

        self.image = pygame.image.load('images/border.png')
        self.rect = self.image.get_rect()

        # Place border in the center of the screen
        self.rect.center = self.screen_rect.center

    def blit(self):
        """Draw the border."""
        self.screen.blit(self.image, self.rect)
