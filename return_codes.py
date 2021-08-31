from enum import Enum


class ReturnCodes(Enum):
    SUCCESS = 'Valid move, go on.'
    INVALID_MOVE = 'Invalid move, please read the chess instructions again'
    MOVE_BLOCKED_OWN = f'Move blocked through own figure'
    BEAT_FIGURE = 'Valid move, beat opponents figure'
    WRONG_INPUT_FORMAT = "Wrong input format. The first character must be a letter from A-H," \
                         " the second one a number from 1-8"

