def is_list_in_order(list_to_check: list, dict_of_rules: dict) -> bool:
    for i, item in enumerate(list_to_check):
        for test_item in list_to_check[i:]:
            if test_item in dict_of_rules.get(item, []):
                return False
    return True

import sys
print(sys.getrecursionlimit())

def fix_line(line_to_fix: list, dict_of_rules: dict) -> list:
    for i, item in enumerate(line_to_fix):
        for j, test_item in enumerate(line_to_fix[i:]):
            if test_item in dict_of_rules.get(item, []):
                line_to_fix[i], line_to_fix[j+i] = line_to_fix[j+i], line_to_fix[i]
                return fix_line(line_to_fix, dict_of_rules)
    return line_to_fix


def get_mid_item(line_as_list: list) -> int:
    mid_position = len(line_as_list) / 2
    item_to_add = line_as_list[int(mid_position)]
    return item_to_add


def main():
    ordering_rules = {}
    firts_chunk = True
    check_list = []
    total_score = 0
    fixed_score = 0

    # read txt file:
    with open('src/Day05-PrintQueue/day05_input.txt', 'r') as file:
        for line in file:
            stripped = line.strip()
            if stripped:
                # populates the ordering rules
                if firts_chunk:
                    before, after = stripped.split('|')
                    ordering_rules.setdefault(after, set()).add(before)
                # tests each line
                else:
                    current_line_as_list = stripped.split(',')
                    check_order = is_list_in_order(current_line_as_list,
                                                    ordering_rules)
                    check_list.append(check_order)
                    if check_order: #solves part one of the puzzle
                        item_to_add = get_mid_item(current_line_as_list)
                        total_score += int(item_to_add)
                    else: #solves part two of the puzzle.
                        fixed_line = fix_line(current_line_as_list, ordering_rules)
                        item_to_add = get_mid_item(fixed_line)
                        fixed_score += int(item_to_add)


            # do this to iterate only once in the txt file.
            # once rules are populated the second chunk can be evaluated inmedietly.
            else:
                firts_chunk = False

    print(f'Total score of ordered lines: {total_score}')
    print(f'score of fixed lines: {fixed_score}')


main()