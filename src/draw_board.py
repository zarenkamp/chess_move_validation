from termcolor import colored
import colorama
import yaml
import pathlib
colorama.init()


def draw_board(board: list):
    """
    Takes board list as input, colours the pieces and the fields
    :param board: list with all pieces and empty fields
    :return:
    """

    insert_board = []
    color_white_figs = 'yellow'  # available: grey, red, green, yellow, blue, magenta, cyan, white
    color_black_figures = 'red'

    with open(pathlib.Path(__file__).parent / "ascii_codes_figures.yaml", "r") as ymlfile:
        ascii_codes = yaml.load(ymlfile, Loader=yaml.FullLoader)
    for index_row, row in enumerate(board):
        for index_col, piece in enumerate(row):
            if type(piece) == dict:
                # piece is element in board list, either a dict with a figure or just a '+'
                if piece['colour'] == 'white':
                    insert_board.append(colored(ascii_codes[piece['piece']], color_white_figs))
                else:
                    insert_board.append(colored(ascii_codes[piece['piece']], color_black_figures))
            else:
                if index_row % 2 != 0 and index_col % 2 != 0 or index_row % 2 == 0 and index_col % 2 == 0:
                    insert_board.append(colored(piece, 'white'))
                else:
                    insert_board.append(colored(piece, 'grey'))

    print("   A B C D E F G H\n"
          "   ---------------\n"
          "8 |{} {} {} {} {} {} {} {}| 8\n"
          "7 |{} {} {} {} {} {} {} {}| 7\n"
          "6 |{} {} {} {} {} {} {} {}| 6\n"
          "5 |{} {} {} {} {} {} {} {}| 5\n"
          "4 |{} {} {} {} {} {} {} {}| 4\n"
          "3 |{} {} {} {} {} {} {} {}| 3\n"
          "2 |{} {} {} {} {} {} {} {}| 2\n"
          "1 |{} {} {} {} {} {} {} {}| 1\n"
          "   ---------------\n"
          "   A B C D E F G H".format(*insert_board))


if __name__ == '__main__':
    b = [[{'piece': 'ROOK', 'colour': 'black', 'sign': 'R'}, {'piece': 'KNIGHT', 'colour': 'black', 'sign': 'N'}, {'piece': 'BISHOP', 'colour': 'black', 'sign': 'B'}, {'piece': 'QUEEN', 'colour': 'black', 'sign': 'Q'}, {'piece': 'KING', 'colour': 'black', 'sign': 'K'}, {'piece': 'BISHOP', 'colour': 'black', 'sign': 'B'}, {'piece': 'KNIGHT', 'colour': 'black', 'sign': 'N'}, {'piece': 'ROOK', 'colour': 'black', 'sign': 'R'}], [{'piece': 'PAWN', 'colour': 'black', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'P'}], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], [{'piece': 'PAWN', 'colour': 'white', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'P'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'P'}], [{'piece': 'ROOK', 'colour': 'white', 'sign': 'R'}, {'piece': 'KNIGHT', 'colour': 'white', 'sign': 'N'}, {'piece': 'BISHOP', 'colour': 'white', 'sign': 'B'}, {'piece': 'QUEEN', 'colour': 'white', 'sign': 'Q'}, {'piece': 'KING', 'colour': 'white', 'sign': 'K'}, {'piece': 'BISHOP', 'colour': 'white', 'sign': 'B'}, {'piece': 'KNIGHT', 'colour': 'white', 'sign': 'N'}, {'piece': 'ROOK', 'colour': 'white', 'sign': 'R'}]]
    draw_board(b)