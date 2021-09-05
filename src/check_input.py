from src.return_codes import ReturnCodes


def check_input(letter_plus_code: str) -> dict:
    """
    Checks if user input is valid.
    :param letter_plus_code: user input as string in the form: 'F4', 'A3', etc.
    :return: dict including result as bool and return message
    """
    valid_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    valid_numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    letter_plus_code = letter_plus_code.upper()
    if len(letter_plus_code) == 2\
            and letter_plus_code[0].isalpha()\
            and letter_plus_code[0] in valid_letters\
            and letter_plus_code[1].isnumeric()\
            and letter_plus_code[1] in valid_numbers:
        return {'result': True, 'message': None}
    else:
        return {'result': False, 'message': ReturnCodes.WRONG_INPUT_FORMAT.value}


def check_field(field: str, occupied_fields: dict) -> dict:
    """
    Checks if there is already a piece at the given field by searching the keys of occupied_fields dict.
    :param field: field as string in the form
    :param occupied_fields: 'F4', 'A3', etc.
    :return: dict including result as bool and return message
    """
    if field in occupied_fields.keys():
        return {'result': True, 'message': None, 'piece': occupied_fields[field]['piece'],
                                                 'colour': occupied_fields[field]['colour']}
    else:
        return {'result': False, 'message': ReturnCodes.EMPTY_FIELD.value, 'piece': None, 'colour': None}


if __name__ == '__main__':
    pass
