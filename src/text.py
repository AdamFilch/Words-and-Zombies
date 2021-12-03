import arcade

# Used to display the letters when user types 
class textBox(arcade.Sprite):
    """ Text box class """

    def __init__(self, GAME_CONFIG, letter, index):


        # Initializes the game configs
        self.SCREEN_WIDTH = GAME_CONFIG["general_settings"]['screen_width']
        self.SCREEN_HEIGHT = GAME_CONFIG["general_settings"]["screen_height"]
        # font?



        


