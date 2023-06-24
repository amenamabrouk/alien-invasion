
class Settings:

    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5 

        # Bullet settings,  
        self.bullet_speed = 1.0 # bullet will travel slightly slower than the ship 
        self.bullet_width = 3 # creates a dark gray bullets with a width of 3 pixels
        self.bullet_height = 15 # and a hight of 15 pixels 
        self.bullet_color = (60, 60, 60)