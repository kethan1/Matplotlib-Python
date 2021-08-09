import matplotlib.pyplot as plt
import random
import numpy as np

plt.hist([random.randint(1, 100) for _ in range(30)], list(np.arange(10, 301, 10)), histtype="bar", color="orange", rwidth=0.8, label="Product Ratings")
plt.show()
