import yaml
from src.transform_input import transform_into_coordinates, transform_into_code
from src.return_codes import ReturnCodes


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
    start_coordinates = transform_into_coordinates(a)
    target_coordinates = transform_into_coordinates(b)

    # get vector of intended move
    move_vector = [target_coordinates[0]-start_coordinates[0], target_coordinates[1]-start_coordinates[1]]

    if occupied_fields[a]['piece'] == 'KNIGHT':
        if move_vector not in occupied_fields[a]['dir']:
            return {'result': False, 'message': ReturnCodes.INVALID_MOVE.value, 'piece': None, 'field': None}
        else:
            if b in occupied_fields.keys():
                if occupied_fields[b]['colour'] == occupied_fields[a]['colour']:
                    return {'result': False, 'message': ReturnCodes.MOVE_BLOCKED_OWN.value,
                            'piece': occupied_fields[b]['piece'], 'field': b}
                else:
                    return {'result': False, 'message': ReturnCodes.BEAT_FIGURE.value,
                            'piece': occupied_fields[b]['piece'], 'field': b}
            else:
                return {'result': True, 'message': ReturnCodes.SUCCESS.value,
                        'piece': None, 'field': None}
    else:
        max_value = max(abs(move_vector[0]), abs(move_vector[1]))
        vector_reduced = [move_vector[0]/max_value, move_vector[1]/max_value]
        if vector_reduced not in occupied_fields[a]['dir']:
            return {'result': False, 'message': ReturnCodes.INVALID_MOVE.value, 'piece': None, 'field': None}
        else:
            # step by step towards target field
            for step in range(1, occupied_fields[a]['max_steps'] + 1):
                # add vector_reduced to start_coordiantes to move one field ahead
                coordinates_temp = [start_coordinates[0] + step * vector_reduced[0], start_coordinates[1] + step * vector_reduced[1]]
                transform = transform_into_code(coordinates_temp)
                coords_temp_trans = transform['value']
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
    with open("../chess_figures_config.yml", "r") as ymlfile:
        pieces_configs = yaml.load(ymlfile, Loader=yaml.FullLoader)

    occ = {'G4': {'piece': 'PAWN', 'colour': 'white', 'dir': [[-1, 0]], 'sign': 'P', 'max_steps': 1},
 'E2': {'piece': 'PAWN', 'colour': 'white', 'dir': [[-1, 0]], 'sign': 'P', 'max_steps': 1},
 'E6': {'piece': 'PAWN', 'colour': 'black', 'dir': [[1, 0]], 'sign': 'P', 'max_steps': 1},
 'B6': {'piece': 'PAWN', 'colour': 'black', 'dir': [[1, 0]], 'sign': 'P', 'max_steps': 1},
 'G5': {'piece': 'PAWN', 'colour': 'black', 'dir': [[1, 0]], 'sign': 'P', 'max_steps': 1},
 'B2': {'piece': 'ROOK', 'colour': 'white', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R', 'max_steps': 7},
 'G6': {'piece': 'ROOK', 'colour': 'white', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R', 'max_steps': 7},
 'D8': {'piece': 'ROOK', 'colour': 'black', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R', 'max_steps': 7},
 'G1': {'piece': 'ROOK', 'colour': 'black', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R', 'max_steps': 7},
 'E4': {'piece': 'BISHOP', 'colour': 'white', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'B', 'max_steps': 7},
 'G2': {'piece': 'BISHOP', 'colour': 'white', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'B', 'max_steps': 7},
 'F5': {'piece': 'BISHOP', 'colour': 'black', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'B', 'max_steps': 7},
 'E1': {'piece': 'BISHOP', 'colour': 'black', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'B', 'max_steps': 7},
 'E5': {'piece': 'KNIGHT', 'colour': 'white', 'dir': [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]], 'sign': 'N', 'max_steps': 1},
 'B3': {'piece': 'KNIGHT', 'colour': 'white', 'dir': [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]], 'sign': 'N', 'max_steps': 1},
 'A7': {'piece': 'KNIGHT', 'colour': 'black', 'dir': [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]], 'sign': 'N', 'max_steps': 1},
 'H3': {'piece': 'KNIGHT', 'colour': 'black', 'dir': [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]], 'sign': 'N', 'max_steps': 1},
 'D6': {'piece': 'QUEEN', 'colour': 'white', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'Q', 'max_steps': 7},
 'C7': {'piece': 'QUEEN', 'colour': 'black', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'Q', 'max_steps': 7},
 'D1': {'piece': 'KING', 'colour': 'white', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'K', 'max_steps': 1},
 'G3': {'piece': 'KING', 'colour': 'black', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'K', 'max_steps': 1}}

    x = 'E5'
    y = 'D3'
    print(move_validation(x, y, occ))









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

