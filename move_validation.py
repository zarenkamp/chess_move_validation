from return_codes import ReturnCodes
import yaml
from math import sqrt


def move_validation(a: list, b: list, board: list) -> dict:
    """
    validate move from a to b
    """
    with open("chess_figure_config.yml", "r") as ymlfile:
        pieces_config = yaml.load(ymlfile, Loader=yaml.FullLoader)

    if a == b:
        return {'validation': False, 'figure': None, 'message': ReturnCodes.SAME_COORDINATES.value}

    # check if there is a piece at the selected field
    piece = board[a[0]][a[1]]
    print(f'piece: {piece}')
    if piece == '+':
        return {'validation': False, 'figure': None, 'message': ReturnCodes.EMPTY_FIELD.value}
    else:
        intended_move = [b[0]-a[0], b[1]-a[1]]
        length = sqrt(intended_move[0]**2 + intended_move[1]**2)
        intended_move_norm = [1/length * intended_move[0], 1/length * intended_move[1]]

        # get directions of move
        for figure in pieces_config.keys():
            print(figure)
            for colour in pieces_config[figure]:
                print(colour)
                if pieces_config[figure][colour]['sign'] == piece:
                    directions_of_move = pieces_config[figure][colour]['directions_of_movement']
                    print(directions_of_move, intended_move_norm)

        if intended_move_norm not in directions_of_move:
            return {'validation': False, 'figure': None, 'message': ReturnCodes.INVALID_MOVE.value}





if __name__ == '__main__':
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

    print(move_validation([4, 2], [0, 0], test_board_2))