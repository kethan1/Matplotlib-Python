import matplotlib.pyplot as plt
import random

plt.bar(0, 5, label="Pass just one number")
plt.bar(['Joey', 'Jim', 'Isabella', 'Jack', 'Margarette'], [random.randint(50, 100) for _ in range(5)], label="Pass a list")
plt.show()
