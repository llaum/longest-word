# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string
import requests

class Game():
    def __init__(self):
        self.grid = [random.choice(string.ascii_uppercase) for i in range(0, 9)]
    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.__check_dictionary(word)

    def __check_dictionary(self, word):
        r = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        response = r.json()
        return response['found']
