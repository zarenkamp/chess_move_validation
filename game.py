from return_codes import ReturnCodes
import yaml
import random
from transform_input import transform_into_coordinates
from init_board import init_board
from draw_board import draw_board
from check_input import check_input, check_field


class ChessGame:

    def __init__(self, rand_order=False):

        try:
            with open("chess_figure_config.yml", "r") as ymlfile:
                self.pieces_config = yaml.load(ymlfile, Loader=yaml.FullLoader)
        except Exception as e:
            print(ReturnCodes.CONFIG_ERROR.value, e)

        self.occupied_fields = {}
        self.board, self.occupied_fields = init_board(self.pieces_config, rand_order)
        print('Board ready...')
        draw_board(self.board)

    def get_intended_move(self):

        while True:
            piece_to_move = input('Which piece to move?').upper()
            user_input = check_input(piece_to_move)
            if user_input['result']:
                check = check_field(piece_to_move, self.occupied_fields)
                if check['result']:
                    print(f'{check["colour"].capitalize()} {check["piece"].lower()} selected')
                    break
                else:
                    print(check['message'])
            else:
                print(user_input['message'])

        while True:
            target_field = input('Where to move?').upper()
            res = check_input(target_field)
            if res['result']:
                break
            else:
                print(res['message'])

        print(f'{check["colour"].capitalize()} {check["piece"].lower()} {piece_to_move} --> {target_field}')




if __name__ == '__main__':
    game = ChessGame(rand_order=True)
    game.get_intended_move()
