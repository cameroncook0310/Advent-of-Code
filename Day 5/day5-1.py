#!/usr/bin/env python3

def create_order_map(rules):
    order_map = {}
    for rule in rules:
        rule = rule.strip().split("|")
        if rule[0] in order_map.keys():
            order_map[rule[0]].add(rule[1])
        else:
            order_map[rule[0]] = set([rule[1]])
    
    return order_map


def check_correct_ordering(order_map, update):

    for i in range(len(update)):
        for j in range(len(update[i:])):
            curr_num = update[i]
            future_num = update[i:][j]
            if future_num in order_map.keys() and curr_num in order_map[future_num]:
                return False

    return True


def get_middle_num(lst):
    length = len(lst)
    return int(lst[(length // 2)])


def main():
    input = open("./Day 5/input.txt", "r")
    input_txt = input.read()

    rules, page_numbers = input_txt.split("\n\n")
    rules = rules.split("\n")
    page_numbers = page_numbers.split("\n")
    
    order_map = create_order_map(rules)

    middle_sum = 0

    for update in page_numbers:
        update = update.split(",")
        if check_correct_ordering(order_map, update):
            middle_sum += get_middle_num(update)
            
    print(middle_sum)
    input.close()

if __name__ == "__main__":
    main()