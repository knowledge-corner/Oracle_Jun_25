# decorator
def is_int(func_obj) :
    def check(param):
        if type(param) == int :
            return func_obj(param)
        else:
            return "Invalid"
    return check

@is_int
def factorial(num) :
    fact = 1
    for i in range(num, 1, -1):
        fact *= i
    return fact

@is_int
def even_odd(num) :
    return "even" if num % 2 == 0 else "odd"

@is_int
def sqaure(num) :
    return num ** 2