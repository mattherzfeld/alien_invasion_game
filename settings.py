
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initalize the game's settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0 #Slightly faster than the ship
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60) #Dark gray color bullets
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1