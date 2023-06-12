import sys
import pygame

class HummerGame: 
    """overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings() # instance of setting and assign it to self.settings

        # self.screen = pygame.display.set_mode((1200, 800))
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_hight))
        pygame.display.set_caption("Rocket")

        self.hummer = Hummer(self) 

        # set the background color of the game 
        # self.bg_color = (230, 230, 230)
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """Start the main loop of the game """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.hummer.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.hummer.moving_left = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.hummer.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.hummer.moving_left = False

                # Redraw the screen druing each pass throught the loop 
                self.screen.fill(self.bg_color)
                self.hummer.blitme() # hummer appears on top of background 
                
            # make the most recently drawn screen visible 
            pygame.display.flip()   

class Settings: 
    """A class to store all settings for rocket"""
    def __init__(self):
        """Initilize the game's settings"""
        # screen setting 
        self.screen_width = 1200
        self.screen_hight = 800
        self.bg_color = (230, 230, 230)

class Hummer:
    """A class to manage the hummer"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship 
        self.image = pygame.image.load("hummer/images/hummer-s.png")
        self.rect = self.image.get_rect()

        #start each new ship at the bottom of the screen 
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag 
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """update the hummer position based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = HummerGame()
    ai.run_game()

print(pygame.__version__)

    