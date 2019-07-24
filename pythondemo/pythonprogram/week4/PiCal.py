# -*- coding=utf-8 -*-
from random import random, seed
#from time import perf_counter

n = eval(input())
seed(123)
res = 0.0
for i in range(n):
    x, y = random(), random()
    d = pow(x ** 2 + y ** 2, 0.5)
    if d <= 1:
        res += 1
out = 4 * (res / n)
print("{:.6f}".format(out))