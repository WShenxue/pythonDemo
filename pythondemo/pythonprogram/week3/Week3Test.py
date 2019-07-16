# -*- coding:utf-8 -*-

# 字符串分段组合
str = input()
# str.join('+')
strs = str.split('-')
print(strs[0] + '+' + strs[-1])

'''
# 平方根按照特定格式输出
num = eval(input())
res = pow(num, 0.5)
print("{:+>30.3f}".format(res))
'''