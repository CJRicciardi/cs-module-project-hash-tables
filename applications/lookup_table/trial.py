import random
import math

cache = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

    if f'{x}, {y}' not in cache:
        cache[f'{x}, {y}'] = slowfun_too_slow(x, y)
        return cache[f'{x}, {y}']

    else:
        return cache[f'{x}, {y}']

# for i in range(2, 14):
#     for j in range(3, 6):
#         print(f'slowfun: {i}, {j} = {slowfun(i, j)}')

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')