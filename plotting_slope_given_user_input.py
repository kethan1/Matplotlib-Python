import matplotlib.pyplot as plt


def get_y(m: int, b: int, x: int) -> int:
    return m * x + b


x_values = [int(input('Please enter a x coordinate: ')) for _ in range(4)]
y_values = [get_y(5, 3, x) for x in x_values]

plt.plot(x_values, y_values, 'co')
plt.xlabel('x')
plt.ylabel('y')

plt.title('X vs Y')
plt.show()
