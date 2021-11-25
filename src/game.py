import yaml
import pathlib
from src.return_codes import ReturnCodes
from src.init_board import init_board
from src.draw_board import draw_board
from src.check_input import check_input, check_field
from src.move_validation import move_validation


class ChessGame:
    """
    Main game class
    """

    def __init__(self, rand_order=False):
        """
        Initializes the game by calling init_board.
        :param rand_order: user can decide whether the figures are placed according to initial positions in
        chess_figures_config, or placed randomly
        """

        try:
            with open(pathlib.Path(__file__).parent.parent / "chess_figures_config.yml", "r") as ymlfile:
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
        """
        Takes in user input via command line. Prevents wrong inputs.
        :return: returns valid field coordinates
        """

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

        print(f'Intended move: {check["colour"].capitalize()} {check["piece"].capitalize()}'
              f' {self.starting_field} --> {self.target_field}')

        return self.starting_field, self.target_field

    def validate_move(self):
        """
        Validates the intended move by calling check_move
        :return:
        """
        if self.starting_field and self.target_field:
            check_move = move_validation(self.starting_field, self.target_field, self.occupied_fields)
            if 'PIECE' and 'FIELD' in check_move['message']:
                message = check_move['message'].replace('PIECE', check_move['piece'].capitalize())\
                                               .replace('FIELD', check_move['field'].capitalize())
                print(message)
                return {'result': True, 'message': message}
            else:
                message = check_move['message']
                print(message)
                return {'result': True, 'message': message}
        else:
            print('Values not set yet, please choose first!')
            return {'result': False, 'message': ReturnCodes.NO_FIELDS_SELECTED.value}

    def display_board(self):
        """
        Displays board in command line.
        :return: None
        """
        draw_board(self.board)


if __name__ == '__main__':
    game = ChessGame(rand_order=True)
    game.get_intended_move()
    game.validate_move()
