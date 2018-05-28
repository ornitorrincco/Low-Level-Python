from ctypes import *

class some_stuff(Union):
    _fields_ = [
    ("stuff_long", c_long),
    ("stuff_int", c_int),
    ("stuff_char", c_char * 8),
    ]

value =  input('Enter the amount of some stuff to put:')
myStuff = some_stuff(int(value))
print('stuff as long: %ld' % myStuff.stuff_long)
print('stuff as int: %d' % myStuff.stuff_int)
print('stuff as char: %s' % myStuff.stuff_char)
