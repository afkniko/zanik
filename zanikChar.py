import pygame

class Zanik():
    # Class to manage character
    
    def __init__(self,zg_game):
        # Create ship and its starting position
        self.screen = zg_game.screen
        self.screen_rect = zg_game.screen.get_rect()
        
        # Load image of character
        self.image = pygame.image.load("images/zanikSprite.bmp")
        self.rect = self.image.get_rect()
        
       
        # Get image size
        self.size = self.image.get_size()
        # create a 5x smaller image than self.image
        self.smaller_img = pygame.transform.scale(self.image, (int(self.size[0]/10), int(self.size[1]/10)))
        self.char_y = 550 # move in y axis
        self.char_x = 50
        self.frame = 0 # count frames
        
        
    def blitme(self):
        # Draw char at location x = 50 , y = 550
        self.screen.blit(self.smaller_img,  [self.char_x, self.char_y])
        
    def control(self,direction):
        #   Move the player down
        if self.char_y >= 550 and direction == -1:
            self.char_y -= 50
        #   Move the player up
        elif self.char_y <= 550 and direction == 1:
            self.char_y += 50