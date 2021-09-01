from return_codes import ReturnCodes

def transform_into_coordinates(letter_plus_code: str):
    # transforms from normal board view down side letters A-H, sides count from 1-8 to a system where 0,0 is the upper
    # left corner
    mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
               '1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    letter_plus_code = letter_plus_code.upper()
    if len(letter_plus_code) == 2\
            and letter_plus_code[0].isalpha()\
            and letter_plus_code[0] in mapping.keys()\
            and letter_plus_code[1].isnumeric()\
            and letter_plus_code[1] in mapping.keys():
        return mapping[letter_plus_code[1]], mapping[letter_plus_code[0]]  # row index before column index
    else:
        return ReturnCodes.WRONG_INPUT_FORMAT.value


if __name__ == '__main__':
    num_1 = input("first try")
    print(transform_into_coordinates(num_1))
