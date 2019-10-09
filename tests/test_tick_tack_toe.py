import unittest

from tick_tack_toe import TickTackToe


class TestTickTackToe(unittest.TestCase):

    def test_next_turn(self):
        test = TickTackToe()
        self.assertEqual(test.next_turn("X"), "O")
        self.assertEqual(test.next_turn("O"), "X")

    def test_new_board(self):
        test = TickTackToe()
        board = test.new_board()
        for i in range(test.NUM_SQUARES):
            self.assertEqual(board[i], test.EMPTY)

    def test_winner(self):
        test = TickTackToe()
        board = test.new_board()
        board[0] = board[1] = board[2] = test.player_x
        self.assertEqual(test.winner(board), test.player_x)

        board = test.new_board()
        board[0] = board[4] = board[8] = test.player_o
        self.assertEqual(test.winner(board), test.player_o)

    def test_legal_moves(self):
        test = TickTackToe()
        board = test.new_board()
        board[0] = board[4] = board[8] = test.player_o
        board[1] = board[2] = board[3] = test.player_x

        moves = test.legal_moves(board)
        self.assertEqual(moves, [5, 6, 7])
