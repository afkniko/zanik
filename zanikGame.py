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
        
        
        # Start main loop for game
        while True:
            
            #   Keep track of user input
            self.__check_events()
            self._update_screen()
   
    #   Function to track user input
    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            #   APPLY direction when key is pressed
            if event.type == pygame.KEYDOWN:
                #   Moves character up
                if event.key == pygame.K_UP:
                    position = -1
                    self.zanik.control(position)
                    
                #   Moves character down                        
                if  event.key == pygame.K_DOWN:
                    position = 1
                    self.zanik.control(position)
    
    def _update_screen(self):
         
        #   Make endless background            
        #   Scroll through the tiles in the background and create infinite loop
        for i in range (self.tiles):
            self.screen.blit(self.bg, (i * self.bg_width + self.settings.scroll - self.bg_width, 0 ))
            
        if abs(self.settings.scroll) > self.bg_width:
            self.settings.scroll = 0
        self.settings.scroll -= 0.35
        
        #   Create player
        self.zanik.blitme()

        #   Update screen to display new background
        pygame.display.update()
                        
    
if __name__ == '__main__':
    zg = ZanikGame()
    zg.run_game()