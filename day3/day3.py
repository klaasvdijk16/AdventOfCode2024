import re

def read_data():
    with open('day3/input.txt', 'r') as f:
        return f.read()

def parse_input(input_string, part):
    if part == 1:
        res = re.findall("mul\((\d+),(\d+)\)", input_string)
    else:
        res = re.findall("mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", input_string)
        res = [tuple(item for item in t if item) for t in res] # remove empty strings in tuples
    return res

def calculate_from_tuple_list(tuple_list):
    total = 0
    enabled = True
    for t in tuple_list:
        if t[0] == 'do()':
            enabled = True
            continue
        elif t[0] == "don't()":
            enabled = False
            continue
        else:
            if enabled:
                total += int(t[0]) * int(t[1])
    return total

def pt1():
    input = read_data()
    tups = parse_input(input, 1)
    total = calculate_from_tuple_list(tups)
    print(total)

def pt2():
    input = read_data()
    tups = parse_input(input, 2)
    total = calculate_from_tuple_list(tups)
    print(total)

def main():
    # pt1()
    pt2()


if __name__ == "__main__":
    main()