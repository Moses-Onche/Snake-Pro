#!/usr/bin/python3

import pygame
import random
import sys
import time
from food import Food
from maze import Maze
from settings import Settings
from snake import Snake


class SnakePro:
    """Main class to call functions and execute all mechanics."""
    def __init__(self):
        """Initialize game components"""
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.screen = pygame.display.set_mode((1200, 800))
        self.settings = Settings()
        self.border = Maze(self)
        self.snake = Snake(self)
        self.food = Food(self)
        self.fps = pygame.time.Clock()

        pygame.display.set_caption("Snake Pro")

    def game_loop(self):
        """Run function to execute all game loops."""
        while True:         
            self.flip_screen()
            self.game_events()
            self.snake.update_pos()
            self.fps.tick(self.snake.speed)

    def game_events(self):
        """Respond to mouse and keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)
            #elif event.type == pygame.KEYUP:
                #self.keyup_events(event)

    def keydown_events(self, event):
        """Respond when a key is pressed down."""
        if event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        if event.key == pygame.K_LEFT:
            self.snake.p_angle = 90
            self.snake.move = "L"
        if event.key == pygame.K_RIGHT:
            self.snake.p_angle = -90
            self.snake.move = "R"
        if event.key == pygame.K_UP:
            self.snake.p_angle = 0
            self.snake.move = "U"
        if event.key == pygame.K_DOWN:
            self.snake.p_angle = -180
            self.snake.move = "D"

    """
    def keyup_events(self, event):
        Respond when a key is released.
        if event.key == pygame.K_LEFT:
            self.snake.left = True
        if event.key == pygame.K_RIGHT:
            self.snake.right = True
        if event.key == pygame.K_UP:
            self.snake.up = True
        if event.key == pygame.K_DOWN:
            self.snake.down = True
    """

    def flip_screen(self):
        """Flip screen as changes and events occur."""
        self.screen.fill(self.settings.bg_color)
        self.border.blitme()
        self.snake.blitme()
        self.food.blitme()
        
        pygame.display.flip()


if __name__ == "__main__":
    """Main game instance."""
    sp_main = SnakePro()
    sp_main.game_loop()
