import matplotlib.pyplot as plt
import csv

x = []
y = []
with open("US_chronic_diseases.csv") as input_file:
    print(input_file.readline().split(','))
    plots = csv.reader(input_file, delimiter=",")
    for row in plots:
        print(row)
        if row[5].lower() == 'alcohol' and (int(row[14]) - int(row[15])) >= 3:
            print('alcohol')
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label="Loaded from file")
plt.xlabel("x")
plt.ylabel("y")
plt.title("MyProject")
plt.show()
