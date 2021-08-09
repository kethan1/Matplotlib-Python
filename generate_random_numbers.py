import random

with open(input('file: '), 'w') as output_file:
    for _ in range(100):
        print(random.randint(1, 100), file=output_file)
