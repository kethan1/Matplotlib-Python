import matplotlib.pyplot as plt

with open(input('file 1: ')) as f1:
    x = [int(line) for line in f1]

with open(input('file 2: ')) as f2:
    y = [int(line) for line in f2]

print(x, y)

plt.plot(x, y, 'co')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Random Numbers')
plt.show()
