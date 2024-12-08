import math
import itertools

def is_in_range(value:int, numbers:list[int]) -> bool:
    min_value = sum(numbers)
    max_value = math.prod(numbers)
    return min_value <= value <= max_value

def get_permutation(length: int) -> list:
    operands = ['+', '*']
    # permutations = list(itertools.product(operands, repeat=length))
    permutations = list(itertools.permutations(operands*length, length))
    return permutations

def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

def test_line(line):
    result, operation = line.split(':')
    result = int(result)
    nums = [int(num) for num in operation.split()]
    test_range = is_in_range(result, nums)
    if test_range:
        permutations = get_permutation(len(nums)-1)
        permutations = set(permutations)
        for permutation in permutations:
            num1 = nums[0]
            for num2, operand in zip(nums[1:], permutation):
                to_eval = [num1, operand, num2]
                to_eval = ''.join(str(item) for item in to_eval)
                num1 = eval(to_eval)
            if num1 == result:
                del result, operation, nums, test_range, permutations
                return num1
    del result, operation, nums, test_range
    return 0

def main():
    total = 0
    for i, line in enumerate(read_file('src/day07-BridgeRepair/day07.txt')):
        print(i)
        if i < 100:
            result = test_line(line)
            total += result
    print(total)

    print(72095400778)
    tl = [1, 7, 4, 1, 5, 6, 6, 79, 3, 5, 2, 780]
    print(test_line('72095400778: 1 7 4 1 5 6 6 79 3 5 2 780'))

main()