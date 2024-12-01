import csv

# Initialize empty lists to store the data
locations_1 = []
locations_2 = []

# Read the data from the CSV file
with open('src/Day01/day01_input.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        parts = row[0].split('   ')
        # Assuming the CSV has two columns
        locations_1.append(int(parts[0]))
        locations_2.append(int(parts[1]))

locations_1.sort()
locations_2.sort()

total_distance = 0
for location_1, location_2 in zip(locations_1, locations_2):
    total_distance += abs(location_2 - location_1)

print(f'Total distance: {total_distance}') #936063

# Part Two:

repetitions = {}

for location_1 in locations_1:
    if location_1 in repetitions:
        continue
    repetitions[location_1] = 0
    for location_2 in locations_2:
        if location_1 == location_2:
            repetitions[location_1] += 1

similarity_score = 0

for location in locations_1:
    score = repetitions[location]
    score_value = location * score
    similarity_score += score_value

print(f'Similarity Score: {similarity_score}') #23150395