"""
Simple python stuff, but including for light revision
"""

## control flow

i = 10
if i < 10:
    print('less than 10')
elif i == 10:
    print('equals 10')
else:
    print('more than 10')

seq = [1,2,3,4,5]
for item in seq:
    print(item)

j = 1

while j < 5:
    print('j is: {}'.format(j))
    j = j + 1

original = [1,2,3,4,5]
double = []
for i in original:
    double.append(i * 2)
print(double)
double_comprehended = [num * 2 for num in original]
print(double_comprehended)