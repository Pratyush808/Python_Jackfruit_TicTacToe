   # ============================ MODE SELECTION ===============================
    '''def show_mode_selection(self):
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
        '''