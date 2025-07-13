def is_even(num):
    return num%2 == 0

def is_odd(num):
    return not is_even(num)
     

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a, b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError
    return a/b