# -*- coding: utf-8 -*-

def check(n):
    s = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            s += i
    return s


def getResult(n):
    for i in range(1, int(n / 2) + 1):
        res = check(i)
        if i != res and check(res) == i:
            print('{}-{}'.format(i, res))


if __name__ == '__main__':
    n = int(input())
    getResult(n)
