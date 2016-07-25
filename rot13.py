#! /usr/bin/env python2
"""
A program which uses Caesar cipher encryption technique
"""
__author__ = "Hari Raghavendar Rao"


key_cipher = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
              'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
              'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
              'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
              'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
              'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
              'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M', ' ': ' '}


class Caesar:
    """
    The main parent class of caesar cipher
    """
    def __init__(self, input_string):
        self.string = input_string

    def encode(self):
        """
        A function to encode a given string
        """
        encoded_string = ''
        for x in self.string:
            encoded_string += key_cipher[x]
        return encoded_string

    def decode(self):
        """
        A function to decode given string
        """
        decoded_string = ''
        for x in self.string:
            for key, value in key_cipher.iteritems():
                if x == value:
                    decoded_string += key
        return decoded_string

if __name__ == "__main__":
    """
    Main function
    """
    input_string_encode = raw_input("Enter the string to encode: ")
    encode = Caesar(input_string_encode)
    print "Encoded string: " + encode.encode()

    input_string_decode = raw_input("Enter the string to decode: ")
    decode = Caesar(input_string_decode)
    print "Decoded string: " + decode.decode()
