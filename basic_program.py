import matplotlib.pyplot as plt

# scatter plot
x = ['carrot', 'beetroot', 'pumpkin', 'broccoli']
y = [10, 12, 5, 7]

plt.plot(x, y, 'r^')
plt.xlabel('x')
plt.ylabel('y')
# Limit x 0 - 6 and limit y 0 - 20
# plt.axis([0, 6, 0, 20])
plt.title('X vs Y')
plt.show()
