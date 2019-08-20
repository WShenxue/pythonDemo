# coding: utf-8

# 英文字符的鲁棒输入
allChars = []
for i in range(26):
    allChars += chr(ord('a') + i)
    allChars += chr(ord('A') + i)
inChars = input()
for i in inChars:
    if i in allChars:
        print("{}".format(i), end="")

# 数字的鲁棒输入
inNum = input()
try:
    if complex(inNum) == eval(inNum):
        print(pow(eval(inNum), 2))
except:
    print("输入有误")