import pygame
import random
from settings import Settings

class Rings():
    
    def __init__(self):
        # Get settings
        self.settings = Settings()
        
        # Loads image
        self.image_path = self.settings.img_path
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()        
        self.rect.x = self.settings.width
        
        # Sets random spawn height
        self.rect.y = random.randrange(500,650)     
        self.value = 1
        
    
        
    def createRings(self):
        self.ringList = []
        # Creates ring to list every 5 loops
        if self.settings.count % 5 == 0 :
            ringChoice = random.randint(0,10)
            if ringChoice > 3:
                r = Rings()
                self.ringList.append(r)
            else: 
                r = Corrupted()
                self.ringList.append(r)
            return self.ringList


class Corrupted(Rings):
    def __init__(self):
        Rings.__init__(self)
        self.image_path = self.settings.corrupted
        self.image = pygame.image.load(self.image_path)
        self.value = -1

        