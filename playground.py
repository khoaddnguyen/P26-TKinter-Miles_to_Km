# Many positional arguments syntax *args
# *args is a tuple
def add(*args):

    print(args[1]) # fetch 5
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(3, 5, 6, 8, 13, 17))

# Many keyword arguments syntax *kwargs
# **kwargs is a dictionary
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    a = n + kwargs["add"]
    b = n * kwargs["multiply"]
    print(n, a, b)

    # loop through all items in kwargs and fetch result that we want to use using a keyword
    #print(kwargs["add"])

calculate(2, add=3, multiply=5)