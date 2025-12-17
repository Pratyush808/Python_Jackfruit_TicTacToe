def handle_move(self, index):
        if self.board[index] != "":
            return
        if self.check_winner() or "" not in self.board:
            return

        self.make_move(index, self.current_player)

        winner = self.check_winner()
        if winner:
            self.end_round(winner)
            return

        if "" not in self.board:
            self.end_round("Draw")
            return

        self.current_player = "O" if self.current_player == "X" else "X"

        if self.vs_computer and self.current_player == "O":
            wx.CallLater(300, self.computer_move)

    def make_move(self, index, symbol):
        self.board[index] = symbol
        self.buttons[index].SetLabel(symbol)

    def computer_move(self):
        if self.check_winner() or "" not in self.board:
            return

        move = self.smart_ai_move()
        self.make_move(move, "O")

        if self.check_winner():
            self.end_round("O")
            return

        if "" not in self.board:
            self.end_round("Draw")
            return

        self.current_player = "X"
