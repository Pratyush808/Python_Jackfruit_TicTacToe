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