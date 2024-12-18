#!/usr/bin/env python3

import sys

def main():
    # The input for this puzzle is a string with two lists (columns) of numbers seperated by whitespace
    puzzle_input = open("input.txt", "r")

    left_list = []
    right_list = []

    dist_sum = 0
    
    # Loops through each line of the input file, splitting the numbers of that line at the whitespace and then adding each
    # number to its respective list
    for line in puzzle_input:
        line = line.strip()
        nums = line.split()
        left_list.append(int(nums[0]))
        right_list.append(int(nums[1]))

    # Sorts both lists
    left_list.sort()
    right_list.sort()

    # Iterates trough each sorted list adding up the difference between each number pair
    for i in range(len(left_list)):
        dist = abs(left_list[i] - right_list[i])
        dist_sum += dist
       
    print(dist_sum)

    puzzle_input.close()


if __name__ == "__main__":
    main()
