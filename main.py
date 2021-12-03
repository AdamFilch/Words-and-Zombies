import arcade
import yaml

from src.game import myGame


def load_config():
    """ Loads game config details to be used """

    with open("config.yaml", "r") as config:
        try:
            return yaml.safe_load(config)
        except yaml.YAMLError as exc:
            print(exc)


def main():
    """ Main Function """

    GAME_CONFIG = load_config()


    window = myGame(GAME_CONFIG)
    arcade.run()


if __name__ == "__main__":
    main()
