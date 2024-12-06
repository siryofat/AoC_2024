def is_list_in_order(list_to_check: list, dict_of_rules: dict) -> bool:
    for i, item in enumerate(list_to_check):
        for test_item in list_to_check[i:]:
            if test_item in dict_of_rules.get(item, []):
                return False
    return True

def part_one():
    ordering_rules = {}
    firts_chunk = True
    check_list = []
    total_score = 0

    # read txt file:
    with open('src/Day05-PrintQueue/day05_input.txt', 'r') as file:
        for line in file:
            stripped = line.strip()
            if stripped:
                if firts_chunk:
                    before, after = stripped.split('|')
                    ordering_rules.setdefault(after, set()).add(before)
                else:
                    current_line_as_list = stripped.split(',')
                    check_order = is_list_in_order(current_line_as_list,
                                                    ordering_rules)
                    check_list.append(check_order)
                    if check_order:
                        mid_position = len(current_line_as_list) / 2
                        item_to_add = current_line_as_list[int(mid_position)]
                        total_score += int(item_to_add)
            else:
                firts_chunk = False


    print(sum(check_list))
    print(total_score)

part_one()