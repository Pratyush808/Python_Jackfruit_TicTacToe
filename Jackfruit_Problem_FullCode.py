import wx
import random

BTN_BG = "#1e1e1e"
BTN_FG = "#ffffff"
ACCENT = "#4CAF50"


class TicTacToe(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Tic Tac Toe", size=(520, 640))
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("#101010")

        self.current_mode = None
        self.player1 = "Player 1"
        self.player2 = "Player 2"
        self.vs_computer = False

        self.scores = {"X": 0, "O": 0}

        self.font_btn = wx.Font(
            32, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD
        )

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.main_sizer)

        self.show_mode_selection()

        self.Centre()
        self.Show()

    # ============================ MODE SELECTION ===============================
    def show_mode_selection(self):
        self.clear_panel()

        title = wx.StaticText(self.panel, label="Choose Game Mode")
        title.SetForegroundColour("#ffffff")
        title.SetFont(wx.Font(26, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        btn_pvp = self.make_menu_button("Player vs Player")
        btn_pvc = self.make_menu_button("Player vs Computer")

        btn_pvp.Bind(wx.EVT_BUTTON, lambda e: self.ask_player_names())
        btn_pvc.Bind(wx.EVT_BUTTON, lambda e: self.start_game(True))

        v = wx.BoxSizer(wx.VERTICAL)
        v.Add(title, 0, wx.ALIGN_CENTER | wx.TOP, 40)
        v.Add(btn_pvp, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        v.Add(btn_pvc, 0, wx.ALIGN_CENTER | wx.ALL, 20)

        self.main_sizer.AddStretchSpacer()
        self.main_sizer.Add(v, 0, wx.ALIGN_CENTER)
        self.main_sizer.AddStretchSpacer()
        self.panel.Layout()

    def make_menu_button(self, text):
        btn = wx.Button(self.panel, label=text, size=(240, 50))
        btn.SetForegroundColour("#ffffff")
        btn.SetBackgroundColour(ACCENT)
        btn.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        return btn

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

    # ============================ GAME SETUP ===============================
    def start_game(self, vs_computer):
        self.vs_computer = vs_computer
        self.current_player = "X"
        self.board = [""] * 9

        if self.vs_computer:
            self.player1 = "You"
            self.player2 = "Computer"

        self.show_game_ui()

    def show_game_ui(self):
        self.clear_panel()

        # Scoreboard
        self.score_text = wx.StaticText(self.panel, label=self.get_score_text())
        self.score_text.SetForegroundColour("#ffffff")
        self.score_text.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        # Board Grid
        self.grid_sizer = wx.GridSizer(3, 3, 10, 10)
        self.buttons = []

        for i in range(9):
            btn = wx.Button(self.panel, label="", size=(120, 120))
            btn.SetFont(self.font_btn)
            btn.SetBackgroundColour(BTN_BG)
            btn.SetForegroundColour(BTN_FG)
            btn.Bind(wx.EVT_BUTTON, self.make_handler(i))
            self.buttons.append(btn)
            self.grid_sizer.Add(btn, 1, wx.EXPAND)

        # Control Buttons
        restart_btn = self.make_control_btn("Restart (reset scores)")
        continue_btn = self.make_control_btn("New Round")
        change_mode_btn = self.make_control_btn("Change Mode")

        restart_btn.Bind(wx.EVT_BUTTON, self.restart_game)
        continue_btn.Bind(wx.EVT_BUTTON, self.continue_game)
        change_mode_btn.Bind(wx.EVT_BUTTON, lambda e: self.show_mode_selection())

        bottom = wx.BoxSizer(wx.HORIZONTAL)
        bottom.Add(restart_btn, 1, wx.ALL, 8)
        bottom.Add(continue_btn, 1, wx.ALL, 8)
        bottom.Add(change_mode_btn, 1, wx.ALL, 8)

        # Add to main layout
        self.main_sizer.Add(self.score_text, 0, wx.ALIGN_CENTER | wx.TOP, 15)
        self.main_sizer.Add(self.grid_sizer, 1, wx.EXPAND | wx.ALL, 20)
        self.main_sizer.Add(bottom, 0, wx.EXPAND | wx.BOTTOM, 20)

        self.panel.Layout()

    def make_control_btn(self, label):
        btn = wx.Button(self.panel, label=label)
        btn.SetBackgroundColour("#333333")
        btn.SetForegroundColour("#ffffff")
        btn.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        return btn

    def make_handler(self, index):
        def handler(event):
            self.handle_move(index)
        return handler

    # ============================ GAME LOGIC ===============================
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

    def smart_ai_move(self):
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                if self.check_winner() == "O":
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "X"
                if self.check_winner() == "X":
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        if self.board[4] == "":
            return 4

        corners = [0, 2, 6, 8]
        random.shuffle(corners)
        for c in corners:
            if self.board[c] == "":
                return c

        sides = [1, 3, 5, 7]
        random.shuffle(sides)
        for s in sides:
            if self.board[s] == "":
                return s

        return 0

    def check_winner(self):
        combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for a, b, c in combos:
            if self.board[a] != "" and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]

        return None

    # ============================ END ROUND ===============================
    def end_round(self, result):
        if result == "Draw":
            wx.MessageBox("It's a draw!", "Result")
        else:
            winner_name = self.player1 if result == "X" else self.player2
            wx.MessageBox(f"{winner_name} wins!", "Result")
            self.scores[result] += 1

        self.score_text.SetLabel(self.get_score_text())

        self.continue_game(None)

    # ============================ UTILITIES ===============================
    def restart_game(self, event):
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


# ============================ RUN APP ===============================
if __name__ == "__main__":
    app = wx.App()
    TicTacToe()
    app.MainLoop()
