class TickTackToe:
    def __init__(self):
        self.player_x = "X"
        self.player_o = "O"
        self.EMPTY = " "
        self.TIE = "TIE"
        self.NUM_SQUARES = 9

    def display_instruct(self):
        print("""
        You will make your move known by entering a number, 0 - 8. The number
        will correspond to the board position as illustrated:
                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8
        """)

    def ask_number(self, question, low, high):
        response = int(input(question))
        if response not in range(low, high):
            raise IndexError
        return response

    def new_board(self):
        board = []
        for square in range(self.NUM_SQUARES):
            board.append(self.EMPTY)
        return board

    def display_board(self, board):
        print("\n\t", board[0], "|", board[1], "|", board[2])
        print("\t", "---------")
        print("\t", board[3], "|", board[4], "|", board[5])
        print("\t", "---------")
        print("\t", board[6], "|", board[7], "|", board[8])

    def legal_moves(self, board):
        moves = []
        for square in range(self.NUM_SQUARES):
            if board[square] == self.EMPTY:
                moves.append(square)
        return moves

    def winner(self, board):
        ways_to_win = ((0, 1, 2),
                       (3, 4, 5),
                       (6, 7, 8),
                       (0, 3, 6),
                       (1, 4, 7),
                       (2, 5, 8),
                       (0, 4, 8),
                       (2, 4, 6))

        for row in ways_to_win:
            if board[row[0]] == board[row[1]] == board[row[2]] != self.EMPTY:
                winner = board[row[0]]
                return winner

        if self.EMPTY not in board:
            return self.TIE

    def human_move(self, player, board):
        legal = self.legal_moves(board)
        move = None
        while move not in legal:
            try:
                move = self.ask_number(f"{player}, \
                where will you move? (0 - 8):", 0, self.NUM_SQUARES)
            except (ValueError, IndexError):
                print("\nInvalid input. Try again\n")
                continue
            if move not in legal:
                print("\nThat square is already occupied. Choose another.\n")
        print("Fine...")
        return move

    def next_turn(self, turn):
        if turn == self.player_x:
            return self.player_o
        else:
            return self.player_x

    def congrat_winner(self, the_winner):
        if the_winner != self.TIE:
            print(the_winner, "won!\n")
        else:
            print("It a tie!\n")

    def ask_yes_no(self):
        question = "Do you want to play another game? (y/n): "
        response = None
        while response not in ("y", "n"):
            response = input(question).lower()
        return response

    def play_game(self):
        while True:
            self.display_instruct()
            turn = self.player_x
            board = self.new_board()
            self.display_board(board)

            player1 = self.player_x
            player2 = self.player_o
            while not self.winner(board):
                if turn == player1:
                    move = self.human_move(player1, board)
                    board[move] = player1
                else:
                    move = self.human_move(player2, board)
                    board[move] = player2
                self.display_board(board)
                turn = self.next_turn(turn)

            the_winner = self.winner(board)
            self.congrat_winner(the_winner)
            response = self.ask_yes_no()
            if response:
                return


# test = TickTackToe()
# test.play_game()
