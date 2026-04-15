
import numpy as np

class Shape:
    def area(self):
        pass

    def circumference(self):
        pass

    def __str__(self):
        return f'(area = {self.area()}, circumfrence = {self.circumference()})'

class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return np.pi * np.square(self.r)
    
    def circumference(self):
        return 2 * np.pi * self.r

class Triangle(Shape):

    def __init__(self, a, b, c):
        super().__init__()

        if not self.check_valid(a, b, c):
            print(f'This triangle could not exist')
            exit(1)

        self.a = a
        self.b = b
        self.c = c

    def check_valid(self, a, b, c):
        s1 = a + b
        s2 = a + c
        s3 = b + c

        print(f'{s1 > c}, {c}, {s2 > b}, {b}, {s3 > a}, {a}')

        return s1 > c or s2 > b or s3 > a 
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return np.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def circumference(self):
        return self.a + self.b + self.c

class Square(Shape):

    def __init__(self, a):
        super().__init__()
        self.a = a

    def area(self):
        return np.square(self.a)
    
    def circumference(self):
        return 4 * self.a
