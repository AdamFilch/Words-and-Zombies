import arcade
import random
import os

WORD_LIST = ("pull", "limping", "thaw", "placid", "record", "untidy", "tested",
        "heartbreaking", "hurt", "assorted", "servant", "stale", "talk",
        "snake", "desk", "advertisement", "balance", "cut", "animated",
        "loaf", "reading", "massive", "rhetorical", "reminiscent", "pig",
        "ray", "wrestle", "upbeat", "person", "addition", "record", "left",
        "lively", "rain", "tick", "knot", "remarkable", "neat", "yam", "sea",
        "amuse", "whirl", "thoughtful", "painstaking", "dysfunctional",
        "female", "threatening", "marked", "linen", "rinse", "word",
        "perfect", "hallowed", "dangerous", "birth", "pumped", "available",
        "coherent", "macabre", "early", "loss", "dam", "true", "berry",
        "unaccountable", "drop", "righteous", "nest", "attack", "smoggy",
        "lettuce", "crib", "mighty", "ratty", "short", "tall", "thankful",
        "aunt", "haunt", "wild", "pull", "brave", "property", "vague", "stove",
        "glass", "black-and-white", "floor", "cart", "blushing", "yellow",
        "daffy", "can", "gruesome", "screw", "wonder", "minor", "rotten",
        "exultant", "fearless", "box", "action", "probable", "verdant",
        "warlike", "wrathful", "support", "cooing", "piquant", "instrument",
        "development", "fire", "late", "rainstorm", "sad", "trust", "perform",
        "press", "spotless", "lyrical", "yell", "finger", "purring", "load",
        "vivacious", "parsimonious", "quack", "bury", "hellish", "selective",
        "leather", "quilt", "deserve", "obsolete", "repeat", "prose", "real",
        "chief", "delicious", "saw", "fold", "move", "pump", "size", "tart",
        "cover", "pets", "wheel", "mate", "rate", "coach", "honorable", "shake",
        "picture", "sprout", "mother", "toes", "interfere", "skinny", "alarm",
        "authority", "questionable", "cub", "enthusiastic", "wistful", "organic",
        "step", "behavior", "zonked", "dry", "alcoholic", "average", "stomach",
        "trade", "street", "panicky", "creepy", "relieved", "use", "animal",
        "distance", "soggy", "part", "worthless", "ball", "precious", "quiet",
        "arithmetic", "excited", "festive", "unequaled", "sincere", "hissing",
        "bruise", "pin", "key", "modern", "pigs", "foregoing", "attempt", "continue",
        "horse", "beautiful", "miscreant", "boorish", "book", "dress", "grey",
        "children", "bustling", "super", "secret", "message", "lock", "giants",
        "squash", "funny", "kindhearted", "classy", "mountain", "boil", "far",
        "hand", "curly", "hysterical", "thirsty", "attraction", "neighborly",
        "experience", "mellow", "knife", "woebegone", "rambunctious", "provide",
        "fragile", "obedient", "power", "jagged", "scrawny", "flag", "government",
        "unruly", "skip", "mess", "incandescent", "bucket", "bird", "desire",
        "nod", "shiny", "spotty", "care", "basin", "coat", "cave", "robin",
        "slippery", "mushy", "hand", "stormy", "fill", "phone", "scale", "unequal",
        "tightfisted", "attend", "nice", "lavish", "cough", "black", "request",
        "embarrassed", "absent", "kick", "tomatoes", "imaginary", "blue-eyed", "shirt",
        "blood", "misty", "shelf", "sulky", "onerous", "resolute", "salty", "sweater",
        "owe", "boring", "adjoining", "lacking", "separate", "shoes", "thread",
        "highfalutin", "ritzy", "apparel", "matter", "existence", "educated", "shocking",
        "rough", "food", "prefer")

# Used to create zombie objects to be drawn on screen
class WordZombie(arcade.Sprite):
    """ Word class """

    def __init__(self, GAME_CONFIG):
        """ Initializes the variables """


        # Inititializes the game configs
        self.SCREEN_WIDTH = GAME_CONFIG["general_settings"]['screen_width']
        self.SCREEN_HEIGHT = GAME_CONFIG["general_settings"]["screen_height"]
        self.MAXIMUM_ZOMBIE = GAME_CONFIG["general_settings"]["maximum_zombie"]
        self.ZOMBIE_KENNY = GAME_CONFIG["assets_path"]["images"]["zombie"]["zombie_kenny"]
        self.BC_SPRITE_SCALE = GAME_CONFIG["general_settings"]["bc_sprite_scale"]
        #self.zombie_word = 



        # Where the zombies spawn
        self.starting_y = random.randrange(self.SCREEN_HEIGHT * 0.5, self.SCREEN_HEIGHT * 0.6)
        self.starting_x = random.randrange(200, self.SCREEN_WIDTH - 100)


        # zombie dimensions
        self.z_width = int()
        self.z_height = int()

        # Variables
        self.zombie_count = int()

        # calculates the zombie's height depending on the distance
        # self.zombie_height

        super().__init__(self.ZOMBIE_KENNY, self.BC_SPRITE_SCALE/1.6, 0,0,0,0, self.starting_x,self.starting_y)

        #self.center_x = self.starting_y
        #self.center_y = self.starting_y


