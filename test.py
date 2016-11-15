__author__ = 'hguthrie'
#  -*- coding: utf-8 -*-

# I am learning to write in Python by playing with the Fibonacci sequence. Fibonacci originally carried out the
# computation beginning with 1,1,2

fibInit, fibSec = 1, 1

while fibSec < 100:
    print(fibSec)
    fibInit, fibSec = fibSec, fibInit + fibSec
