from return_codes import ReturnCodes
import yaml
import random
from transform_input import transform_into_coordinates
from init_board import init_board
from draw_board import draw_board


class ChessGame:

    def __init__(self, rand_order=False):

        try:
            with open("chess_figure_config.yml", "r") as ymlfile:
                self.pieces_config = yaml.load(ymlfile, Loader=yaml.FullLoader)
        except Exception as e:
            print(ReturnCodes.CONFIG_ERROR.value, e)

        self.occupied_fields = {}

        self.board, self.occupied_fields = init_board(self.pieces_config, rand_order)

        print(self.occupied_fields)

        draw_board(self.board)







if __name__ == '__main__':
    game = ChessGame(rand_order=True)
