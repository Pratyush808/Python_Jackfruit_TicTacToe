
    # ============================ PLAYER NAMES ===============================
    def ask_player_names(self):
        dlg = wx.TextEntryDialog(self, "Enter Player 1 name:", "Player Names")
        if dlg.ShowModal() == wx.ID_OK:
            self.player1 = dlg.GetValue() or "Player 1"
        dlg.Destroy()

        dlg2 = wx.TextEntryDialog(self, "Enter Player 2 name:", "Player Names")
        if dlg2.ShowModal() == wx.ID_OK:
            self.player2 = dlg2.GetValue() or "Player 2"
        dlg2.Destroy()

        self.start_game(vs_computer=False)
