import pygame

class Snake:
    """Defines the snake object."""

    def __init__(self, game_obj):
        """Initialize the maze frame."""
        self.screen = game_obj.screen
        self.screen_rect = game_obj.screen.get_rect()
        
        # Create head
        self.h_image = pygame.image.load('images/head.png')
        self.snake1 = pygame.transform.rotate(self.h_image, 0)
        self.h_rect = self.h_image.get_rect()

        # Create neck
        self.n_image = pygame.image.load('images/neck.png')
        self.snake2 = pygame.transform.rotate(self.n_image, 0)
        self.n_rect = self.n_image.get_rect()

        # Create body segment 1
        self.b1_image = pygame.image.load('images/body1.png')
        self.snake3 = pygame.transform.rotate(self.b1_image, 0)
        self.b1_rect = self.b1_image.get_rect()

        # Create body segment 2
        self.b2_image = pygame.image.load('images/body2.png')
        self.snake4 = pygame.transform.rotate(self.b2_image, 0)
        self.b2_rect = self.b2_image.get_rect()
        
        # Start snake at the center of the screen.
        self.h_rect.center = self.screen_rect.center
        self.n_rect.center = ((self.h_rect.center[0], self.h_rect.center[1] + 15))
        self.b1_rect.center = ((self.n_rect.center[0], self.n_rect.center[1] + 15))
        self.b2_rect.center = ((self.b1_rect.center[0], self.b1_rect.center[1] + 15))

        # Image list for rotation
        self.seg = [[self.snake1, self.h_rect],
                [self.snake2, self.n_rect],
                [self.snake3, self.b1_rect],
                [self.snake4, self.b2_rect]
                ]

        # Define border limits for snake movement.
        border_width = 372
        border_height = 225
        self.left_border = self.h_rect.center[0] - border_width + 1
        self.right_border = self.h_rect.center[0] + border_width
        self.top_border = self.h_rect.center[1] - border_height - 15
        self.bottom_border = self.h_rect.center[1] + border_height - 25

        # Movement parameters
        self.speed = 5
        self.p_angle = 0
        self.move = "U"
        self.dir = self.move

    def update_pos(self):
        """Implement snake's continuous movement."""
        # Check if two opposite directions are not keyed in then assign direction.
        # For loop applies changes to each body segment sequentially.
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

        """
        for seg in self.seg:
            if self.move == "U" and self.dir != "D":
                self.dir = "U"
                pygame.transform.rotate(seg[0], self.p_angle)
                if seg[1].top > self.top_border:
                    seg[1].y -= self.speed
            if self.move == "L" and self.dir != "R":
                self.dir = "L"
                pygame.transform.rotate(seg[0], self.p_angle)
                if seg[1].left > self.left_border:
                    seg[1].x -= self.speed
            if self.move == "R" and self.dir != "L":
                self.dir = "R"
                pygame.transform.rotate(seg[0], self.p_angle)
                if seg[1].right < self.right_border:
                    seg[1].x += self.speed
            if self.move == "D" and self.dir != "U":
                self.dir = "D"
                pygame.transform.rotate(seg[0], self.p_angle)
                if seg[1].bottom < self.bottom_border:
                    seg[1].y += self.speed
        """

    def blitme(self):
        """Draw the maze."""
        self.screen.blit(self.snake1, self.h_rect)
"""
    def blitme(self):
        Draw the maze.
        for seg in self.seg:
            self.screen.blit(seg[0], seg[1])
"""
