from nltk.corpus import words as nltk


def encrypt(message, shift)
    res = ""

    for char in message:
        if char.isupper():
            upper_case = 65
            number_of_shifts = ((ord(char) + shift - number_of_shifts) % 26) + number_of_shifts
            res += chr(number_of_shifts)

        elif char.islower():
            lower_case = 97
            number_of_shifts = ((ord(char) + shift - number_of_shifts) % 26) + number_of_shifts
            res += chr(number_of_shifts)

        elif ord(char) == 32:
            res += ' '

        else:
            res += char

    return res