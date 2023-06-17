import sys
import pygame

# ********************************************************************************
# ********************************** MAIN CLASS **********************************
class HummerGame: 
    """overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings() # instance of setting and assign it to self.settings

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_hight))
        pygame.display.set_caption("Hummer Game")

        self.hummer = Hummer(self) 

    def run_game(self):
        """Start the main loop of the game """
        while True:
            self._check_events()
            self.hummer.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.hummer.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.hummer.moving_left = True
        if event.key == pygame.K_UP:
            self.hummer.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.hummer.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """respond to key releases"""
        if event.key == pygame.K_RIGHT:
             self.hummer.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.hummer.moving_left = False 
        if event.key == pygame.K_UP:
            self.hummer.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.hummer.moving_down = False 

    def _update_screen(self):
        # Redraw the screen druing each pass throught the loop 
        self.screen.fill(self.settings.bg_color)
        self.hummer.blitme() # hummer appears on top of background 

        # make the most recently drawn screen visible 
        pygame.display.flip()    
                  

# ************************************************************************************
# ********************************** SETTINGS CLASS **********************************
class Settings: 
    """A class to store all settings for hummer"""
    def __init__(self):
        """Initilize the game's settings"""
        # screen setting 
        self.screen_width = 1200
        self.screen_hight = 800
        self.bg_color = (230, 230, 230)

        # hummer speed settings 
        self.hummer_speed = 1.5

# **********************************************************************************
# ********************************** HUMMER CLASS **********************************
class Hummer:
    """A class to manage the hummer"""
    def __init__(self, hg_game):
        self.screen = hg_game.screen
        self.settings = hg_game.settings
        self.screen_rect = hg_game.screen.get_rect()

        # load the hummer image and get its rect
        self.image = pygame.image.load("hummer/images/hummer-s.png")
        self.rect = self.image.get_rect()

        #start each new hummer at the center of the screen 
        self.rect.center = self.screen_rect.center
        
        # store a decimal value for the hummer's horizontal and vertical positions. 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # movement flag 
        self.moving_right, self.moving_left = False, False
        self.moving_up, self.moving_down = False, False
    
    def update(self):
        """update the hummer position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.hummer_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.hummer_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.hummer_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.hummer_speed
        
        # update rect object from position attributes 
        self.rect.x = self.x 
        self.rect.y = self.y 

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    hg = HummerGame()
    hg.run_game()

print(pygame.__version__)

    