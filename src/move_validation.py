from return_codes import ReturnCodes
import yaml
from math import sqrt
from transform_input import transform_into_coordinates, transform_into_code

def move_validation(a: str, b: str, occupied_fields: dict) -> dict:
    """
    Validates the intended move. First the vector of the move is calculated. This vector is reduced to a base move.
    Validation if this base move is in the figure config for this piece. Step by step marching to target field and
    checking if there is piece blocking. Validation if move is longer than in figure config.
    :param a: starting field
    :param b: target field
    :param occupied_fields: dict with all occupied fields
    :return: result dict
    """
    start_coordiantes = transform_into_coordinates(a)
    target_coordiantes = transform_into_coordinates(b)

    # get vector of intended move
    move_vector = [target_coordiantes[0]-start_coordiantes[0], target_coordiantes[1]-start_coordiantes[1]]

    if occupied_fields[a] == 'KNIGHT':
        if move_vector not in occupied_fields[a]['dir']:
            return {'result': False, 'message': ReturnCodes.INVALID_MOVE.value, 'piece': None, 'field': None}
        else:
            # prüfen ob und welche Figur auf dem target Feld steht
            print('valid')
    else:
        max_value = max(abs(move_vector[0]), abs(move_vector[1]))
        vector_reduced = [move_vector[0]/max_value, move_vector[1]/max_value]
        if vector_reduced not in occupied_fields[a]['dir']:
            return {'result': False, 'message': ReturnCodes.INVALID_MOVE.value, 'piece': None, 'field': None}
        else:
            # prüfen ob was dazwischen liegt
            print('valid')
            # step by step towards target field
            for step in range(1, occupied_fields[a]['max_steps'] + 1):
                # add vector_reduced to start_coords to move one field ahead
                coordinates_temp = [start_coordiantes[0] + step * vector_reduced[0], start_coordiantes[1] + step * vector_reduced[1]]
                print(coordinates_temp)
                transform = transform_into_code(coordinates_temp)
                coords_temp_trans = transform['value']
                print(coords_temp_trans)
                # valid transformation of coordinates
                if transform['result']:
                    # check if there is a piece at the actual field
                    if coords_temp_trans in occupied_fields.keys():
                        # blocking piece has same colour
                        if occupied_fields[coords_temp_trans]['colour'] == occupied_fields[a]['colour']:
                            return {'result': False, 'message': ReturnCodes.MOVE_BLOCKED_OWN.value,
                                    'piece': occupied_fields[coords_temp_trans]['piece'], 'field': coords_temp_trans}
                        # blocking piece as different colour
                        else:
                            return {'result': True, 'message': ReturnCodes.BEAT_FIGURE.value,
                                     'piece': occupied_fields[coords_temp_trans]['piece'], 'field': coords_temp_trans}
                    # actual field empty
                    else:
                        # check if target field is reached, if so this is a valid move
                        if coords_temp_trans == b:
                            return {'result': True, 'message': ReturnCodes.SUCCESS.value,
                                    'piece': None, 'field': None}

                    # if last step of loop is made and target field is not reached than this is a invalid move,
                    # e.g. a two-field move for Pawn or King
                    if step == occupied_fields[a]['max_steps'] and coords_temp_trans != b:
                        return {'result': False, 'message': ReturnCodes.INVALID_MOVE.value, 'piece': None,
                                'field': None}

                # not possible to transform coordinates
                else:
                    return {'result': False, 'message': transform['message'], 'piece': None,
                            'field': None}









if __name__ == '__main__':
    with open("../chess_figure_config.yml", "r") as ymlfile:
        pieces_configs = yaml.load(ymlfile, Loader=yaml.FullLoader)

    occ = {'B2': {'piece': 'PAWN', 'colour': 'white', 'dir': [[-1, 0]], 'sign': 'R', 'max_steps': 1},
             'D2': {'piece': 'PAWN', 'colour': 'white', 'dir': [[-1, 0]], 'sign': 'R', 'max_steps': 1},
             'C2': {'piece': 'PAWN', 'colour': 'white', 'dir': [[-1, 0]], 'sign': 'R', 'max_steps': 1},
             'A7': {'piece': 'PAWN', 'colour': 'black', 'dir': [[1, 0]], 'sign': 'R', 'max_steps': 1},
             'G6': {'piece': 'PAWN', 'colour': 'black', 'dir': [[1, 0]], 'sign': 'R', 'max_steps': 1},
             'H5': {'piece': 'PAWN', 'colour': 'black', 'dir': [[1, 0]], 'sign': 'R', 'max_steps': 1},
             'C6': {'piece': 'PAWN', 'colour': 'black', 'dir': [[1, 0]], 'sign': 'R', 'max_steps': 1},
             'F7': {'piece': 'PAWN', 'colour': 'black', 'dir': [[1, 0]], 'sign': 'R', 'max_steps': 1},
             'B7': {'piece': 'ROOK', 'colour': 'white', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R', 'max_steps': 7},
             'E6': {'piece': 'ROOK', 'colour': 'white', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R', 'max_steps': 7},
             'A4': {'piece': 'ROOK', 'colour': 'black', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R', 'max_steps': 7}, 'D4': {'piece': 'ROOK', 'colour': 'black', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R', 'max_steps': 7}, 'D3': {'piece': 'BISHOP', 'colour': 'white', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'R', 'max_steps': 7}, 'B5': {'piece': 'BISHOP', 'colour': 'white', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'R', 'max_steps': 7}, 'H3': {'piece': 'BISHOP', 'colour': 'black', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'R', 'max_steps': 7}, 'B1': {'piece': 'BISHOP', 'colour': 'black', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'R', 'max_steps': 7}, 'G7': {'piece': 'KNIGHT', 'colour': 'white', 'dir': [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]], 'sign': 'R', 'max_steps': 1}, 'A8': {'piece': 'KNIGHT', 'colour': 'white', 'dir': [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]], 'sign': 'R', 'max_steps': 1}, 'F3': {'piece': 'KNIGHT', 'colour': 'black', 'dir': [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]], 'sign': 'R', 'max_steps': 1}, 'C1': {'piece': 'KNIGHT', 'colour': 'black', 'dir': [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]], 'sign': 'R', 'max_steps': 1}}

    a = 'A6'
    b = 'A5'
    print(move_validation(a, b, occ))









    test_board_1 = [['Rb', '+', 'Bb', 'Qb', 'Nb', 'Bb', 'Nb', 'Rb'],
                   ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
                   ['+', '+', 'Nb', '+', '+', '+', '+', '+'],
                   ['+', '+', '+', '+', '+', '+', '+', '+'],
                   ['+', '+', '+', 'Pw', 'Bw', '+', '+', '+'],
                   ['+', '+', '+', '+', '+', '+', '+', '+'],
                   ['Pw', 'Pw', 'Pw', '+', 'Pw', 'Pw', 'Pw', 'Pw'],
                   ['Rw', 'Nw', '+', 'Qw', 'Kw', 'Bw', 'Nw', 'Rw']]

    test_board_2 = [['+', '+', '+', '+', '+', '+', '+', '+'],
                   ['+', '+', '+', '+', '+', '+', '+', '+'],
                   ['+', '+', 'Nb', '+', 'Pb', '+', '+', '+'],
                   ['+', '+', '+', '+', '+', '+', '+', '+'],
                   ['+', '+', 'Rw', 'Pw', 'Bw', '+', '+', '+'],
                   ['+', '+', '+', '+', '+', '+', '+', '+'],
                   ['+', '+', '+', '+', '+', '+', '+', '+'],
                   ['+', '+', '+', '+', '+', '+', '+', '+']]

