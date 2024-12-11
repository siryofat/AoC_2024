import string
data = []

with open('src/day08/day08_test.txt', 'r') as file:
    for line in file:
        data.append(line.strip())

data_size = (len(data), len(data[0]))

def test_item(row:int, col:int, size:tuple, char:str, data:list[list], reso:set):
    #check horizontal:
    mrow, mcol = size #max rows and cols
    test_wide = min(col, mcol-col)
    test_height = min(row, mrow-row)
    for j in range(col - test_wide, col+test_wide):
        if data[row+1][j] == char:
            if row+2 <= mrow and 0 <= 2*j-col <= mcol:
                reso.add((row+2, 2*j-col))
                test.append((row+2, 2*j-col))
            if 0 <= row-1 and 0 <= 2*col-j <= mcol:
                reso.add((row-1, 2*col-j))
                test.append((row-1, 2*col-j))
    for i in range(row - test_height, row+test_height):
        if data[i][col+1] == char:
            if col+2 <= mcol and 0 <= 2*i-row <= mrow:
                reso.add((2*i-row, col+2))
                test.append((col+2, 2*i-row))
            if 0 <= col-1 and 0 <= 2*row-i <= mrow:
                reso.add((2*row-i, col-1))
                test.append((col-1, 2*row-i))
                if (col-1, 2*row-i) == (3,6):
                    print('here')

characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
antennas = set()
test = []

for r, row in enumerate(data):
    for c, col in enumerate(row):
        if col in characters:
            test_item(r, c, data_size, col, data, antennas)

print(len(antennas))
print(len(test))

print(antennas)