# 2.1 Caesar
def encrypt_caesar_cipher(plaintext):
    if plaintext:
        return "".join((right_shift(char, 3) for char in plaintext))
    else:
        return ""


def decrypt_caesar_cipher(ciphertext):
    if ciphertext:
        return "".join((left_shift(char, 3) for char in ciphertext))
    else:
        return ""


# 2.2 Vigenere
def encrypt_vigenere_cipher(plaintext, keyword):
    if plaintext and keyword:
        keyword = repeat_or_trim(keyword, len(plaintext))
        return "".join((right_shift(plaintext_char, ord(keyword_char) - ord('A'))) for plaintext_char, keyword_char in
                       zip(plaintext, keyword))
    else:
        return ""


def decrypt_vigenere_cipher(ciphertext, keyword):
    if ciphertext and keyword:
        keyword = repeat_or_trim(keyword, len(ciphertext))
        return "".join((left_shift(ciphertext_char, ord(keyword_char) - ord('A'))) for ciphertext_char, keyword_char in
                       zip(ciphertext, keyword))
    else:
        return ""


# 2.3 Morse
morse_code = {
    ' ': ' ',
    'A': '. ---',
    'B': '--- . . .',
    'C': '--- . --- .',
    'D': '--- . .',
    'E': '.',
    'F': '. . --- .',
    'G': '--- --- .',
    'H': '. . . .',
    'I': '. .',
    'J': '. --- --- ---',
    'K': '--- . ---',
    'L': '. --- . .',
    'M': '--- ---',
    'N': '--- .',
    'O': '--- --- ---',
    'P': '. --- --- .',
    'Q': '--- --- . ---',
    'R': '. --- .',
    'S': '. . .',
    'T': '---',
    'U': '. . ---',
    'V': '. . . ---',
    'W': '. --- ---',
    'X': '--- . . ---',
    'Y': '--- . --- ---',
    'Z': '--- --- . .',
    '1': '. --- --- --- ---',
    '2': '. . --- --- ---',
    '3': '. . . --- ---',
    '4': '. . . . ---',
    '5': '. . . . .',
    '6': '--- . . . .',
    '7': '--- --- . . .',
    '8': '--- --- --- . .',
    '9': '--- --- --- --- .',
    '0': '--- --- --- --- ---'
}
space = ' '
char_space = 3 * space
word_space = 7 * space
inverted_morse_code = {v: k for k, v in morse_code.items()}


def encrypt_morse_code(plaintext):
    return char_space.join((morse_code[char] for char in plaintext))


def decrypt_morse_code(ciphertext):
    return space.join(decrypt_morse_word(word) for word in make_morse_list(ciphertext))


############################### Helper functions ##########################################

def right_shift(char, shift):
    shift = shift % 26
    if ord(char) < ord('A') or ord(char) > ord('Z'):
        return char
    elif ord(char) <= ord('Z') - shift:
        return chr(ord(char) + shift)
    else:
        return chr(ord(char) + (shift - 1) - (ord('Z') - (ord('A'))))


def left_shift(char, shift):
    shift = shift % 26
    if ord(char) < ord('A') or ord(char) > ord('Z'):
        return char
    elif ord(char) >= ord('A') + shift:
        return chr(ord(char) - shift)
    else:
        return chr(ord(char) - (shift - 1) + (ord('Z') - (ord('A'))))


def repeat_or_trim(keyword, text_length):
    return (keyword * (text_length // len(keyword) + 1))[:text_length]


def make_morse_list(morsetext):
    morse_words = morsetext.split(word_space)
    morse_chars = [word.split(char_space) for word in morse_words]
    return morse_chars


def decrypt_morse_word(morse_word):
    decrypted_word = ''.join((inverted_morse_code[morse_char] for morse_char in morse_word))
    return decrypted_word


def main():
    # cipher = encrypt_caesar_cipher("PYTHON")
    # cipher2 = encrypt_caesar_cipher("F1RST P0ST")
    # print(cipher)
    # print(cipher2)
    # decrypted = decrypt_caesar_cipher(cipher)
    # decrypted2 = decrypt_caesar_cipher(cipher2)
    # print(decrypted)
    # print(decrypted2)
    # print(encrypt_caesar_cipher(""))
    # print(decrypt_caesar_cipher(""))

    # cipher3 = encrypt_vigenere_cipher("ATTACKATDAWN", "LEMON")
    # print(cipher3)
    # decrypted3 = decrypt_vigenere_cipher(cipher3, "LEMON")
    # print(decrypted3)

    cipher4 = encrypt_morse_code("MEET ME AT MIDNIGHT")
    print(cipher4)
    print(make_morse_list(cipher4))
    decrypted4 = decrypt_morse_code(cipher4)
    print(decrypted4)


if __name__ == '__main__':
    main()
