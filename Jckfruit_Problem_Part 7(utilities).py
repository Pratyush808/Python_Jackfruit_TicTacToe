 # ============================ UTILITIES ===============================
    '''def restart_game(self, event):
        self.scores = {"X": 0, "O": 0}
        self.start_game(self.vs_computer)

    def continue_game(self, event):
        self.board = [""] * 9
        self.current_player = "X"
        for btn in self.buttons:
            btn.SetLabel("")
        self.score_text.SetLabel(self.get_score_text())

    def get_score_text(self):
        return (
            f"{self.player1} (X): {self.scores['X']}     |     "
            f"{self.player2} (O): {self.scores['O']}"
        )

    def clear_panel(self):
        for child in self.panel.GetChildren():
            child.Destroy()
        self.main_sizer.Clear(True)
        '''