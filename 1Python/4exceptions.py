

# IndexError 
try:
    L = [0, 1, 2]
    print(L[4])
except IndexError as error:
    print(error)
    
# NameError
try:
    fibonacci(10)
except NameError as error:
    print(error)
    
# ZeroDivisionError
try:
    a, b = 5, 0
    print(a / b)
except ZeroDivisionError as error:
    print(error)