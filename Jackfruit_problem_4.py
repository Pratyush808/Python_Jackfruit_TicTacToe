
    # GAME SETUP
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
        btn.SetBackgroundColour("#000000")
        btn.SetForegroundColour("#ffffff")
        btn.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        return btn

    def make_handler(self, index):
        def handler(event):
            self.handle_move(index)
        return handler