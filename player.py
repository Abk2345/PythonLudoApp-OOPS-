from tokens import Token
class Player:
    def __init__(self, id, board):
        self.id = id
        self.tokens = [Token(i) for i in range(1, 5)]

        # initial setup for testing
        # if id == 1:
        #     self.tokens[0].set_position(7, 2, self.id, board)
        # elif id == 2:
        #     self.tokens[0].set_position(3, 8, self.id, board)
    
    def valid_move_inside_reserved_grid(self, x, y, steps):
         # if inside home line, do this things
        if x == 7 and y != 0 and y <= 5:
            if steps > 6 - y:
                return False
        elif x == 7 and y != 14 and y >= 9:
            if steps > abs(y - 8):
                return False
        elif x != 0 and x <= 5 and y == 7:
            if steps > 6 - x:
                return False
        elif x != 14 and x >= 9 and y == 7:
            if steps > abs(y - 8):
                return False
        else:
            return True

    def move_token(self, token_id, steps, board, static_data, started_tokens, reached_tokens):
        token = self.tokens[token_id-1]
        if token.position == static_data.home_position[self.id]:
            prev = token_id
            while prev == token_id:
                token_id = int(input(f"Token {token_id} has reached home, choose another token to continue: "))
        
        token = self.tokens[token_id-1]

        # need to organise from here
        # here need to implement logic, if there is one outside and not yet reached home, you should choose that
        if self.id in started_tokens:
            if self.id in reached_tokens:
                if len(started_tokens[self.id]) != len(reached_tokens[self.id]):
                    if token.position == (0, 0) and steps != 6:
                        while token_id == prev:
                            token_id = int(input(f"Token {token_id} has needs 6 to start, choose another token to continue: "))
            else:
                if token.position == (0, 0) and steps != 6:
                    prev = token_id
                    while token_id == prev:
                        token_id = int(input(f"Token {token_id} has needs 6 to start, choose another token to continue: "))

        token = self.tokens[token_id-1]
        
        # check valid move if inside home
        if self.valid_move_inside_reserved_grid(token.position[0], token.position[1], steps) == False:
            prev = token_id
            while token_id == prev:
                token_id = int(input(f"Token {token_id} cannot make valid move, choose another token to continue: "))
            

        token = self.tokens[token_id-1]

        # remove it from existing pieces position
        board.remove_token_from_this_position(token.position[0], token.position[1], token_id, self.id)
        token.move(self.id, steps, board, started_tokens, reached_tokens, static_data)

    def kill_token(self, token_id):
        token = self.tokens[token_id-1]
        # print(token.position)
        token.kill_token()
        # print(token.position)

    def has_won(self, reached_tokens, static_data):
        return all(token.is_home(self.id, reached_tokens, static_data.home_position) for token in self.tokens)

