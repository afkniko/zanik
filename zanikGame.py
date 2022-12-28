import sys
import pygame
import math
from zanikChar import Zanik
from settings import Settings


class ZanikGame:
    #   Class to manage game assets and behaviour.
    
    def __init__(self):
        # Initialize game and create resources.
        
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        
        #   Set title for window
        pygame.display.set_caption("Zanik and the lost rings")
        
        #   Get background image and adjust it to display
        self.bg_img = pygame.image.load("images/bg.png")
        self.bg_width = self.bg_img.get_width()
        self.bg = pygame.transform.scale(self.bg_img, (self.bg_width, self.settings.height))
             
        # Count display "tiles" for scrolling the back
        self.tiles = math.ceil((self.settings.width/self.bg_width)+2)
        # Initialize created character
        self.zanik = Zanik(self)
        
    def run_game(self):
        scroll = self.settings.scroll
        direction = 0
        # Start main loop for game
        
        while True:
            
            # Keep track of user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                #   APPLY direction when key is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = -1
                        self.zanik.control(direction)
                        #   TODO Jump on press or move 1 line up?
                        
                    if  event.key == pygame.K_DOWN:
                        direction = 1
                        self.zanik.control(direction)
                        # TODO Crouch on press or move 1 line down?
                        
                        
                #   REMOVE direction when key is released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        # TODO ??
                        continue
                    if  event.key == pygame.K_DOWN:
                        # TODO Character stands up when released
                        continue
                    
            #   Make endless background            
            #   Scroll through the tiles in the background and create infinite loop
            for i in range (self.tiles):
                self.screen.blit(self.bg, (i * self.bg_width + scroll - self.bg_width, 0 ))
                
            if abs(scroll) > self.bg_width:
                scroll = 0
            scroll -= 0.35
            
            #   Create player
            self.zanik.blitme()

            #   Update screen to display new background
            pygame.display.update()
        
    
if __name__ == '__main__':
    zg = ZanikGame()
    zg.run_game()