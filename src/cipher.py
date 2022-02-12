from nltk.corpus import words as nltk

def encrypt(message, shift):
    res = ""

    for char in message:
        if char.isupper():
            key = 65
            number_of_shifts = ((ord(char) + shift - key) % 26) + key
            res += chr(number_of_shifts)

        elif char.islower():
            key = 97
            number_of_shifts = ((ord(char) + shift - key) % 26) + key
            res += chr(number_of_shifts)

        elif ord(char) == 32:
            res += ' '

        else:
            res += char

    return res


def decrypt(message, shift):
    return encrypt(message, 26-shift)


def crack(message):
    word_list = nltk.words()
    res = ''
    max_words_matched = 0

    for shift in range(1,26):
        decrypted = decrypt(message, shift)
        words_matched = 0
        for word in decrypted.split(' '):
            if word in word_list:
                words_matched += 1
        
        #### Check for 50% Match ####
        if words_matched > len(message) // 2:
            return decrypted
        
        #### Return the match with most words ####
        elif words_matched > max_words_matched:
            max_words_matched = words_matched
            res = decrypted
            
    return res

if __name__ == '__main__':

    shift = 10
    message = 'Lets make it funky'
    print(f'message: {message}')
    encrypted = encrypt(message, shift)

    print(f'encrypting: {encrypted}')
    decrypted = decrypt(encrypted, shift)
    print(f'decrypted: {decrypted}')

    print(f'decrypting with no shift: {encrypted}')
    cracked = crack(encrypted)
    print(f'Message Cracked: {cracked}')