import logging

class Banner:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def load(self):
        self.logger.info('Loading Banner')

        print(" _.................._")
        print("| |minecraft       | |")
        print("| |world           | |")
        print("| |boundary        | |")
        print("| |                | |")
        print("| |                | |")
        print("| |  tomordonez.com| |")
        print("| |________________| |")
        print("|    _________       |")
        print("|   |    |    |      |")
        print("|___|____|____|______|")
        print("\n")
