#!/usr/bin/env python3

import re

def mul(num1, num2):
    return int(num1) * int(num2)

def main():
    input = open("./day 3/input.txt", "r")
    input_text = input.read()

    valid_muls = re.findall("mul\(\d+,\d+\)", input_text)

    muls_sum = 0

    for curr_mul in valid_muls:
        muls_sum += eval(curr_mul)
    
    print(muls_sum)

if __name__ == "__main__":
    main()