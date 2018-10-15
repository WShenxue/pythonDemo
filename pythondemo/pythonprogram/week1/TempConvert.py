# -*- coding: utf-8 -*-
#TempConvert.py

# Tempstr = input(":")
# if Tempstr[-1] in ['F', 'f']:
#     c = (eval(Tempstr[0: -1]) - 32) / 1.8
#     print("{:.2f}C".format(c))
# elif Tempstr[-1] in ['C', 'c']:
#     f = 1.8 * eval(Tempstr[0: -1]) + 32
#     print("{:.2f}F".format(f))
# else:
#     print("输入格式错误")

# TempStr = input("")
# if TempStr[0] in ['F', 'f']:
#     c = (eval(TempStr[1: len(TempStr)]) - 25) / 1.8
#     print("C{:.2f}".format(c))
# elif TempStr[0] in ['C', 'c']:
#     f = 1.8 * eval(TempStr[1: len(TempStr)]) + 25
#     print("F{:.2f}".format(f))


TempStr = input("")
if TempStr[0: 3] in ['RMB']:
    c = eval(TempStr[3: len(TempStr)]) / 6.78
    print("USD{:.2f}".format(c))
elif TempStr[0: 3] in ['USD']:
    f = 6.78 * eval(TempStr[3: len(TempStr)])
    print("RMB{:.2f}".format(f))
