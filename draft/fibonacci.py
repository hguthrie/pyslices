__author__ = 'hguthrie'
#  -*- coding: utf-8 -*-

# Fibonacci sequence
fib1, fib2 = 1,1
print ("Fibonacci sequence: "), fib1
while fib2 < 100:
    print(fib2)
    fib1, fib2 = fib2, fib1 + fib2