import random

from board import Board
from player import Player
from static_data import StaticData

# static properties player aur game ka property hai -> game ke andar se board aur players setup- > players se token setup aur interactions


class LudoGame:
    # initialize game of ludo
    def __init__(self, num_players):
        self.num_players = num_players
        self.board = Board()
        self.static_data = StaticData()
        self.reached_tokens = dict()
        self.started_tokens = dict()
        self.current_player = None
        self.players = [Player(i, self.board) for i in range(1, num_players+1)]

    def start_game(self):
        self.current_player = self.players[0]
        print("Starting player id is: ", self.current_player.id)
        while not self.is_winner():
            self.play_turn()
            self.switch_player()
        print("Winning person id: ", self.current_player.id)

    def play_turn(self):
        dice_roll = random.randint(1, 6)
        print(f"Player {self.current_player.id}, it's your turn. You rolled a {dice_roll}")
        move_token = input("Enter the token ID to move or 'skip': ")
        if move_token != 'skip':
            move_token = int(move_token)
            while move_token > 4:
                 move_token = int(input("Enter correct token ID in range (1 to 4) to move or 'skip': "))
            # move_token = int(move_token)
            self.current_player.move_token(move_token, dice_roll, self.board, self.static_data, self.started_tokens, self.reached_tokens)
        
        self.print_board_pieces()

    def switch_player(self):
        index = self.players.index(self.current_player)
        self.current_player = self.players[(index+1) % self.num_players]

    def is_winner(self):
        return any(player.has_won(self.reached_tokens, self.static_data) for player in self.players)

    def print_board_pieces(self):
        self.board.print_all_pieces()

if __name__ == "__main__":
    # Debugging ludo board
    lg = LudoGame(2)
    num_players = int(input("Enter the number of players (2 to 4) "))
    if 2 <= num_players <= 4:
        game = LudoGame(num_players)
        game.start_game()
    else:
        print("Invalid number of players. Please choose between 2 to 4.")
