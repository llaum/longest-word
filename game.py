import random
import string

class Game():
    def __init__(self):
        self.grid = [random.choice(string.ascii_uppercase) for i in range(0, 9)]
