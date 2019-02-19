from mpl_toolkits.mplot3d import axes3d
import csv
import matplotlib.pyplot as plt
hardwood = []
carpet = []
figure = plt.figure()
ax1 = figure.add_subplot(111, projection='3d')
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

z = []

first_index = 61

second_index = 62

third_index = 63
for line in hardwood:
    x.append(float(line[first_index]))
    y.append(float(line[second_index]))
    z.append(float(line[third_index]))

x1 = []

y1 = []

z1 = []
for line2 in carpet:
    x1.append(float(line2[first_index]))
    y1.append(float(line2[second_index]))
    z1.append(float(line2[third_index]))

ax1.scatter(x,y,z,c='b')

ax1.scatter(x1,y1,z1,c='r')

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
print("Waiting...")
plt.show()
print("Finishing...")
#making the means for hardwood
hardwoodSum64 = []

print(len(hardwoodSum64))

for i in range(len(hardwood)):
    line = hardwood[i]
    hardwoodSum64.append([])
    for j in range(len(line)):
        hardwoodSum64[i].append(hardwood[i][j])

hardwoodMeans64 = []

for i in range(len(hardwood[0])):
    hardwoodMeans64.append([])

print(len(hardwoodSum64))

for i in range(len(hardwoodMeans64)):
    sum = 0
    for j in range(len(hardwoodSum64)):
        sum += float(hardwoodSum64[j][i])
    hardwoodMeans64[i]=sum/len(hardwoodSum64)


#means for carpet

carpetSum64 = []

for i in range(len(carpet)):
    line = carpet[i]
    carpetSum64.append([])
    for j in range(len(line)):
        carpetSum64[i].append(carpet[i][j])

carpetMean64 = []

for i in range(len(carpet[0])):
    carpetMean64.append([])

for i in range(len(hardwoodMeans64)):
    sum = 0
    for j in range(len(carpetSum64)):
        sum += float(carpetSum64[j][i])
    carpetMean64[i] = sum / len(carpetSum64)
print(carpetMean64)
##############################histogram

plt.hist(hardwoodMeans64)
plt.hist(carpetMean64)
print(len(hardwoodMeans64))
print(len(carpetMean64))
plt.xlabel("features")
plt.ylabel("means")
plt.legend(['hardwood', 'carpet'])
plt.title('Hardwood vs Carpet Means')
plt.show()
###########################line graph
featuresGrid = []
for i in range(0,64):
    featuresGrid.append(i)

plt.plot(featuresGrid, carpetMean64,color='r',label='Carpet means')
plt.plot(featuresGrid, hardwoodMeans64, color='b', label='Hardwood means')
plt.xlabel('features')
plt.ylabel('Means')
plt.legend()
plt.show()

