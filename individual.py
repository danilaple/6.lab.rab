#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))
   
    if len(A) != 22:
        print("Неверное количество дисков", file=sys.stderr)
        exit(1)
    if len(B) != 22:
        print("Неверное количество цен", file=sys.stderr)
        exit(1)

    s = input(int())
    a = 0
    for item in B:
        if item > s:
            a += 1

    print("Kоличество подходящих: ", a)