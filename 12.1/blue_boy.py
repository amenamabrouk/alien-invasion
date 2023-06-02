import pygame


class BlueBoy:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect. 
        self.image = pygame.image.load('12.1/images /boy_axe_down_1.png')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom of each screen 
        self.rect.midbottom = self.screen_rect.midbottom

    def blitime(self):
        """Draw yhe ship at its current location."""
        self.screen.blit(self.image, self.rect)
