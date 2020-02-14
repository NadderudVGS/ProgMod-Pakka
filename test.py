from metoder import *

def funk(x):
    return -x**2 + 4*x

A = num_int_trap(funk, 0, 4, 100)

print(A)