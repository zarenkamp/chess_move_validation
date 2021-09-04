from enum import Enum


class ReturnCodes(Enum):
    SUCCESS = 'Valid move, go on.'
    INVALID_MOVE = 'Invalid move, please read the chess instructions again.'
    MOVE_BLOCKED_OWN = f'Own figure blocks move.'
    BEAT_FIGURE = 'Valid move, beat opponents figure!'
    WRONG_INPUT_FORMAT = "Wrong input. The first character must be a letter from A-H," \
                         " the second one a number from 1-8."
    EMPTY_FIELD = 'Empty field selected.'
    SAME_COORDINATES = 'Input coordinates are identical.'
    ENTRY_NOT_FOUND = 'Entry not found.'
    CONFIG_ERROR = 'Config not found!'
    INVALID_COORDINATES = 'Coordinates invalid.'
