# -*- coding:utf-8 -*-

# 100以内所有素数和

res = 2
for i in range(3, 100):
    for j in range(2, i):
        if i % j == 0 :
            break;
    else:
        res += i
print(res)


'''
for i in range(1000, 10000):
    a = str(i)
    b = pow(eval(a[0]), 4) + pow(eval(a[1]), 4) + pow(eval(a[2]), 4) + pow(eval(a[3]), 4)
    if b == i:
        print(i)
'''


'''

k = 10000
a = 0
while k > 1:
    print(k)
    k = k / 2
    a += 1
print("a:{:}".format(a))
'''