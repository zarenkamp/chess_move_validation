from return_codes import ReturnCodes


def transform_into_coordinates(letter_plus_code: str):
    # transforms from normal board view down side letters A-H, sides count from 1-8 to a system where 0,0 is the upper
    # left corner to simplify iteration over nested list
    mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
               '1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    letter_plus_code = letter_plus_code.upper()
    if len(letter_plus_code) == 2\
            and letter_plus_code[0].isalpha()\
            and letter_plus_code[0] in mapping.keys()\
            and letter_plus_code[1].isnumeric()\
            and letter_plus_code[1] in mapping.keys():
        return [mapping[letter_plus_code[1]], mapping[letter_plus_code[0]]]  # row index before column index
    else:
        return ReturnCodes.WRONG_INPUT_FORMAT.value


def transform_into_code(coordinates):
    first_digit = {0: '8', 1: '7', 2: '6', 3: '5', 4: '4', 5: '3', 6: '2', 7: '1'}
    second_digit = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}

    if coordinates[0] in first_digit.keys() and coordinates[1] in second_digit.keys():
        return {'result': True, 'message': None, 'value': second_digit[coordinates[1]] + first_digit[coordinates[0]]}
    else:
        return {'result': False, 'message': ReturnCodes.INVALID_COORDINATES.value, 'value': None}

if __name__ == '__main__':

    print(type(transform_into_code([4, 5])))
