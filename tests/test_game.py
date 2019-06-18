import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_digits_is_invalid(self):
        new_game = Game()
        grid = new_game.grid
        self.assertFalse(new_game.is_valid("123"))

    def test_grid_is_valid(self):
        new_game = Game()
        grid = new_game.grid
        self.assertTrue(new_game.is_valid(grid))
