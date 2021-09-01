import yaml
from transform_input import transform_into_coordinates
from draw_board import draw_board
import random


def init_board(random_lineup=False) -> list:

    # draw initially '+' on the field
    lineup = [['+' for j in range(8)] for i in range(8)]
    # draw_board(lineup)
    # read config file into dict
    with open("chess_figure_config.yml", "r") as ymlfile:
        pieces_config = yaml.load(ymlfile, Loader=yaml.FullLoader)

    if random_lineup:

        for piece in ['PAWN_black', 'PAWN_white']:
            # selects 1-5 pawns...
            pawn_number = random.randint(1, 5)
            pawn_selection = random.sample(pieces_config[piece]['init_pos'], pawn_number)
            for pawn_position in pawn_selection:
                pawn_coord = transform_into_coordinates(pawn_position)
                rand_movement = random.randint(0, 2)
                # ...and moves them by init_pos +0 - +2 * directions_of_movement, multiplied by (-1) as the board is
                # flipped in comparison to the players view!
                pawn_row = pawn_coord[0] + rand_movement * pieces_config[piece]['directions_of_movement'][0][0] * (-1)
                # column of the pawn stays the same
                pawn_col = pawn_coord[1]
                lineup[pawn_row][pawn_col] = pieces_config[piece]['sign']

        # get all empty fields on the board
        empty_fields = [(row_index, col_index) for row_index, row in enumerate(lineup)
                        for col_index, col in enumerate(row) if col == '+']

        # get all pieces which are not pawns
        list_of_figures = [pieces_config[piece]['sign'] for piece in pieces_config.keys()
                           if 'P' not in pieces_config[piece]['sign']]

        # place all other figures randomly on the field by selecting as much fields as needed from the empty fields list
        field_selection = random.sample(empty_fields, len(list_of_figures))

        for piece, position in zip(list_of_figures, field_selection):
            lineup[position[0]][position[1]] = piece

    else:
        # place all pieces according to there initial position on the board
        for piece in pieces_config.keys():
            for positions in pieces_config[piece]['init_pos']:
                coord_temp = transform_into_coordinates(positions)
                lineup[coord_temp[0]][coord_temp[1]] = pieces_config[piece]['sign']

    draw_board(lineup)
    return lineup

if __name__ == '__main__':
    init_board(random_lineup=True)
