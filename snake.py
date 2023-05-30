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
        border_width = 375
        border_height = 226
        #screen_middle = (self.screen_rect.left + self.screen_rect.right) / 2
        self.left_border = self.rect.center[0] - border_width
        self.right_border = self.rect.center[0] + border_width

        self.m = 10
        self.m_right = False
        self.m_left = False
        self.m_up = False
        self.m_down = False

    def update_pos(self):
        """Update snake's position in response to movement."""
        if self.m_right and self.rect.right < self.right_border:
            self.rect.x += self.m
        if self.m_left:
            self.rect.x -= self.m
        if self.m_up:
            self.rect.y -= self.m
        if self.m_down:
            self.rect.y += self.m

    def blitme(self):
        """Draw the maze."""
        self.screen.blit(self.image, self.rect)
