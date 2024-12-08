import math
import itertools

def is_in_range(value:int, numbers:list[int]) -> bool:
    min_value = sum(numbers)
    max_value = math.prod(numbers)
    return min_value <= value <= max_value

def get_permutation(length: int):
    operands = ['+', '*']
    return itertools.product(operands, repeat=length)

def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def test_line(line):
    try:
        result, operation = line.split(':')
        result = int(result)
        nums = [int(num) for num in operation.split()]
        if not is_in_range(result, nums):
            return 0

        for permutation in get_permutation(len(nums)-1):
            num1 = nums[0]
            for num2, operand in zip(nums[1:], permutation):
                num1 = eval(f"{num1}{operand}{num2}")
            if num1 == result:
                return result
        return 0
    except Exception as e:
        print(f"Error processing line: {line}")
        print(f"Error details: {e}")
        return 0

def main():
    total = 0
    for i, line in enumerate(read_file('src/day07-BridgeRepair/day07.txt')):
        print(f"Processing line {i}: {line}")
        result = test_line(line)
        total += result
        print(f"Result: {result}, Running Total: {total}")

    print(f"Final Total: {total}")

    # Test the problematic line separately
    print(test_line('72095400778: 1 7 4 1 5 6 6 79 3 5 2 780'))

main()