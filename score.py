import pygame

class Score:
    """Handle the score count."""
    
    def __init__(self, game_obj):
        """Initialize default parameters for score display."""
        self.screen = game_obj.screen

        self.player_score = 0
        #self.font = pygame.font.SysFont('nimbussans', 15)
        #self.color = (243, 254, 188)

        #self.score = font.render('Score: ' + str(self.player_score), True, color)
        #self.score_rect = self.score.get_rect()
        #self.score_rect.center = ((600, 117))

    def blit(self):
        self.font = pygame.font.SysFont('nimbussans', 15)
        self.color = (243, 254, 188)

        self.score = self.font.render('Score: ' + str(self.player_score), True, self.color)
        self.score_rect = self.score.get_rect()
        self.score_rect.center = ((600, 117))

        self.screen.blit(self.score, self.score_rect)
