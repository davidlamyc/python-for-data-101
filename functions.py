"""
Simple python stuff, but including for light revision
"""

def my_func(param1 = 'Nameless'):
    print('Hello {}'.format(param1))

my_func('John')
my_func(param1 = 'John')
my_func()

def square(n):
    return n ** 2

print(square(5))

### inbuilt functions

def multiply_by_2(n):
    return n * 2

my_list = [1,2,3,4,5]

print(list(map(multiply_by_2, my_list)))

def multiply_by_2(n):
    return n * 2

print(list(filter(lambda num : num % 2 == 0, my_list)))