def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

def log(sequence, message, *values):
    if not values:
        print('%s: %s'%(sequence,message))
    else:
        values_str=','.join(str(x) for x in values)
        print('%s: %s: %s' %(sequence,message,values_str))

def my_geneartor():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it=my_geneartor()
my_func(*it) #Using the * operator with a geneartor may cause your program to run out of memory and crash

#
# log('My numbers are', 1, 2)
# log('Hi there')
#
# log(1,'Favorites',7,33)
log(1,'Favorite numbers',7,33) # New usage is OK
log('Favorite numbers',7,33) # Old usage breaks