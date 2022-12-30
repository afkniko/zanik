import pygame
import random

class Collectibles():
    
    def __init__(self,zg_game):
        # Create  screen
        self.screen = zg_game.screen
        self.screen_rect = zg_game.screen.get_rect()
        self.settings = zg_game.settings
        
        self.x = self.settings.width
        self.y = random.randrange(500,600)
        self.hitbox = (self.x + 10, self.y + 25)
        
        
        # Load images of collectibles
        self.rings_img = [pygame.image.load("assets/ring1.bmp"), 
                        pygame.image.load("assets/ring2.bmp"), 
                        pygame.image.load("assets/ring3.bmp")]
        
        
    def createRing(self):
        ringChoice = random.choice([0,1,2])
        self.screen.blit(self.rings_img[0],  [self.x, self.y])
        
    def moveRing(self):
        self.x -= self.settings.idle_speed