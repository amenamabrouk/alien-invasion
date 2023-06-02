import sys
import pygame
from blue_boy import BlueBoy

class BlueSky:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("blue sky")
        self.blue_blue = BlueBoy(self)
        self.bg_color = (53, 127, 238)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.blue_blue.blitime()
            pygame.display.flip()

if __name__ == '__main__':
    ai = BlueSky()
    ai.run_game()


  


