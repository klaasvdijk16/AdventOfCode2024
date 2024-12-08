import re

def read_data():
    with open('day3/input.txt', 'r') as f:
        return f.read()

def parse_input(input_string):
    res = re.findall("mul\((\d+),(\d+)\)", input_string)
    return res

def calculate_from_tuple_list(tuple_list):
    total = 0
    for t in tuple_list:
        total += int(t[0]) * int(t[1])
    return total

def pt1():
    input = read_data()
    tups = parse_input(input)
    total = calculate_from_tuple_list(tups)
    print(total)

def main():
    pt1()


if __name__ == "__main__":
    main()