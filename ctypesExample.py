from ctypes import *

# only in windows
msvcrt = cdll.msvcrt
msvcrt.printf(bytes('Testing: %s','utf-8'), bytes("Hello World!\n",'utf-8'))


seitz = c_char_p(bytes('loves python','utf-8'))

print(seitz)
print('Pointer of Seitz: ' + str(byref(seitz)))
# dereferencing pointer

print(seitz.value)
# only in linux
# libc = CDLL('libc.so.6')
# libc.printf(bytes('Testing: %s','utf-8'), bytes("Hello World!\n",'utf-8'))
class beer_recipe(Structure):
    _fields_ = [
    ("amt_barley", c_int),
    ("amt_water", c_int),
    ]
