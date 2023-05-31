import pygame

class Snake:
    """Defines the snake object."""

    def __init__(self, game_obj):
        """Initialize the maze frame."""
        self.screen = game_obj.screen
        self.screen_rect = game_obj.screen.get_rect()
        
        self.image = pygame.image.load('images/box.png')
        self.rect = self.image.get_rect()
        
        # Start snake at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Define border limits for snake movement.
        border_width = 372
        border_height = 225
        self.left_border = self.rect.center[0] - border_width + 1
        self.right_border = self.rect.center[0] + border_width
        self.top_border = self.rect.center[1] - border_height - 15
        self.bottom_border = self.rect.center[1] + border_height - 25

        # Movement parameters
        self.speed = 15

        """
        self.m = 10
        self.m_right = False
        self.m_left = False
        self.m_up = False
        self.m_down = False
        """

    def update_pos(self):
        """Update snake's position in response to movement."""
        if self.m_right and self.rect.right < self.right_border:
            self.rect.x += self.m
        if self.m_left and self.rect.left > self.left_border:
            self.rect.x -= self.m
        if self.m_up and self.rect.top > self.top_border:
            self.rect.y -= self.m
        if self.m_down and self.rect.bottom < self.bottom_border:
            self.rect.y += self.m

    def blitme(self):
        """Draw the maze."""
        self.screen.blit(self.image, self.rect)
