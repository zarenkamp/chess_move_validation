from src.transform_input import transform_into_coordinates


def fill_board(occupied_fields: dict, board: list) -> list:
    """
    Fills the board with all the pieces in occupied fields dict. Each entry is a tuple including the piece, its colour
    and its sign.
    :param occupied_fields: dict with all occupied fields and the pieces on them
    :param board: list of all fields of the board
    :return: board list with new positions of pieces
    """
    for field in occupied_fields.keys():
        coordinates = transform_into_coordinates(field)['value']
        board[coordinates[0]][coordinates[1]] = {'piece': occupied_fields[field]['piece'],
                                                 'colour': occupied_fields[field]['colour'],
                                                 'sign': occupied_fields[field]['sign']}
    return board


if __name__ == '__main__':
    o = {'A2': {'piece': 'PAWN', 'colour': 'white', 'dir': [[1, 0]], 'sign': 'R'}, 'B2': {'piece': 'PAWN', 'colour': 'white', 'dir': [[1, 0]], 'sign': 'R'}, 'C2': {'piece': 'PAWN', 'colour': 'white', 'dir': [[1, 0]], 'sign': 'R'}, 'D2': {'piece': 'PAWN', 'colour': 'white', 'dir': [[1, 0]], 'sign': 'R'}, 'E2': {'piece': 'PAWN', 'colour': 'white', 'dir': [[1, 0]], 'sign': 'R'}, 'F2': {'piece': 'PAWN', 'colour': 'white', 'dir': [[1, 0]], 'sign': 'R'}, 'G2': {'piece': 'PAWN', 'colour': 'white', 'dir': [[1, 0]], 'sign': 'R'}, 'H2': {'piece': 'PAWN', 'colour': 'white', 'dir': [[1, 0]], 'sign': 'R'}, 'A7': {'piece': 'PAWN', 'colour': 'black', 'dir': [[-1, 0]], 'sign': 'R'}, 'B7': {'piece': 'PAWN', 'colour': 'black', 'dir': [[-1, 0]], 'sign': 'R'}, 'C7': {'piece': 'PAWN', 'colour': 'black', 'dir': [[-1, 0]], 'sign': 'R'}, 'D7': {'piece': 'PAWN', 'colour': 'black', 'dir': [[-1, 0]], 'sign': 'R'}, 'E7': {'piece': 'PAWN', 'colour': 'black', 'dir': [[-1, 0]], 'sign': 'R'}, 'F7': {'piece': 'PAWN', 'colour': 'black', 'dir': [[-1, 0]], 'sign': 'R'}, 'G7': {'piece': 'PAWN', 'colour': 'black', 'dir': [[-1, 0]], 'sign': 'R'}, 'H7': {'piece': 'PAWN', 'colour': 'black', 'dir': [[-1, 0]], 'sign': 'R'}, 'A1': {'piece': 'ROOK', 'colour': 'white', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R'}, 'H1': {'piece': 'ROOK', 'colour': 'white', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R'}, 'A8': {'piece': 'ROOK', 'colour': 'black', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R'}, 'H8': {'piece': 'ROOK', 'colour': 'black', 'dir': [[1, 0], [-1, 0], [0, 1], [0, -1]], 'sign': 'R'}, 'C1': {'piece': 'BISHOP', 'colour': 'white', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'R'}, 'F1': {'piece': 'BISHOP', 'colour': 'white', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'R'}, 'C8': {'piece': 'BISHOP', 'colour': 'black', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'R'}, 'F8': {'piece': 'BISHOP', 'colour': 'black', 'dir': [[1, 1], [1, -1], [-1, 1], [-1, -1]], 'sign': 'R'}}
    b = [['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+']]

    print(fill_board(o, b))
