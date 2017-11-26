def addition(a, b):
    return a+b

def subtraction(a, b):
    return b-a

def multiplication(a, b):
    return a*b

def division(a, b):
    return a/b


def addition_all(*args):
    return (sum(args))

def multiplication_all(*args):
    mult = 1
    for i in args:
        mult *= i
    return mult



