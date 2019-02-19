import csv
import matplotlib.pyplot as plt
hardwood =[]
carpet = []
with open('hardwood.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            hardwood.append(line)

with open('carpet.csv', 'r') as csv_file2:
        csv_reader2 = csv.reader(csv_file2)
        for line in csv_reader2:
            carpet.append(line)

x = []

y = []

first_index = 0

second_index = 1

third_index = 2

fourth_index = 3

for line in hardwood:
    x.append(line[first_index])
    x.append(line[second_index])
    y.append(line[third_index])
    y.append(line[fourth_index])

x1 = []

y1 = []


for line2 in carpet:
    x1.append(line2[first_index])
    x1.append(line2[second_index])
    y1.append(line2[third_index])
    y1.append(line2[fourth_index])

plt.scatter(x, y, label='hardwood', color='blue')

plt.scatter(x1, y1, label='carpet', color='red')

plt.xlabel('features')

plt.ylabel('observations')

plt.title('Hardwood and Carpet')

print("Waiting...")

plt.legend()

plt.show()

print("Finished......")