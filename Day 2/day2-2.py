#!/usr/bin/env python3

# Takes a single level as input and returns True or False based on
# whether the level is safe or not
def is_safe(level):

    prev_num = level[0] 

    safe_distance = True
    mono_seq = True
    
    is_initially_positive_difference = (int(level[1]) - int(level[0])) > 0

    for num in level[1:]:
        diff = int(num) - int(prev_num)
        abs_diff = abs(diff)

        is_positive_difference = diff > 0

        if is_positive_difference != is_initially_positive_difference or diff == 0:
            mono_seq = False

        if abs_diff > 3 or abs_diff < 1:
            safe_distance = False
        
        prev_num = num
        

    return (safe_distance and mono_seq)


def main():
    input = open('./day 2/input.txt', 'r')

    safe_count = 0

    for level in input:
        level = level.strip()
        level = level.split()
        safe_level_found = False
        if is_safe(level):
            safe_level_found = True
        else:
            for i in range(len(level)):
                sub_level = level[:i] + level[i+1:]
                if is_safe(sub_level):
                    safe_level_found = True
                    break
        
        if safe_level_found:
            safe_count += 1
        
    print(safe_count)

if __name__ == "__main__":
    main()
