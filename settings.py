class Settings:
    # Settings for game.
    
    def __init__(self):
        # Game settings
        
        # Display settings
        self.height = 800
        self.width = 1200
        
        # Background scroll speed
        self.scroll = 0       
        
        # Char speed 
        self.char_speed = 0.75
        self.idle_speed = 0.35
        
        # Score
        self.score = 0
        
        # Ring settings
        self.img_path = "assets/ring1.bmp"
        self.corrupted = "assets/corrupted_ring.bmp"
        self.ring_speed = 0.15
       
        # Set loop count
        self.count = 0