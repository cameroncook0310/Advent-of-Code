#!/usr/bin/env python3

def check_valid_idx(matrix, i, j):
    if i in range(len(matrix)) and j in range(len(matrix[i])):
        return True
    else:
        return False 

def find_xmas(matrix, curr_i, curr_j):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    xmas_count = 0
    target = "XMAS"
    for dir in directions:
        check_str = ""
        for i in range(len(target)):
            new_i = curr_i + dir[0] * i
            new_j = curr_j + dir[1] * i
            if check_valid_idx(matrix, new_i, new_j) == False:
                break
            check_str += matrix[new_i][new_j]
            if check_str not in target:
                break
        
        if check_str == target:
            xmas_count += 1

    return xmas_count

def main():
    input = open("./day 4/input.txt", "r")
    input_matrix = []

    xmas_count = 0

    for row in input:
        row = list(row.strip())
        input_matrix.append(row)

    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[i])): 
            if input_matrix[i][j] == 'X':
                #xmas_count += find_xmas(input_matrix, i, j, "",set())
                xmas_count += find_xmas(input_matrix, i, j)
    
    print(xmas_count)

if __name__ == "__main__":
    main()