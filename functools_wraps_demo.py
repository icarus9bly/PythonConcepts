# https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
# If using a decorator always meant losing this information about a function, it would be a serious problem. That's why we have functools.wraps.
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        print("Start logger")
        output = func(*args, **kwargs)
        print(output)
        print("End logger")
    return wrapper_func

def square(x):
    "Squares number"
    return x*x

result = square(45)
print(result)
# 2025

@logger
def square(x):
    "Squares number"
    return x*x

print(square.__name__)
print(square.__doc__)
print(square)
# Start logger
# 7921
# End logger