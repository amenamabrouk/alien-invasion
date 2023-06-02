
import sys
import pygame
from ship import Ship
from settings import Settings

# https://devdocs.io/pygame/
class AlienInvasion:
    """Overall class to manage game assets and behaviors."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        
        # Screen is a surface where a game element can be displayed
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height ))
        pygame.display.set_caption("Alien Invation")

        # set the background color 
        self.screen.fill(self.settings.bg_color) 

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update image on the screen, and flip to the new screen"""
        # redraw the screen during each pass thought the loop 
        self.screen.fill(self.settings.bg_color)
        self.ship.blitime() # blit() -> draw one image onto another 
            
        # Make the most recently drawn screen visible 
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

print(pygame.__version__)
