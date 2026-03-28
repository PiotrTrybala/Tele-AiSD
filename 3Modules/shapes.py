
import numpy as np

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return np.pi * np.square(self.r)

    def __str__(self):
        return f'(area = {self.area()})'

class Triangle:

    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        return self.a * self.h / 2

    def __str__(self):
        return f'(area = {self.area()})'

class Square:

    def __init__(self, a):
        self.a = a

    def area(self):
        return np.square(self.a)

    def __str__(self):
        return f'(area = {self.area()})'