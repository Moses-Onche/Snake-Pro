import pygame
from food import Food
from random import randrange

class Snake:
    """Defines the snake object."""

    def __init__(self, game_obj):
        """Initialize the maze frame."""
        self.screen = game_obj.screen
        self.screen_rect = game_obj.screen.get_rect()
        self.food = Food(self)
        
        # Create head
        self.h_image = pygame.image.load('images/head.png')
        self.snake1 = pygame.transform.rotate(self.h_image, 0)
        self.h_rect = self.h_image.get_rect()
        
        # Start snake at the center of the screen.
        self.h_rect.center = self.screen_rect.center

        # Define border limits for snake movement.
        border_width = 372
        border_height = 225
        self.left_border = self.h_rect.center[0] - border_width + 1
        self.right_border = self.h_rect.center[0] + border_width
        self.top_border = self.h_rect.center[1] - border_height - 15
        self.bottom_border = self.h_rect.center[1] + border_height - 25

        # Movement parameters
        self.speed = 10
        self.p_angle = 0
        self.move = "U"
        self.dir = self.move
        self.position = (0, 0)

    def update_pos(self):
        """Implement snake's continuous movement."""
        # Check if two opposite directions are not keyed in then assign direction.
        # For loop applies changes to each body segment sequentially.
        self.n_rect = self.h_rect
        #self.b1_rect = self.n_rect
        #self.b2_rect = self.b1_rect
        if self.move == "U" and self.dir != "D":
            self.dir = "U"
            self.snake1 = pygame.transform.rotate(self.h_image, self.p_angle)
            if self.h_rect.top > self.top_border:
                self.h_rect.y -= self.speed
        if self.move == "L" and self.dir != "R":
            self.dir = "L"
            self.snake1 = pygame.transform.rotate(self.h_image, self.p_angle)
            if self.h_rect.left > self.left_border:
                self.h_rect.x -= self.speed
        if self.move == "R" and self.dir != "L":
            self.dir = "R"
            self.snake1 = pygame.transform.rotate(self.h_image, self.p_angle)
            if self.h_rect.right < self.right_border:
                self.h_rect.x += self.speed
        if self.move == "D" and self.dir != "U":
            self.dir = "D"
            self.snake1 = pygame.transform.rotate(self.h_image, self.p_angle)
            if self.h_rect.bottom < self.bottom_border:
                self.h_rect.y += self.speed

    def blit(self):
        """Draw the maze."""
        self.screen.blit(self.snake1, self.h_rect)
