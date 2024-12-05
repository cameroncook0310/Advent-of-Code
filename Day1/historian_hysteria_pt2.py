#!/usr/bin/env python3

import sys

def main():
    puzzle_input = open("Day1/input.txt", "r")
    
    left_list = []
    right_list = []

    sim_score = 0
    
    # Loops through each line of the input file, splitting the numbers of that line at the whitespace and then adding each
    # number to its respective list
    for line in puzzle_input:
        line = line.strip()
        nums = line.split()
        left_list.append(int(nums[0]))
        right_list.append(int(nums[1]))

    for lnum in left_list:
        for rnum in right_list:
            if lnum == rnum:
                sim_score += lnum
    
    print(sim_score)

if __name__ == "__main__":
    main()