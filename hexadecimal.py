#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: December 2019
# This program finds the hexadecimals of a word


def convert(word):
    # this function finds the hexadecimals of a word
    hexadecimal = {}
    converted = []

    # adding items
    hexadecimal['a'] = "61"
    hexadecimal['b'] = "62"
    hexadecimal['c'] = "63"
    hexadecimal['d'] = "64"
    hexadecimal['e'] = "65"
    hexadecimal['f'] = "66"
    hexadecimal['g'] = "67"
    hexadecimal['h'] = "68"
    hexadecimal['i'] = "69"
    hexadecimal['j'] = "6a"
    hexadecimal['k'] = "6b"
    hexadecimal['l'] = "6c"
    hexadecimal['m'] = "6d"
    hexadecimal['n'] = "6e"
    hexadecimal['o'] = "6f"
    hexadecimal['p'] = "70"
    hexadecimal['q'] = "71"
    hexadecimal['r'] = "72"
    hexadecimal['s'] = "73"
    hexadecimal['t'] = "74"
    hexadecimal['u'] = "75"
    hexadecimal['v'] = "76"
    hexadecimal['w'] = "77"
    hexadecimal['x'] = "78"
    hexadecimal['y'] = "79"
    hexadecimal['z'] = "7a"

    for counter in word:
        if counter in hexadecimal.keys():
            converted.append(hexadecimal[counter])
        else:
            print("Not in the dictionary. Try again.")

    return converted


def main():
    # this function shows the hexadecimal

    # input
    word = input("Enter a word: ")

    # process
    converted = convert(word)

    # output
    for counter in converted:
        print(counter, end=" ")


if __name__ == "__main__":
    main()
