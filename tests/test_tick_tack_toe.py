import unittest

from tick_tack_toe import TickTackToe


class TestTickTackToe(unittest.TestCase):

    def test_next_turn(self):
        test = TickTackToe()
        self.assertEqual(test.next_turn("X"), "O")
        self.assertEqual(test.next_turn("O"), "X")
