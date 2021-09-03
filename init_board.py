import yaml
from transform_input import transform_into_coordinates, transform_into_code
from draw_board import draw_board
import random
from fill_board import fill_board


def init_board(pieces_config, random_lineup=False):
    """
    Initilizes the board either according to initial positions in the config or randomly
    :param pieces_config: config file with all information about the used chess figures
    :param random_lineup:  bool if pieces should be placed randomly
    :return: board as list with pieces at positions to occupied fields dict, occupied fields dict
    """

    # draw initially '+' on the field
    initial_board = [['+' for j in range(8)] for i in range(8)]
    #draw_board(lineup)
    # read config file into dict
    # kann nachher raus da in ChessGame Klasse definiert
    # with open("chess_figure_config.yml", "r") as ymlfile:
    #     pieces_config = yaml.load(ymlfile, Loader=yaml.FullLoader)
    ######################################################################
    # print(pieces_config)
    occupied_fields = {}
    if random_lineup:
        for colour in pieces_config['PAWN']:
            # selects 1-5 pawns...
            pawn_number = random.randint(1, 5)
            pawn_selection = random.sample(pieces_config['PAWN'][colour]['init_pos'], pawn_number)
            for pawn_position in pawn_selection:
                pawn_coord = transform_into_coordinates(pawn_position)
                rand_movement = random.randint(0, 2)
                # ...and moves them by initial position +0 - +2 * directions_of_movement,
                # multiplied by (-1) as the board is flipped in comparison to the players view!
                pawn_row = pawn_coord[0] + rand_movement * pieces_config['PAWN'][colour]['directions_of_movement'][0][0] * (-1)
                # column of the pawn stays the same
                pawn_col = pawn_coord[1]
                position = transform_into_code([pawn_row, pawn_col])
                print(position)
                occupied_fields[position] = {'piece': 'PAWN',
                                             'colour': colour,
                                             'dir': pieces_config['PAWN'][colour][
                                             'directions_of_movement'],
                                             'sign': 'R'}

        # fill board to see which fields are still empty
        board_temp = fill_board(occupied_fields, initial_board)

        # get all empty fields on the board after placing the pawns
        empty_fields = [(row_index, col_index) for row_index, row in enumerate(board_temp)
                        for col_index, col in enumerate(row) if col == '+']

        for piece in pieces_config.keys():
            # pawns are already placed and can be skipped
            if piece != 'PAWN':
                for colour in pieces_config[piece].keys():
                    # repeat as often that all figures which should be placed according to init_pos are placed
                    for number in range(len(pieces_config[piece][colour]['init_pos'])):
                        # pick a random empty field and remove it from the list
                        random_index = random.randint(0, len(empty_fields) - 1)
                        random_position = transform_into_code(empty_fields.pop(random_index))
                        occupied_fields[random_position] = {'piece': piece,
                                                          'colour': colour,
                                                          'dir': pieces_config[piece][colour][
                                                          'directions_of_movement'],
                                                          'sign': 'R'}
        board = fill_board(occupied_fields, board_temp)

    else:
        for piece in pieces_config.keys():
            for colour in pieces_config[piece].keys():
                for position in pieces_config[piece][colour]['init_pos']:
                    occupied_fields[position] = {'piece': piece,
                                                      'colour': colour,
                                                      'dir': pieces_config[piece][colour][
                                                      'directions_of_movement'],
                                                      'sign': 'R'}
        board = fill_board(occupied_fields, initial_board)

    return board, occupied_fields




if __name__ == '__main__':

    print(init_board(True))
