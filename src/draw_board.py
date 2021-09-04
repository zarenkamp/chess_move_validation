from termcolor import colored
import colorama
colorama.init()


def draw_board(board: list):

    insert_board = []
    color_white_figs = 'yellow'
    color_black_figures = 'red'

    for index_row, row in enumerate(board):
        for index_col, piece in enumerate(row):

            if type(piece) == dict:
                if piece['colour'] == 'white':
                    insert_board.append(colored(piece['sign'], color_white_figs))
                else:
                    insert_board.append(colored(piece['sign'], color_black_figures))
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

    t2 = [[{'piece': 'ROOK', 'colour': 'black', 'sign': 'R'}, '+', {'piece': 'BISHOP', 'colour': 'black', 'sign': 'R'}, '+', '+', {'piece': 'BISHOP', 'colour': 'black', 'sign': 'R'}, '+', {'piece': 'ROOK', 'colour': 'black', 'sign': 'R'}], [{'piece': 'PAWN', 'colour': 'black', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'black', 'sign': 'R'}], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], ['+', '+', '+', '+', '+', '+', '+', '+'], [{'piece': 'PAWN', 'colour': 'white', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'R'}, {'piece': 'PAWN', 'colour': 'white', 'sign': 'R'}], [{'piece': 'ROOK', 'colour': 'white', 'sign': 'R'}, '+', {'piece': 'BISHOP', 'colour': 'white', 'sign': 'R'}, '+', '+', {'piece': 'BISHOP', 'colour': 'white', 'sign': 'R'}, '+', {'piece': 'ROOK', 'colour': 'white', 'sign': 'R'}]]


    draw_board(t2)
