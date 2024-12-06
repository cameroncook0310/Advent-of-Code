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

    occurrance_map = {}

    for i in range(len(left_list)):
        left_num = left_list[i]
        right_num = right_list[i]

        if left_num in occurrance_map.keys():
            occ_counts = occurrance_map[left_num]
            occurrance_map[left_num] = (occ_counts[0] + 1, occ_counts[1])

        else:
            occurrance_map[left_num] = (1, 0)

        if right_num in occurrance_map.keys():
            occ_counts = occurrance_map[right_num]
            occurrance_map[right_num] = (occ_counts[0], occ_counts[1] + 1)

        else:
            occurrance_map[right_num] = (0, 1)


    for num, occs in occurrance_map.items():
        l_occ, r_occ = occs
        sim_score += l_occ * (num * r_occ)

    print(sim_score)

if __name__ == "__main__":
    main()