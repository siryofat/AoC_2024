import math
import itertools

def is_in_range(value:int, numbers:list[int]) -> bool:
    min_value = sum(numbers)
    max_value = math.prod(numbers)
    return min_value <= value <= max_value

def get_permutation(length: int):
    operands = ['+', '*', 'c']
    return itertools.product(operands, repeat=length+1)

def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

def test_line(line):
    try:
        result, operation = line.split(':')
        result = int(result)
        nums = [int(num) for num in operation.split()]

        for permutation in get_permutation(len(nums)-1):
            num1 = nums[0]
            for num2, operand in zip(nums[1:], permutation):
                if operand == 'c':
                    # TODO find a better logic, I'm rushing now. revisit later.
                    num1 = str(num1)
                    num2 = str(num2)
                    num1 = num1 + num2
                    num1 = int(num1)
                else:
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
print(test_line('994003: 22 954 1 155 5 47'))
print(3310275554652+994003)

main()