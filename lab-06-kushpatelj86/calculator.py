def add(a,b):
    sum = a + b
    return sum

def subtract(a,b):
    diff = a - b
    return diff


def multiply(a,b):
    mul = a * b
    return mul

def divide(a,b):
    div = a / b

    if b == 0:
        raise ZeroDivisionError("You can't divide by 0")
    return div

