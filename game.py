from board import Board
from player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("X"), Player("O")]
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % 2

    def play(self):
        while True:
            # play a single round
            while True:
                self.board.display()
                current_player = self.players[self.current_player_index]
                current_player.make_move(self.board)

                if self.board.check_winner(current_player.symbol):
                    self.board.display()
                    print(f"Player {current_player.symbol} wins!")
                    break

                if self.board.is_crowded():
                    self.board.display()
                    print("Nobody wins, it's a draw!")
                    break

                self.switch_player()

            # ask whether to replay
            if not self.ask_replay():
                print("Thanks for playing!")
                break

            # reset game state for a new round
            self.board = Board()
            self.current_player_index = 0

    def ask_replay(self):
        while True:
            replay = input("Do you want to play again? (y/n): ").lower()
            if replay in ['y', 'n']:
                return replay == 'y'
            print("Invalid input, Please enter 'y' or 'n'.")