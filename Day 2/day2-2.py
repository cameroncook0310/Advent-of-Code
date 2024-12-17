#!/usr/bin/env python3


### INCOMPLETE

# Takes a single level as input and returns True or False based on
# whether the level is safe or not
def is_safe(level):
    level = level.strip()
    level = level.split()

    prev_num = level[0] 

    error_count = 0
    
    is_initially_positive_difference = (int(level[1]) - int(level[0])) > 0

    first_i = True

    for num in level[1:]:

        diff = int(num) - int(prev_num)
        abs_diff = abs(diff)

        is_positive_difference = diff > 0

        if is_positive_difference != is_initially_positive_difference or diff == 0 or abs_diff > 3 or abs_diff < 1:
            error_count += 1



            continue

        prev_num = num

        first_i = False
        

    return (error_count < 2)


def main():
    input = open('./day 2/input.txt', 'r')

    safe_count = 0

    for level in input:
        if is_safe(level):
            safe_count += 1

    print(safe_count)

if __name__ == "__main__":
    main()
