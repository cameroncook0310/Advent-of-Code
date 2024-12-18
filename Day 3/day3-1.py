#!/usr/bin/env python3


def main():
    input = open("./day 3/input.txt", "r")
    input_text = input.read()

    l_point = 0
    r_point = 0

    input_length = len(input_text)

    while l_point < len(input_text):
        print(input_text[l_point])

        l_point += 1


if __name__ == "__main__":
    main()