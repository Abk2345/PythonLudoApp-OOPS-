# To Store Static Data for Ludo Game
class StaticData:
    def __init__(self):
        self.start_position = dict()
        self.home_position = dict()
        self.direction_map = dict()

        self.set_direction_map()
        self.set_start_position()
        self.set_home_position()

    def set_start_position(self):
        self.start_position[1] = (6, 1)  #Red
        self.start_position[2] = (1, 8)  #Green
        self.start_position[3] = (8, 13)  #Blue
        self.start_position[4] = (13, 6)  #Yellow

    def set_home_position(self):
        self.home_position[1] = (7, 6)  #red
        self.home_position[2] = (6, 7) #green
        self.home_position[3] = (7, 8) #Blue
        self.home_position[4] = (8, 7) #Yellow

    def set_direction_map(self):
        self.direction_map[(5, 6)] = (-1, 0)
        self.direction_map[(0, 6)] = (0, 1)
        self.direction_map[(0, 8)] = (1, 0)
        self.direction_map[(5, 8)] = (1, 1)

        self.direction_map[(6, 9)] = (0, 1)
        self.direction_map[(6, 14)] = (1, 0)
        self.direction_map[(8, 14)] = (0, -1)
        self.direction_map[(8, 9)] = (1, -1)

        self.direction_map[(9, 8)] = (1, 0)
        self.direction_map[(14, 8)] = (0, -1)
        self.direction_map[(14, 6)] = (-1, 0)
        self.direction_map[(9, 6)] = (-1, -1)

        self.direction_map[(8, 5)] = (0, -1)
        self.direction_map[(8, 0)] = (-1, 0)
        self.direction_map[(6, 0)] = (0, 1)
        self.direction_map[(6, 5)] = (-1, 1)

        self.direction_map[(0, 7)] = (0, 1)
        self.direction_map[(7, 0)] = (-1, 0)
        self.direction_map[(7, 14)] = (1, 0)
        self.direction_map[(14, 7)] = (0, -1)
