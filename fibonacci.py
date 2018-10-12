# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:22:09 2018

@author: 石坂 梨緒
"""
def fib(n):
    a=0
    b=1
    if n==0:
        print(a)
    elif n==1:
        print(b)
    else:
        for i in range(n):
            a=b
            b=a+b
            print(b)
fib(2018)
        