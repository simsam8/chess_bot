class Board:
    def __init__(self):
        self.board = [
            ["br", "bh", "bb", "bq", "bk", "bb", "bh", "br"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            ["wr", "wh", "wb", "wq", "wk", "wb", "wh", "wr"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ]

        self.columns = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        self.rows = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7}
        return

    def print_board(self):
        for row in self.board:
            print(row)

    def translate_move(self, chess_pos):
        """
        translates chess position to list index
        """
        return (self.rows[chess_pos[1]], self.columns[chess_pos[0]])

    def move_piece(self, current_pos, new_pos):
        """
        Moves a piece form current_pos to new_pos
        Input a chess position like: A2, G5
        """
        current_pos = self.translate_move(current_pos)
        new_pos = self.translate_move(new_pos)
        piece_to_move = self.board[current_pos[0]][current_pos[1]]
        piece_at_target = self.board[new_pos[0]][new_pos[1]]

        if piece_to_move == 0:
            print("There is no piece at this position")

        else:
            self.board[new_pos[0]][new_pos[1]] = piece_to_move
            self.board[current_pos[0]][current_pos[1]] = 0


game = Board()

game.print_board()
game.move_piece("A1", "A3")
game.print_board()
