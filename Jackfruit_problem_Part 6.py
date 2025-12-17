def end_round(self, result):
    if result == "Draw":
         wx.MessageBox("It's a draw!", "Result")
    else:
        winner_name = self.player1 if result == "X" else self.player2
        wx.MessageBox(f"{winner_name} wins!", "Result")
        self.scores[result] += 1

        self.score_text.SetLabel(self.get_score_text())

        self.continue_game(None)
