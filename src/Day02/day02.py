import csv
from itertools import pairwise
from typing import Type

def read_csv_file(csv_file_name: str) -> Type[csv.reader]:
    with open(csv_file_name, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        return csv_reader


def check_for_safety(list_to_check: list[int]) -> bool:
    first_item, second_item = list_to_check[0], list_to_check[1]
    sorting_order = 'ascending' if second_item > first_item else 'descending'
    for item_0, item_1 in pairwise(list_to_check):
        current_sorting = 'ascending' if item_1 > item_0 else 'descending'
        adjacent_step = abs(item_0 - item_1)
        sorting_condition_fail = current_sorting != sorting_order
        step_condition_fail = adjacent_step > 3 or adjacent_step == 0
        if any([sorting_condition_fail, step_condition_fail]):
            return False
    return True

def get_cleared_lists(list_to_clear: list[int]) -> list[list]:
    cleared_lists = []
    for i in range(len(list_to_clear)):
        subset = list_to_clear[:i] + list_to_clear[i+1:]
        cleared_lists.append(subset)
    return cleared_lists

def get_safety_checks_with_tolerance(list_to_check: list[str]) -> bool:
    cleared_lists = get_cleared_lists(list_to_check)
    safety_checks = []
    for list_to_check_with_tolerance in cleared_lists:
        check_status = check_for_safety(list_to_check_with_tolerance)
        safety_checks.append(check_status)
    return any(safety_checks)

def get_safety_checks(csv_file_name: str, use_dampener: bool = True) -> list[bool]:
    safety_checks = []
    with open(csv_file_name, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=' ')
        for list_to_check in csv_reader:
            list_to_check = list(map(int,list_to_check))
            check_status = check_for_safety(list_to_check)
            if use_dampener:
                if check_status:
                    safety_checks.append(check_status)
                else:
                    check_status = get_safety_checks_with_tolerance(list_to_check)
                    safety_checks.append(check_status)
            else:
                safety_checks.append(check_status)
    return safety_checks



def main():
    csv_file = 'src/Day02/day02_input.csv'
    safety_checks = get_safety_checks(csv_file, use_dampener=False)
    safety_checks_with_dampener = get_safety_checks(csv_file)
    print(f'Safety checks without dampener: {sum(safety_checks)}') #252
    print(f'Safety checks with dampener: {sum(safety_checks_with_dampener)}') #324


main()
