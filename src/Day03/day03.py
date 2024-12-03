import re

#TODO: Make this more readable!

with open('src/Day03/day03_input.txt', 'r') as file:
    content = file.read()

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
matches = re.findall(pattern, content)

total_add = 0
for match in matches:
    num1, num2 = match
    current_mul = int(num1) * int(num2)
    total_add += current_mul

print(total_add)



pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
results = []
matches = re.findall(pattern, content)
multiplier = 1
total_add = 0
for match in matches:
    if match == "do()":
        multiplier = 1
    elif match == "don't()":
        multiplier = 0
    else:
        num1, num2 = match[4:-1].split(',')
        current_mul = int(num1) * int(num2) * multiplier
        total_add += current_mul

print(total_add)