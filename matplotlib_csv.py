import matplotlib.pyplot as plt
import csv

x = []
y = []
with open('US_chronic_diseases.csv') as input_file:
    print(input_file.readline().split(','))
    plots = csv.reader(input_file, delimiter=',')
    rows = 0
    idaho_alcohol = 0
    male_arthritis = 0
    for row in plots:
        rows += 1
        # print(row)
        if row[5].lower() == 'alcohol' and row[3].lower() == 'idaho':
            idaho_alcohol += 1
        elif 'Gender' in row and row[row.index('Gender') + 1] == 'Male' and row[5] == 'Arthritis':
            male_arthritis += 1

plt.pie(
    [rows - (idaho_alcohol + male_arthritis), idaho_alcohol, male_arthritis],
    labels=['other', 'Alcoholic Idahos', 'Males with Arthritis'], startangle=90,
    explode=(0, 0.2, 0.2), autopct='%1.1f%%'
)
plt.tight_layout()
plt.show()
