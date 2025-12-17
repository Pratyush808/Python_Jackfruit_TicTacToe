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
