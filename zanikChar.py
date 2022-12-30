import pygame

class Zanik():
    # Class to manage character
    
    def __init__(self,zg_game):
        # Create  screen
        self.screen = zg_game.screen
        self.screen_rect = zg_game.screen.get_rect()
        self.settings = zg_game.settings
        
        # Load image of character
        self.image = pygame.image.load("assets/zanikSprite.bmp")
        self.rect = self.image.get_rect()
        
        # Movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.idle_left = True

        
        # Get image size
        self.size = self.image.get_size()
        # Create a 10x smaller image than self.image
        #self.smaller_img = pygame.transform.scale(self.image, (int(self.size[0]/10), int(self.size[1]/10)))
        self.rect.y = 550 # Move in y axis
        self.rect.x = 500 # Move in x axis
        self.frame = 0 # Count frames
        
        # Char positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.hitbox = (self.x + 10, self.y + 20)
        
        
    def blitme(self):
        # Draw char at location x = 50 , y = 550
        self.screen.blit(self.image,  [self.rect.x, self.rect.y])
        
    def move(self):
        # Move the player up
        if self.moving_up and self.rect.y > 500:
            self.y -= self.settings.char_speed
        # Move the player down
        if self.moving_down and self.rect.y < 600:
            self.y += self.settings.char_speed
        # Move the player right   
        if self.moving_right and self.rect.x < 1000:
            self.x += self.settings.char_speed
        # Move the player left   
        if self.moving_left and self.rect.x > 0:
            self.x -= self.settings.char_speed
        
        if self.idle_left and self.rect.x > 0:
            self.x -= self.settings.idle_speed
            
        self.rect.x = self.x
        self.rect.y = self.y
