# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the
# alphabet. ROT13 is an example of the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
# characters included in the string, they should be returned as they are. Only letters from the latin/english
# alphabet should be shifted, like in the original Rot13 "implementation".
#
# Please note that using encode is considered cheating.


def rot13(message):
    result = ''
    for char in message:
        if char.isalpha() and char.isupper():
            result += chr((((ord(char) - 65) + 13) % 26) + 65)
        elif char.isalpha() and char.islower():
            result += chr((((ord(char) - 97) + 13) % 26) + 97)
        else:
            result += char
    return result
