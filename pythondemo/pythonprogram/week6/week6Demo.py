# -*- coding:utf-8 -*-

A = {"123", "p", "y"}
for item in A:
    print(item, end = "")
try:
    while True:
        print(A.pop(), end = "")
except:
    pass
