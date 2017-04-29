#Item 14: Prefer Exceptions to Returning None
import sys

print(sys.version_info)
print(sys.version)
x,y=5,0
print
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


try:
    result=divide(x,y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is%.1f' % result)
