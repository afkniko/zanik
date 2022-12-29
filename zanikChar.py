import pygame

class Zanik():
    # Class to manage character
    
    def __init__(self,zg_game):
        # Create ship and its starting position
        self.screen = zg_game.screen
        self.screen_rect = zg_game.screen.get_rect()
        
        # Load image of character
        self.image = pygame.image.load("assets/zanikSprite.bmp")
        self.rect = self.image.get_rect()
        
        # Movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
       
        # Get image size
        self.size = self.image.get_size()
        # Create a 5x smaller image than self.image
        self.smaller_img = pygame.transform.scale(self.image, (int(self.size[0]/10), int(self.size[1]/10)))
        self.rect.y = 550 # Move in y axis
        self.rect.x = 500 # Move in x axis
        self.frame = 0 # Count frames
        
        
        
    def blitme(self):
        # Draw char at location x = 50 , y = 550
        self.screen.blit(self.smaller_img,  [self.rect.x, self.rect.y])
        
    def move(self):
        # Move the player up
        if self.moving_up and self.rect.y > 500:
            self.rect.y -= 1
        # Move the player down
        if self.moving_down and self.rect.y < 600:
            self.rect.y += 1
        # Move the player right   
        if self.moving_right and self.rect.x < 1000:
            self.rect.x += 1
        # Move the player left   
        if self.moving_left and self.rect.x > 0:
            self.rect.x -= 1