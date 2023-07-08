import sys
import os
from random import randint

def encrypt(cleartext, key):
    character_mapping = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4,
        'e': 5, 'f': 6, 'g': 7, 'h': 8,
        'i': 9, 'j': 10, 'k': 11, 'l': 12,
        'm': 13, 'n': 14, 'o': 15, 'p': 16,
        'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26, ' ': 100, 'A': 101,
        'B': 102, 'C': 103, 'D': 104, 'E': 105,
        'F': 106, 'G': 107, 'H': 108, 'I': 109,
        'J': 110, 'K': 111, 'L': 112, 'M': 113,
        'N': 114, 'O': 115, 'P': 116, 'Q': 117,
        'R': 118, 'S': 119, 'T': 120, 'U': 121,
        'V': 122, 'W': 123, 'X': 124, 'Y': 125,
        'Z': 126, '.': 200, '/': 201, '\\': 202,
        '$': 203, '#': 204, '@': 205, '%': 206,
        '^': 207, '*': 208, '(': 209, ')': 210,
        '_': 211, '-': 212, '=': 213, '+': 214,
        '>': 215, '<': 216, '?': 217, ';': 218,
        ':': 219, "'": 220, '"': 221, '{': 222,
        '}': 223, '[': 224, ']': 225, '|': 226,
        '`': 227, '~': 228, '!': 229, '0': 300,
        '1': 301, '2': 302, '3': 303, '4': 304,
        '5': 305, '6': 306, '7': 307, '8': 308,
        '9': 309
    }

    # Create an Initialization Vector (IV) seed value
    iv = randint(311, 457)

    encoded_buffer = []
    for character in cleartext:
        if character in character_mapping:
            encoded_buffer.append(character_mapping[character])

    print('Encoded string:', encoded_buffer)

    cipher_stream = []
    cipher_stream.append(iv)  # Prepend the IV unencrypted
    composite_key = iv + int(key)  # Composite key: IV + key

    for value in encoded_buffer:
        encrypted_byte = (3 * value) + composite_key
        cipher_stream.append(encrypted_byte)

    print('Encrypted string:', cipher_stream)
    return cipher_stream

def main():
    if len(sys.argv) < 3:
        print('Usage: python3 filename.py <cleartext> <key>')
        return

    cleartext = sys.argv[1]
    key = sys.argv[2]

    cipher_stream = encrypt(cleartext, key)

    # Write encrypted list to a file
    print('Writing encrypted list to file: encrypted.txt')
    with open('encrypted.txt', 'w') as encrypted_file:
        encrypted_file.write(str(cipher_stream))

if __name__ == '__main__':
    main()
