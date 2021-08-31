from termcolor import colored
import colorama
colorama.init()


def draw_board(board):

    insert_board = [colored(field[0], color_piece(field)) for row in board for field in row]

    print("8 |{} {} {} {} {} {} {} {}\n"
          "7 |{} {} {} {} {} {} {} {}\n"
          "6 |{} {} {} {} {} {} {} {}\n"
          "5 |{} {} {} {} {} {} {} {}\n"
          "4 |{} {} {} {} {} {} {} {}\n"
          "3 |{} {} {} {} {} {} {} {}\n"
          "2 |{} {} {} {} {} {} {} {}\n"
          "1 |{} {} {} {} {} {} {} {}\n"
          "   ---------------\n"
          "   A B C D E F G H".format(*insert_board))


def color_piece(piece_to_color):

    if 'w' in piece_to_color:
        return 'yellow'
    elif 'b' in piece_to_color:
        return 'blue'
    else:
        return 'grey'





if __name__ == '__main__':

    test_board = [['Rb', 'Nb', 'Bb', 'Qb', 'Nb', 'Bb', 'Nb', 'Rb'],
                  ['Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb'],
                  [ '0',  '0',  '0',  '0',  '0',  '0',  '0',  '0'],
                  [ '0',  '0',  '0',  '0',  '0',  '0',  '0',  '0'],
                  [ '0',  '0',  '0',  '0',  '0',  '0',  '0',  '0'],
                  [ '0',  '0',  '0',  '0',  '0',  '0',  '0',  '0'],
                  ['Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw'],
                  ['Rw', 'Nw', 'Bw', 'Qw', 'Kw', 'Bw', 'Nw', 'Rw']]

    draw_board(test_board)
