import yaml
from src.return_codes import ReturnCodes
from src.init_board import init_board
from src.draw_board import draw_board
from src.check_input import check_input, check_field
from src.move_validation import move_validation


class ChessGame:

    def __init__(self, rand_order=False):
        """

        :param rand_order:
        """

        try:
            with open("chess_figures_config.yml", "r") as ymlfile:
                self.pieces_config = yaml.load(ymlfile, Loader=yaml.FullLoader)
            self.occupied_fields = {}
            self.board, self.occupied_fields = init_board(self.pieces_config, rand_order)
            self.starting_field = ''
            self.target_field = ''
            print('Board ready...')
            draw_board(self.board)

        except Exception as e:
            print(ReturnCodes.CONFIG_ERROR.value, e)

    def get_intended_move(self):

        while True:
            self.starting_field = input('Which piece to move?').upper()
            user_input = check_input(self.starting_field)
            if user_input['result']:
                check = check_field(self.starting_field, self.occupied_fields)
                if check['result']:
                    print(f'{check["colour"].capitalize()} {check["piece"].capitalize()} selected')
                    break
                else:
                    print(check['message'])
            else:
                print(user_input['message'])

        while True:
            self.target_field = input('Where to move?').upper()
            res = check_input(self.target_field)
            if res['result']:
                if self.target_field == self.starting_field:
                    print(ReturnCodes.SAME_COORDINATES.value)
                else:
                    break
            else:
                print(res['message'])

        print(f'{check["colour"].capitalize()} {check["piece"].capitalize()} {self.starting_field} --> {self.target_field}')
        return self.starting_field, self.target_field

    def validate_move(self):
        """
        Validates intended move from a to b
        :param a:
        :param b:
        :return:
        """
        if self.starting_field and self.target_field:
            check_move = move_validation(self.starting_field, self.target_field, self.occupied_fields)
            print(check_move['message'])
        else:
            print('Values not set yet, please choose first!')


if __name__ == '__main__':
    game = ChessGame(rand_order=True)
    game.get_intended_move()
    game.validate_move()
