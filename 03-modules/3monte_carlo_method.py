import numpy as np

def is_inside_circle(x, y, r):
    return np.sqrt(np.square(x) + np.square(y)) <= r


def circle_monte_carlo(r, n = 10):
    c = 0
    for _ in range(n):

        x = np.random.uniform(-r, r)
        y = np.random.uniform(-r, r)

        if is_inside_circle(x, y, r):
            c += 1

    in_circle = c / n
    area = (2 * r)**2 * in_circle
    expected = np.pi * r**2

    print(f'n = {n}, area = {area:.3f}, expected = {expected:.3f}, error = {abs(area - expected):.3f}', flush=True)

    return area

def integral_monte_carlo(a, b, n = 10):

    c = 0
    for _ in range(n):

        x = np.random.uniform(a, b)
        y = np.random.uniform(-1, 1)

        value = np.sin(x)

        if value >= 0:
            if 0 <= y <= value:
                c += 1
        else:
            if value <= y <= 0:
                c -= 1

    area = (b - a) * 2 * (c / n)
    expected = 1 - np.cos(2)

    print(f'n = {n}, area = {area:.3f}, expected = {expected:.3f}, error = {abs(area - expected):.3f}', flush=True)

    return area

# calculating circle area using Monte Carlo Method

circle_monte_carlo(3, 10)
circle_monte_carlo(3, 100)
circle_monte_carlo(3, 1000)
circle_monte_carlo(3, 10000)

print(f'Circle -> final result = {circle_monte_carlo(3, 10000)}')

# calculating integral of sin(x) in range [0, 2] using Monte Carlo Method

integral_monte_carlo(0, 2, 10)
integral_monte_carlo(0, 2, 100)
integral_monte_carlo(0, 2, 100)
integral_monte_carlo(0, 2, 1000)

print(f'Integral -> final result = {integral_monte_carlo(0, 2, 10000)}')

