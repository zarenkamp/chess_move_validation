import random
import yaml
from src.draw_board import draw_board
from src.fill_board import fill_board
from src.transform_input import transform_into_coordinates, transform_into_code


def init_board(pieces_config, random_lineup=False):
    """
    Initializes the board either according to initial positions in the config or randomly
    :param pieces_config: config file with all information about the used chess figures
    :param random_lineup:  bool if pieces should be placed randomly
    :return: board as list with pieces at positions in occupied fields dict, occupied fields dict
    """

    # draw initially '+' on the field
    initial_board = [['+' for j in range(8)] for i in range(8)]

    occupied_fields = {}
    # place pieces randomly
    if random_lineup:
        for colour in pieces_config['PAWN']:
            # selects 1-5 pawns...
            pawn_number = random.randint(1, 5)
            pawn_selection = random.sample(pieces_config['PAWN'][colour]['init_pos'], pawn_number)
            for pawn_position in pawn_selection:
                # transform into board coordinates
                pawn_coord = transform_into_coordinates(pawn_position)['value']
                rand_movement = random.randint(0, 2)
                pawn_row = pawn_coord[0] + rand_movement * pieces_config['PAWN'][colour]['directions_of_movement'][0][0]
                # column of the pawn stays the same
                pawn_col = pawn_coord[1]
                # re-transform
                position = transform_into_code([pawn_row, pawn_col])['value']
                occupied_fields[position] = {'piece': 'PAWN',
                                             'colour': colour,
                                             'dir': pieces_config['PAWN'][colour]['directions_of_movement'],
                                             'sign': pieces_config['PAWN'][colour]['sign'],
                                             'max_steps': pieces_config['PAWN'][colour]['max_steps']}
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
                        random_position = transform_into_code(empty_fields.pop(random_index))['value']
                        occupied_fields[random_position] = {'piece': piece,
                                                            'colour': colour,
                                                            'dir': pieces_config[piece][colour]['directions_of_movement'],
                                                            'sign': pieces_config[piece][colour]['sign'],
                                                            'max_steps': pieces_config[piece][colour]['max_steps']}
        # set pieces to board
        board = fill_board(occupied_fields, board_temp)

    # place pieces according to config
    else:
        for piece in pieces_config.keys():
            for colour in pieces_config[piece].keys():
                for position in pieces_config[piece][colour]['init_pos']:
                    occupied_fields[position] = {'piece': piece,
                                                 'colour': colour,
                                                 'dir': pieces_config[piece][colour]['directions_of_movement'],
                                                 'sign': pieces_config[piece][colour]['sign'],
                                                 'max_steps': pieces_config[piece][colour]['max_steps']}
        board = fill_board(occupied_fields, initial_board)

    return board, occupied_fields


if __name__ == '__main__':
    with open("../chess_figures_config.yml", "r") as ymlfile:
        pieces_configs = yaml.load(ymlfile, Loader=yaml.FullLoader)

    res = init_board(pieces_configs, True)
    print(res[1])
    draw_board(res[0])

