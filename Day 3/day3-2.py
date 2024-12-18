#!/usr/bin/env python3

import re

def mul(num1, num2):
    return int(num1) * int(num2)

def main():
    input = open("./day 3/input.txt", "r")
    input_text = input.read()

    valid_funcs = re.findall("don't\(\)|do\(\)|mul\(\d+,\d+\)",input_text)

    muls_sum = 0
    
    mul_enabled = True
    for curr_func in valid_funcs:
        if curr_func == "do()":
            mul_enabled = True
        elif curr_func == "don't()":
            mul_enabled = False
        elif mul_enabled:
            muls_sum += eval(curr_func)
    
    print(muls_sum)

if __name__ == "__main__":
    main()