"""
main game
"""
from src.game import ChessGame

if __name__ == '__main__':

    while True:
        try:
            game = ChessGame(rand_order=True)
            game.get_intended_move()
            game.validate_move()

            break
        except Exception as e:
            print(e)
            break
