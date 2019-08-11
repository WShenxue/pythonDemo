# -*- coding:utf-8 -*-

# 请在...补充一行或多行代码

def prime(m):
    for i in range(2, m):
        if (m % i) == 0:
            return False
    return True


def main(m):
    round = 0
    while round < 5:
        if prime(m):
            if round == 4:
                print(m, end="")
            else:
                print(m, end=",")
            round += 1
        else:
            prime(m)
        m += 1


n = eval(input())
m = int(n)
m = (m + 1) if m < n else m
main(m)
'''
def func(a,b):
    c = a ** 2 + b
    b = a
    return c
a = 10
b = 100
c = func(a, b) + a
'''
