import sys
import pygame
import math
import random
from zanikChar import Zanik
from settings import Settings
from collectibles import Rings
import time


class ZanikGame:
    # Class to manage game assets and behaviour.
    def __init__(self):
        # Initialize game and create resources.
         
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        
        # Font for texts
        self.myfont = pygame.font.SysFont("monospace", 32)
        
        # Set title for window
        pygame.display.set_caption("Zanik and the lost rings")
        
        # Get background image and adjust it to display
        self.bg_img = pygame.image.load("assets/bg.png")
        self.bg_width = self.bg_img.get_width()
        self.bg = pygame.transform.scale(self.bg_img, (self.bg_width, self.settings.height))
             
        # Count display "tiles" for scrolling the back
        self.tiles = math.ceil((self.settings.width/self.bg_width)+2)
        # Initialize assets
        self.zanik = Zanik(self)
        self.rings = Rings()
        self.ringCount = self.rings.createRings()
        


        
    def run_game(self):
        # Start main loop for game

        while True:
            
            # Keep track of user input
            self.__check_events()
            
            # Make character response to keys
            self.zanik.move()
            
            # Update ring movement
            self._update_rings()
            
            # Update display
            self._update_screen()
            
            self.settings.count += 1
                   
            
    # Function to track user input
    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    
    def _check_keydown_events(self, event):
        # Respond to keypresses
        # Moves character up
        if event.key == pygame.K_UP:
            self.zanik.moving_up = True
        # Moves character down                        
        if  event.key == pygame.K_DOWN:
            self.zanik.moving_down = True            
        # Move character right
        if event.key == pygame.K_RIGHT:
            self.zanik.moving_right = True    
        # Move character left
        if event.key == pygame.K_LEFT:
            self.zanik.moving_left = True
            pygame.transform.flip(self.zanik.image, True, False)
        if event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        # Respond to key release
        
        if event.key == pygame.K_UP:
            self.zanik.moving_up = False
                
        if  event.key == pygame.K_DOWN:
            self.zanik.moving_down = False
            
        if event.key == pygame.K_RIGHT:
            self.zanik.moving_right = False

        if event.key == pygame.K_LEFT:
            self.zanik.moving_left = False

    def _update_screen(self):
        
        # Make endless background            
        # Scroll through the tiles in the background and create infinite loop
        for i in range (self.tiles):
            self.screen.blit(self.bg, (i * self.bg_width + self.settings.scroll - self.bg_width, 0 ))
            
        if abs(self.settings.scroll) > self.bg_width:
           self.settings.scroll = 0
        self.settings.scroll -= 0.35
        
        # Create player
        self.zanik.blitme()
        
        # Display score
        self.scoreText()
        
        # Check if ringlist is empty
        if len(self.ringCount) == 0:
            self.ringCount = self.rings.createRings()
            
        # Creates rings from the ring list        
        for i in range(len(self.rings.ringList)):
            self.screen.blit(self.rings.ringList[i].image, [self.rings.ringList[i].rect.x, self.rings.ringList[i].rect.y])

        
        
        # Update screen to display new background
        pygame.display.update()

    # Create movement for rings      
    def _update_rings(self):
        for r in self.rings.ringList:
                r.rect.x -= r.settings.ring_speed
                
                if r.rect.x == 0:
                    self.rings.ringList.pop()
                # On char collision point is added to the scoreboard
                elif r.rect.x in range(self.zanik.rect.x, self.zanik.rect.x + 50):
                    if r.rect.y in range(self.zanik.rect.y, self.zanik.rect.y +100):
                        self.rings.ringList.pop()
                        # Adds rings value to score when ring is collected  
                        self.settings.score += r.value
                                   
    def scoreText(self):
       text = self.myfont.render("Score: " +str(self.settings.score),1, (0, 0, 0))
       self.screen.blit(text,(5,10))
    

if __name__ == '__main__':
    zg = ZanikGame()
    zg.run_game()