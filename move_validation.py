from return_codes import ReturnCodes
import yaml
from math import sqrt
from transform_input import transform_into_coordinates

def move_validation(a: str, b: str, occupied_fields: dict) -> dict:
    """
    validate move from a to b
    """

    start_coords = transform_into_coordinates(a)
    target_coords = transform_into_coordinates(b)
    print(start_coords, target_coords)
    # get vector
    move_vector = [target_coords[0]-start_coords[0], target_coords[1]-start_coords[1]]
    print(move_vector)
    # get directions of move

    if occupied_fields[a] == 'KNIGHT':
        if move_vector not in occupied_fields[a]['dir']:
            return {'result': False, 'message': ReturnCodes.INVALID_MOVE.value}
        else:
            print('valid')
    else:
        max_value = max(abs(move_vector[0]), abs(move_vector[1]))
        vector_reduced = [move_vector[0]/max_value, move_vector[1]/max_value]
        if vector_reduced not in occupied_fields[a]['dir']:
            return {'result': False, 'message': ReturnCodes.INVALID_MOVE.value}
        else:
            print('valid')





if __name__ == '__main__':
    with open("chess_figure_config.yml", "r") as ymlfile:
        pieces_configs = yaml.load(ymlfile, Loader=yaml.FullLoader)

    occ = {'G3': {'piece': 'PAWN', 'colour': 'white', 'dir': [[-1, 0]], 'sign': 'R'}, 'B5': {'piece': 'PAWN', 'colour': 'black', 'dir': [[-1, 0]], 'sign': 'R'}, 'D7': {'piece': 'PAWN', 'colour': 'black', 'dir': [[-1, 0]], 'sign': 'R'}, 'E6': {'piece': 'PAWN', 'colour': 'black', 'dir': [[-1, 0]], 'sign': 'R'}, 'G6': {'piece': 'PAWN', 'colour': 'black', 'dir': [[-1, 0]], 'sign': 'R'}, 'B6': {'piece': 'ROOK', 'colour': 'white', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R'}, 'H5': {'piece': 'ROOK', 'colour': 'white', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R'}, 'G7': {'piece': 'ROOK', 'colour': 'black', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R'}, 'F8': {'piece': 'ROOK', 'colour': 'black', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R'}, 'H2': {'piece': 'BISHOP', 'colour': 'white', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'R'}, 'H4': {'piece': 'BISHOP', 'colour': 'white', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'R'}, 'F2': {'piece': 'BISHOP', 'colour': 'black', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'R'}, 'D6': {'piece': 'BISHOP', 'colour': 'black', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'R'}, 'G2': {'piece': 'KNIGHT', 'colour': 'white', 'dir': [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]], 'sign': 'R'}, 'A4': {'piece': 'KNIGHT', 'colour': 'white', 'dir': [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]], 'sign': 'R'}, 'E8': {'piece': 'KNIGHT', 'colour': 'black', 'dir': [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]], 'sign': 'R'}, 'C3': {'piece': 'KNIGHT', 'colour': 'black', 'dir': [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]], 'sign': 'R'}}

    a = 'G3'
    b = 'G4'
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

