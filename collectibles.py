import pygame
import random
from settings import Settings

class Rings():
    
    def __init__(self,image_path, x ,y):

        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()        
        self.rect.y = y
        self.rect.x = x
        self.settings = Settings()
        self.corrupted = False

        #self.hitbox = (self.rect.x, self.rect.y)
        self.value = 1
        
    
        
    def createRings(self):
        # Load images of collectibles    
        self.ringList = []
        # Creates ring to list every 5 loops
        if self.settings.count % 5 == 0 :
            y_cor = random.randrange(500,650)
            ringChoice = random.randint(0,10)
            if ringChoice > 3:
                r = Rings(self.image_path, self.rect.x, y_cor)
                self.ringList.append(r)
            else: 
                r = Corrupted(self.settings.corrupted, self.rect.x, y_cor)
                
                self.ringList.append(r)
            return self.ringList

class Corrupted(Rings):
    def __init__(self, image_path, x ,y, corrupted = True):
        Rings.__init__(self, image_path, x, y)
        
        
        self.corrupted = corrupted

        