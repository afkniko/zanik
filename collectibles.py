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

        #self.hitbox = (self.rect.x, self.rect.y)
        self.value = 1
        
        
        
    def createRings(self):
        # Load images of collectibles    
        self.ringList = []
        if self.settings.count % 5 == 0 :
            y_cor = random.randrange(500,650)
            r = Rings(self.image_path, self.rect.x, y_cor)
            self.ringList.append(r)
            return self.ringList

