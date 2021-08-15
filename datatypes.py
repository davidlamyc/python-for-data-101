"""
Simple python stuff, but including for light revision
"""

## datatypes
my_int = 1
print(type(my_int)) # int

my_float = 1.0
print(type(my_float)) # float

print(1/4) # python3 has true division

my_string = 'this is a single'
print(type(my_string)) # string

# print formatting
age = 28
name = 'John'
print('My age is {} and my name is {}.'.format(age, name))
print('My age is {my_age} and my name is {my_name}.'.format(my_age=age, my_name=name))

# indexing strings
s = 'hello'
print(s[0]) # h
print(s[4]) # o
print(s[1:3]) # el
print(s[:3]) # hel
print(s[3:]) # lo

# lists
my_list = [1,2,3]
my_list.append(4)
print(my_list) # [1,2,3,4]
print(my_list[2]) # 3

# dictionaries
d = {
    'key1': 'my value',
    'key2': 123,
    'list_in_dict': [1,2,3,4],
    'dict_in_dict': {
        'innerkey': 'innervalue'
    }
}
print(d['key1']) # 'my_value'
print(d['list_in_dict'][2]) # 3
print(d['dict_in_dict']['innerkey']) # 'innervalue'

# booleans
print(type(True))
print(type(False))

# tuple
t = (1,2,3)
print(t[1]) # 2
# t[1] = 6 # TypeError: 'tuple' object does not support item assignment, cannot mutate tuples

# sets
s = {1,2,3,3,3,4,4,4,4,4}
print(s) # {1,2,3,4}