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

first_index = 1

second_index = 2

for line in hardwood:
    x.append(line[first_index])
    y.append(line[second_index])

x1 = []

y1 = []


for line2 in carpet:
    x1.append(line2[first_index])
    y1.append(line2[second_index])

for i in range(len(x)):
    sentence = x[i] + " " + x1[i]
    print(sentence)


plt.scatter(x, y, label='hardwood', color='blue')

plt.scatter(x1, y1, label='carpet', color='red')

plt.xlabel('features')

plt.ylabel('observations')

plt.title('Hardwood and Carpet')

plt.legend()

plt.show()