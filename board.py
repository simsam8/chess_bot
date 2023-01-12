class Board:
    def __init__(self):
        self.board = [
            ["br", "bh", "bb", "bq", "bk", "bb", "bh", "br"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wr", "wh", "wb", "wq", "wk", "wb", "wh", "wr"],
        ]

        self.columns = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        self.rows = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7}
        return

    def print_board(self):
        # only for printing purposes
        inverse_row_id = {v: k for k, v in self.rows.items()}
        print(inverse_row_id)
        for i, row in enumerate(self.board):
            print(inverse_row_id[i], end="\t")
            for col in row:
                print(col, end="\t")
            print()
        print(" ", end="\t")
        for x in range(65, 73):
            print(chr(x), end="\t")
        print()

    def translate_move(self, chess_pos):
        """
        translates chess position to list index
        """
        return (self.rows[chess_pos[1]], self.columns[chess_pos[0]])

    def move_valid(self, current_pos, new_pos):
        """
        Validates if the chosen piece can move
        to the new position

        current_pos and new_pos is given as list index

        return true/false
        """

        piece_to_move = self.board[current_pos[0]][current_pos[1]]
        piece_at_target = self.board[new_pos[0]][new_pos[1]]

        # Movement rules based on which piece we choose

        # Pawns
        if piece_to_move[1] == "p":
            # white pawns
            if piece_to_move[0] == "w":
                # if it is in starting position
                if current_pos[0] == 6:
                    if (0 < (current_pos[0] - new_pos[0]) <= 2) and (
                        current_pos[1] == new_pos[1] and piece_at_target == 0
                    ):
                        return True
                    else:
                        return False
                # All other positions
                else:
                    if (0 < (current_pos[0] - new_pos[0]) <= 1) and (
                        current_pos[1] == new_pos[1] and piece_at_target == 0
                    ):
                        return True
                    # TODO: take other pieces + en pasant
                    else:
                        return False
            # TODO: Black pawns

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

        if self.move_valid(current_pos, new_pos):
            self.board[new_pos[0]][new_pos[1]] = piece_to_move
            self.board[current_pos[0]][current_pos[1]] = 0

        else:
            print("Not a valid move")


game = Board()

while True:
    game.print_board()
    from_tile = str(input("Choose piece to move: "))
    to_tile = str(input("Choose tile to move to: "))
    game.move_piece(from_tile, to_tile)
