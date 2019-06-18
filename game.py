# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string

class Game():
    def __init__(self):
        self.grid = [random.choice(string.ascii_uppercase) for i in range(0, 9)]
    def is_valid(self, word):
        for letter in word:
            if letter not in self.grid:
                return False
        return True

