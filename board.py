from player import Player

class Board:
    def __init__(self):
        self.special_pos = [(6, 1), (2, 6), (1, 8), (6, 12), (8, 13), (12, 8), (13, 6), (8, 2)]
        
        # no body used this board diagram for anything -> but this is to say how a ludo board looks like
        self.board = [[0 for _ in range(15)] for _ in range(15)]
        for i in range(0, 15):
            for j in range(0, 15):
                if (i, j) in self.special_pos:
                    self.board[i][j] = 2
                elif i in range(6, 9) and j in range(6, 9):
                    self.board[i][j] = 0
                elif i in range(6, 9) or j in range(6, 9):
                    self.board[i][j] = 1
        # Red reserved
        for i in range(1, 6):
            self.board[7][i] = 3
        # Green Reserved
        for i in range(1, 6):
            self.board[i][7] = 4
        # Yellow Reserved
        for i in range(9, 14):
            self.board[7][i] = 5
        # Blue Reserved
        for i in range(9, 14):
            self.board[i][7] = 6
        self.pieces_at_position = dict()

    # removing token from old position
    def remove_token_from_this_position(self, x, y, token_id, player_id):
        token_number = 4*(player_id-1) + token_id
        if (x, y) in self.pieces_at_position.keys():
            if token_number in self.pieces_at_position[(x, y)]:
                self.pieces_at_position[(x, y)].remove(token_number)           

    # putting token on the new position
    def update_position(self, token_id, x, y, player_id):
        if x == 0 and y == 0:
            return

        # for killing it should not be a safe cell or len = 0
        if (x, y) in self.special_pos or (x, y) not in self.pieces_at_position.keys() or len(self.pieces_at_position[(x, y)]) == 0:
            token_number = 4 * (player_id - 1) + token_id
            all_pieces = []
            if (x, y) in self.pieces_at_position:
                all_pieces = self.pieces_at_position[(x, y)]
            all_pieces.append(token_number)
            self.pieces_at_position[(x, y)] = all_pieces
        else:
            ele = self.pieces_at_position[(x, y)][0]
            ply_id = ele//4 + 1
            tkn_id = ele % 4
            if tkn_id == 0:
                tkn_id = 4
            print("This is killed: (player_id, token_id) ", ply_id, tkn_id)
            if ply_id != player_id:
                # original player ko update karna hai
                player = Player(ply_id, self)
                player.kill_token(tkn_id)

            token_number = 4 * (player_id - 1) + token_id
            all_pieces = list()
            all_pieces.append(token_number)
            self.pieces_at_position[(x, y)] = all_pieces

    def print_all_pieces(self):
        print("Position: [token_number, ... ], token_number = 4*(player_id - 1) + token_id")
        for (key, value) in self.pieces_at_position.items():
            print(key, end=" : ")
            print(value)

    def print_board(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[0])):
                print(self.board[i][j], end=" ")
            print("\n")
