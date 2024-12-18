#!/usr/bin/env python3

def check_valid_idx(matrix, i, j):
    if i in range(len(matrix)) and j in range(len(matrix[i])):
        return True
    else:
        return False 

def is_xmas_cross(matrix, curr_i, curr_j):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    target_set = set(["M", "A", "S"])
    left_diag_set = set(["A"])
    right_diag_set = set(["A"])

    for dir in directions:
        new_i = curr_i + dir[0]
        new_j = curr_j + dir[1]
        if check_valid_idx(matrix, new_i, new_j) == False:
            return False
        if dir in [(-1, -1), (1, 1)]:
            left_diag_set.add(matrix[new_i][new_j])
        else:
            right_diag_set.add(matrix[new_i][new_j])

    return left_diag_set == target_set and right_diag_set == target_set

def main():
    input = open("./day 4/input.txt", "r")
    input_matrix = []

    xmas_count = 0

    for row in input:
        row = list(row.strip())
        input_matrix.append(row)

    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[i])): 
            if input_matrix[i][j] == 'A' and is_xmas_cross(input_matrix, i, j):
                xmas_count += 1
    
    print(xmas_count)

if __name__ == "__main__":
    main()