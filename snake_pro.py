#!/usr/bin/python3

import pygame
from settings import Settings
import sys

class SnakePro:
    """Main class to call functions and execute all mechanics."""
    def __init__(self):
        """Initialize game components"""
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings = Settings()
        pygame.display.set_caption("Snake Pro")

    def game_run(self):
        """Run function to execute all game loops."""
        while True:
            self.game_events()

            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

    def game_events(self):
        """Respond to mouse and keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    """Main game instance."""
    sp_main = SnakePro()
    sp_main.game_run()
