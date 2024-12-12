#test_string, blinks = '125 17', 6 #22
#test_string, blinks = '3 386358 86195 85 1267 3752457 0 741', 25 #183248
test_string, blinks = '3 386358 86195 85 1267 3752457 0 741', 75 #183248
#wrongs = [78]

def clean(item:str) -> str:
    item = item.lstrip('0')
    return item if item else '0'

def arranger(input_list:list) -> list:
    new_list = []
    for stone in input_list:
        if stone == '0':
            new_list.append('1')
            continue

        if len(stone)%2 == 0:
            half = int(len(stone) / 2)
            first_half = stone[:half]
            second_half = stone[half:]
            new_list.append(clean(first_half))
            new_list.append(clean(second_half))
            continue

        last = int(stone)*2024
        new_list.append(str(last))

    return new_list

test_list = [item for item in test_string.split()]

# for i in range(blinks):
#     print(f'iteration {i}, list before function {test_list=}')
#     test_list = arranger(test_list)
#     print(f'list after function {test_list=}\n')

# print(len(test_list))

total = 0
for stone in test_list:
    run = [stone]
    print(f'running for {stone}:')
    for i in range(blinks):
        run = arranger(run)
    print(f'this run {len(run)}')
    total += len(run)

print(total)