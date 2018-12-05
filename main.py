import random
import math


def calculate_pi(attempts):
    assert isinstance(attempts, int)
    assert attempts>0
    falling_inside = 0

    for _ in range(attempts):
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 1.0)
        if math.sqrt(x**2 + y**2) <= 1:
            falling_inside += 1
    pi = 4 * falling_inside/attempts
    return pi

iterations = 100000
result = calculate_pi(iterations)
print('Approximated value for Pi: {}'.format(result))
print('Iterations used: {}'.format(iterations))






