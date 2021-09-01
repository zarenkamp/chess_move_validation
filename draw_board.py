from termcolor import colored
import colorama
colorama.init()


def draw_board(board: list):

    insert_board = []

    for index_row, row in enumerate(board):
        for index_col, piece in enumerate(row):
            insert_board.append(colored(piece[0], color_piece(piece, index_row, index_col)))

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


def color_piece(piece_to_color, row_index, col_index):

    if 'w' in piece_to_color:
        return 'yellow'
    elif 'b' in piece_to_color:
        return 'red'
    elif row_index % 2 != 0 and col_index % 2 != 0 or row_index % 2 == 0 and col_index % 2 == 0:
        return 'white'
    else:
        return 'grey'





if __name__ == '__main__':

    test_board = [['Rb', 'Nb', 'Bb', 'Qb', 'Nb', 'Bb', 'Nb', 'Rb'],
                  ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
                  [ '+',  '+',  '+',  '+',  '+',  '+',  '+',  '+'],
                  [ '+',  '+',  '+',  '+',  '+',  '+',  '+',  '+'],
                  [ '+',  '+',  '+',  '+',  '+',  '+',  '+',  '+'],
                  [ '+',  '+',  '+',  '+',  '+',  '+',  '+',  '+'],
                  ['Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw'],
                  ['Rw', 'Nw', 'Bw', 'Qw', 'Kw', 'Bw', 'Nw', 'Rw']]

    test_board_1 = [['Rb', '+', 'Bb', 'Qb', 'Nb', 'Bb', 'Nb', 'Rb'],
                  ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
                  ['+', '+', 'Nb', '+', '+', '+', '+', '+'],
                  ['+', '+', '+', '+', '+', '+', '+', '+'],
                  ['+', '+', '+', 'Pw', 'Bw', '+', '+', '+'],
                  ['+', '+', '+', '+', '+', '+', '+', '+'],
                  ['Pw', 'Pw', 'Pw', '+', 'Pw', 'Pw', 'Pw', 'Pw'],
                  ['Rw', 'Nw', '+', 'Qw', 'Kw', 'Bw', 'Nw', 'Rw']]



    draw_board(test_board_1)
