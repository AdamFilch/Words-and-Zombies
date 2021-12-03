import arcade

# Used to position the bullet counter automatically
class BulletCount(arcade.Sprite):
    """ Bullet count class """

    def __init__(self, GAME_CONFIG, current_bullet_count, bullet_color, bullet_location=0):

        # Initializes the config options
        self.SCREEN_WIDTH = GAME_CONFIG["general_settings"]['screen_width']
        self.SCREEN_HEIGHT = GAME_CONFIG["general_settings"]["screen_height"]
        self.STARTING_BULLET_COUNT = GAME_CONFIG["general_settings"]["starting_bullet_count"]
        self.BLUE_BULLET = GAME_CONFIG["assets_path"]["images"]["bulletcount"]["blue_bullet"]
        self.BLACK_BULLET = GAME_CONFIG["assets_path"]["images"]["bulletcount"]["black_bullet"]
        self.BC_SPRITE_SCALE = GAME_CONFIG["general_settings"]["bc_sprite_scale"]
       
        # When function is called it already chooses which bullet. this is just to simplify things
        self.bullet_color = self.BLUE_BULLET
        if(bullet_color == "black"):
            self.bullet_color = self.BLACK_BULLET

        super().__init__(self.bullet_color, self.BC_SPRITE_SCALE/5)

        # Automatically postition the bullet according to the previous
        self.bullet_count = bullet_location
        self.center_x = self.SCREEN_WIDTH * 0.05
        self.center_y = (self.SCREEN_HEIGHT * 0.1) + (self.bullet_count * self.SCREEN_HEIGHT * 0.085)

