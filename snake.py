import pygame

class Snake:
    """Defines the snake object."""

    def __init__(self, game_obj):
        """Initialize the maze frame."""
        self.screen = game_obj.screen
        self.screen_rect = game_obj.screen.get_rect()
        
        # Create head
        self.h_image = pygame.image.load('images/head.png')
        self.h_rect = self.h_image.get_rect()

        # Create neck
        self.n_image = pygame.image.load('images/neck.png')
        self.n_rect = self.n_image.get_rect()

        # Create body segment 1
        self.b1_image = pygame.image.load('images/body1.png')
        self.b1_rect = self.b1_image.get_rect()

        # Create body segment 2
        self.b2_image = pygame.image.load('images/body2.png')
        self.b2_rect = self.b2_image.get_rect()
        
        # Start snake at the center of the screen.
        self.h_rect.center = self.screen_rect.center
        self.n_rect.center = ((self.h_rect.center[0], self.h_rect.center[1] + 8))
        self.b1_rect.center = ((self.n_rect.center[0], self.n_rect.center[1] + 8))
        self.b2_rect.center = ((self.b1_rect.center[0], self.b1_rect.center[1] + 8))
        # Default body
        self.body = [self.h_rect.center,
                self.n_rect.center,
                self.b1_rect.center,
                self.b2_rect.center,
                self.b1_rect.center,
                self.b2_rect.center]

        # Define border limits for snake movement.
        border_width = 372
        border_height = 225
        self.left_border = self.h_rect.center[0] - border_width + 1
        self.right_border = self.h_rect.center[0] + border_width
        self.top_border = self.h_rect.center[1] - border_height - 15
        self.bottom_border = self.h_rect.center[1] + border_height - 25

        # Movement parameters
        #self.move = 0
        self.speed = 2
        self.p_angle = 90
        self.n_angle = self.p_angle - 90

        self.up = True
        self.right = False
        self.left = False
        self.down = False

    def update_pos(self):
        """Implement snake's continuous movement."""
        if self.up and self.h_rect.top > self.top_border:
            self.h_rect.y -= self.speed
        elif self.left and self.h_rect.left > self.left_border:
            self.h_rect.x -= self.speed
        elif self.right and self.h_rect.right < self.right_border:
            self.h_rect.x += self.speed
        elif self.down and self.h_rect.bottom < self.bottom_border:
            self.h_rect.y += self.speed

    def blitme(self):
        """Draw the maze."""
        self.screen.blit(self.h_image, self.h_rect)
        self.screen.blit(self.n_image, self.n_rect)
        self.screen.blit(self.b1_image, self.b1_rect)
        self.screen.blit(self.b2_image, self.b2_rect)
