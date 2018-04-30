from ctypes import *
msvcrt = cdll.msvcrt

msvcrt.printf(bytes('Testing: %s','utf-8'), bytes("Hello World!\n",'utf-8'))
