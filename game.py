from return_codes import ReturnCodes
import yaml
import random
from transform_input import transform_into_coordinates


class ChessGame:

    def __init__(self, rand_order=False):

        try:
            with open("chess_figure_config.yml", "r") as ymlfile:
                self.pieces_config = yaml.load(ymlfile, Loader=yaml.FullLoader)
        except Exception as e:
            print(ReturnCodes.CONFIG_ERROR.value, e)

        self.occupied_fields = {}
        # draw initially '+' on the field
        self.board = [['+' for j in range(8)] for i in range(8)]

        if rand_order:
            pass
        else:
            for piece in self.pieces_config.keys():
                for colour in self.pieces_config[piece].keys():
                    for position in self.pieces_config[piece][colour]['init_pos']:
                        self.occupied_fields[position] = {'piece': piece,
                                                           'colour': colour,
                                                           'dir': self.pieces_config[piece][colour]['directions_of_movement'],
                                                           'sign': 'R'}
        print(self.occupied_fields)






if __name__ == '__main__':
    game = ChessGame(rand_order=False)
