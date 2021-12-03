import arcade
import pygame
import os
import random
from enum import Enum

from src.bc import BulletCount
from src.text import textBox
from src.zombie import WordZombie


class GameState(Enum):

    # Game states that would detemine current game location
    GAMEOVER = 0
    MENU = 1
    RUNNING = 2
    COUNTDOWN = 3


class PlayerState(Enum):

    # Player State that would determine current action
    IDLE = 6
    SHOOTING = 7
    RELOADING = 8
    HELP = 9

class myGame(arcade.Window):

    def __init__(self, GAME_CONFIG):
        """ Initiates Code """

        # Config data
        self.GAME_CONFIG = GAME_CONFIG
        self.SCREEN_WIDTH = GAME_CONFIG["general_settings"]['screen_width']
        self.SCREEN_HEIGHT = GAME_CONFIG["general_settings"]["screen_height"]
        self.SCREEN_TITLE = GAME_CONFIG["general_settings"]["screen_title"]
        self.STARTING_BULLET = GAME_CONFIG["general_settings"]["starting_bullet_count"]
        self.MAXIMUM_ZOMBIE = GAME_CONFIG["general_settings"]["maximum_zombie"]


        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)
        arcade.set_background_color(arcade.color.INDIGO)



        
        # Variables holding sprites
        self.bullet_count_list = None
        self.zombie_list = None
        self.player_list = None
        self.clair_list = None



        

        # Game Variables 
        self.lifeline = int()
        self.lives = int() 
        self.bullet = int()
        self.score = int()
        self.word = None
        self.total_time = float()
        self.zombie_count = int()
        self.countdown = int()

        self.highscore = int()

        # for bullets
        self.bullet = 9
        

        # Changes current status to MENU
        self.status = GameState.MENU


        # Changes current player status
        self.player_status = PlayerState.IDLE





    def setup(self):
        """ Restart all variables every time """

        # Game variables
        self.lives = 5
        self.bullet = 9
        self.score = 0
        self.word = []
        self.total_time = 0.0
        self.zombie_count = 0
        self.countdown = 5
        self.lastcount = pygame.time.get_ticks()

        # Game Background sprites (Not created)
        arcade.set_background_color(arcade.color.BLACK)


        # Sprite lists
        self.bullet_count_list = arcade.SpriteList()
        self.zombie_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.clair_list = arcade.SpriteList()


        # Pre loads drawings onto the screen before actual drawing process
        # Set up bullet counter pre-draw
        self.set_bullet_count()

        # Set up text box pre-draw
        # self.set_text_box()

        # set up game timer
        self.set_timer()

        # Set up player and side character pre-draw
        # Self.

        # Set up word zombie pre draw
        self.set_word_zombie()

        
          

    def draw_main_menu(self):
        """ Draws the game over screen if the game state goes MENU """


        # Displays instructions to begin
        mainMenuText = "Press ENTER to play the game"
        arcade.draw_text(mainMenuText, self.SCREEN_WIDTH//2,
                        self.SCREEN_HEIGHT//2, 
                        arcade.color.LIGHT_BLUE, 
                        24, width= self.SCREEN_WIDTH, align = "center",anchor_x="center", anchor_y="center" )

        





        



    def draw_game(self):
        """ Draws the game over screen if the game state is RUNNING """


        arcade.set_background_color(arcade.color.LIGHT_BLUE)

        # Draw the bullet counter
        self.bullet_count_list.draw()


        # Draw the letter display
        # self.set_text_box()


        # Draws zombies
        for zombie in self.zombie_list:
            self.zombie_list.draw()

        
        # Player draw
        arcade.draw_rectangle_filled(self.SCREEN_WIDTH//2 + 90, self.SCREEN_HEIGHT * 0.1, 100,300, arcade.color.BLACK)


        # Prints word 'list' boringly onto the screen
        joined = "".join(self.word)
        arcade.draw_text(joined, self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT * 0.15, arcade.color.WHITE,
                         35, width= self.SCREEN_WIDTH - 100, align = "center",anchor_x="center", anchor_y="center")


        # Draw score


        # Draw countdown
        if self.countdown > 0:
            self.set_countdown()
            


        # Draw Timer
        self.set_timer()




    def draw_gameover(self):
        """ Draws the game over screen if the game state goes GAMEOVER """
        pass
    



    def on_draw(self):
        """Draws on screen"""


        # To start rendering objects on screen
        arcade.start_render()

        # Draw main menu if the current status if MENU
        if self.status == GameState.MENU:
            self.draw_main_menu()


        # Draws the game while is running
        elif self.status == GameState.RUNNING:
            self.draw_game()

        # Draws game over screen
        else:
            self.draw_gameover()


    def on_update(self, delta_time):
        """ Zombie logic and player stuff and other logical entities """

        vel = 30

        if self.countdown > 0:
            count_timer = pygame.time.get_ticks()
            if count_timer - self.lastcount > 1000:
                self.countdown -= 1
                self.lastcount == count_timer
        

        if self.status == GameState.RUNNING and self.countdown == 0:
            for zombie in self.zombie_list:
                zombie.center_y -= vel * delta_time
                

            # Calculates time
            self.total_time += delta_time
        


    def on_key_press(self, key, key_modifiers):
        """ Any keyboard presses moves here """

        # Submit word
        if key == arcade.key.SPACE and self.bullet > 0 and self.status == GameState.RUNNING and self.countdown == 0:

            # Submitting a word attempts a word check and minus a bullet
            self.bullet -= 1

            # Every time a word is submitted checks if reload is required
            if self.bullet == 0:
                self.bullet += 9

            # Updates the bullet counter sprites
            self.set_bullet_count()

            # Resets the text array
            self.word = []


        # Condition for game restart and begin
        if key == arcade.key.ENTER and self.status == GameState.MENU or self.status == GameState.GAMEOVER:
            self.status = GameState.RUNNING
            self.setup()
            


        # Typing letters
        if key < 127 and self.status == GameState.RUNNING and key != arcade.key.SPACE and key != arcade.key.ENTER:

            # Appends the character into a list
            self.word.append(chr(key))

            print(self.word)

        if key == arcade.key.BACKSPACE and self.status == GameState.RUNNING:

            print(self.word)

            # Deletes the last element on the list if not empty otherwise its an empty list
            if len(self.word) > 0:
                self.word.pop()

            else:
                self.word = []

        if key == arcade.key.TAB and self.countdown > 0 and self.status == GameState.RUNNING:
            self.countdown -= 1





    def set_bullet_count(self):
        """ Appends the bullet counter sprites """

        remainder_bullets = self.STARTING_BULLET - self.bullet 

        # Executes bullet display function which chooses filled/not filled
        for i in range(self.bullet):
            self.bullet_count_s = BulletCount(self.GAME_CONFIG, self.bullet, "blue", i)
            self.bullet_count_list.append(self.bullet_count_s)


        # Places black bullets if there are a remainder of bullets
        if self.bullet < self.STARTING_BULLET:
            for i in range(remainder_bullets):
                x = self.bullet + i
                self.bullet_count_s = BulletCount(self.GAME_CONFIG, self.bullet, "black", x)
                self.bullet_count_list.append(self.bullet_count_s)


        print(remainder_bullets)


    # Outdated, Using the basic arcade.draw_text instead of individually displaying
    def set_text_box(self):
        """ Creates the box where user types into """

        # Only proceeds if there is something
        if self.word != None:
            for i in range(len(self.word)):
                self.letter_display = textBox(self.GAME_CONFIG, self.word[i], i)
                



            
    def set_timer(self):
        """ Makes timer calculation and draw """

        # Calculate minutes
        minutes = int(self.total_time) // 60

        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60

        # Figure out our output
        output = f"T: {minutes:02d}:{seconds:02d}"

        # Output the timer text.
        arcade.draw_text(output, self.SCREEN_WIDTH * 0.01, self.SCREEN_HEIGHT // 1.1, arcade.color.BLACK, 30)

       
    def set_countdown(self):
        arcade.draw_text("GET READY", self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2, arcade.color.BLACK,
                             35, width= self.SCREEN_WIDTH - 100, align = "center",anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.countdown), self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2 + 50, arcade.color.BLACK,
                             35, width= self.SCREEN_WIDTH - 100, align = "center",anchor_x="center", anchor_y="center")
      
    def set_word_zombie(self):
        """ Creates zombies and appends to zombie list """

        # Only proceeds if lesser than the maximum
        while(self.zombie_count < self.MAXIMUM_ZOMBIE):
            
            self.zombie = WordZombie(self.GAME_CONFIG)



            ## Where the zombies spawn
            #self.starting_y = random.randrange(self.SCREEN_HEIGHT * 0.4,self.SCREEN_HEIGHT * 0.6)
            #self.starting_x = random.randrange(200, self.SCREEN_WIDTH - 100)


            ## calculates the zombie's height depending on the distance
            ## self.zombie_height
        
            #z_width = 100
            #z_height = 150



            #red = random.randrange(256)
            #green = random.randrange(256)
            #blue = random.randrange(256)
            #alpha = random.randrange(256)


            #zombie = arcade.create_rectangle_filled(self.starting_x, self.starting_y, z_width, z_height, (red, green, blue, alpha))




            self.zombie_count += 1
            self.zombie_list.append(self.zombie)
            print(self.zombie_list)



        




            




      





