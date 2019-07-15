# _*_  coding:utf-8 _*_
# a每天进步%，B（进步五天，休息日退步1%）需要每天进步多少超过a
dayUp = 1

a = pow((1+0.01), 365)
print(a)

def BUp(df):
    b = dayUp
    for i in range(365):
        if i % 7 in [6, 0]:
            b = b * (1 - 0.01)
        else:
            b = b * (1 + df)
    return b

bFactory = 0.01

while BUp(bFactory) < a:
    bFactory += 0.001
print("{:.3f}".format(bFactory))
