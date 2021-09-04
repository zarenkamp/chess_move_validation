"""
main game, run from ide or from console with 'python path_to_dir/main.py'
"""
from src.game import ChessGame

if __name__ == '__main__':
    try:
        while True:
            while True:
                rand_order = input('Place pieces randomly? y/n')
                if rand_order not in ['n', 'y']:
                    print('Wrong input!')
                    continue
                else:
                    if rand_order == 'y':
                        rand_order = True
                    else:
                        rand_order = False
                    break

            game = ChessGame(rand_order)

            while True:

                game.get_intended_move()
                game.validate_move()
                while True:
                    new_try = input('Another try -> 1, new board -> 2, quit game -> 3?')

                    if new_try not in ['1', '2', '3']:
                        print('Wrong input!')
                        continue
                    else:
                        break

                if new_try == '1':
                    continue
                else:
                    break
            if new_try == '2':
                continue
            else:
                break

    except Exception as e:
        print(e)

