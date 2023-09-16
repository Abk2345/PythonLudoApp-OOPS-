class Token:
    def __init__(self, id):
        self.id = id
        self.position = (0, 0)

    def set_position(self, x, y, player_id, board):
        self.position = (x, y)
        board.update_position(1, x, y, player_id)
        board.print_all_pieces()
        # print(self.position, self.id)

    def kill_token(self):
        self.position = (0, 0)

    # which direction to move from this point
    def find_direction(self, x, y, steps):
        row_fixed = -1
        col_fixed = -1
        if x in [6, 8]:
            row_fixed = x
        if y in [6, 8]:
            col_fixed = y
        dr = [0, 0]

        # if inside home line, do this things
        if x == 7 and y != 0 and y <= 5:
            dr[0] = 0
            dr[1] = 1
            return dr
        elif x == 7 and y != 14 and y >= 9:
            dr[0] = 0
            dr[1] = -1
            return dr
        elif x != 0 and x <= 5 and y == 7:
            dr[0] = 1
            dr[1] = 0
            return dr
        elif x != 14 and x >= 9 and y == 7:
            dr[0] = -1
            dr[1] = 0
            return dr

        # otherwise
        if row_fixed == -1:
            if col_fixed == 6:
                dr[0] = -1
                dr[1] = 0
            elif col_fixed == 8:
                dr[0] = 1
                dr[1] = 0
        if col_fixed == -1:
            if row_fixed == 6:
                dr[0] = 0
                dr[1] = 1
            elif row_fixed == 8:
                dr[0] = 0
                dr[1] = -1

        return dr

    def handle_steps(self, player_id, steps, board, direction):
        new_position_x = self.position[0] + steps*direction[0]
        new_position_y = self.position[1] + steps*direction[1]
        self.position = (new_position_x, new_position_y)
        board.update_position(self.id, self.position[0], self.position[1], player_id)
        return

    # move nahi kar payega, but mujhe use choice bhi dena hai ki they can select other token

    def move_2(self, player_id, steps, board, direction_map):
        if steps == 0:
            # print("Visited move!", self.id, self.position[0], self.position[1], player_id)
            board.update_position(self.id, self.position[0], self.position[1], player_id)
            return
        else:
            # handling entering to home
            if player_id == 1 and self.position == (7, 0):
                dr = [0, 1]
                return self.handle_steps(player_id, steps, board, dr)
            elif player_id == 2 and self.position == (0, 7):
                dr = [1, 0]
                return self.handle_steps(player_id, steps, board, dr)
            elif player_id == 3 and self.position == (7, 14):
                dr = [0, -1]
                return self.handle_steps(player_id, steps, board, dr)
            elif player_id == 4 and self.position == (14, 7):
                dr = [-1, 0]
                return self.handle_steps(player_id, steps, board, dr)
            elif self.position in direction_map:
                dr = direction_map[self.position]
            else:
                dr = self.find_direction(self.position[0], self.position[1], steps)
                
            new_pos_x = self.position[0] + dr[0]
            new_pos_y = self.position[1] + dr[1]
            self.position = (new_pos_x, new_pos_y)
            # print("Position: ", new_pos_x, new_pos_y)
            self.move_2(player_id, steps-1, board, direction_map)

    def move(self, player_id, steps, board, started_tokens, reached_tokens, static_data):
        # here
        if self.position == (0, 0):
            # print("here?")
            if steps == 6:
                temp_list = []
                if player_id in started_tokens:
                    temp_list = started_tokens[player_id]
                temp_list.append(self.id)
                started_tokens[player_id] = temp_list
                self.position = static_data.start_position[player_id]
                board.update_position(self.id, self.position[0], self.position[1], player_id)
            return
        self.move_2(player_id, steps, board, static_data.direction_map)

        # print("Current position for token number: ", end=" ")
        # print(4*(player_id-1)+self.id, end=" -> ")
        # print(self.position)


    def is_home(self, player_id, reached_tokens, home_position):
        # print("Cheking is home? : ", self.position == home_position[player_id], self.id, player_id)
        temp_list = []
        if self.position == home_position[player_id]:
            if player_id in reached_tokens.keys():
                temp_list = reached_tokens[player_id]
            temp_list.append(self.id)
            reached_tokens[player_id] = temp_list
            return True
