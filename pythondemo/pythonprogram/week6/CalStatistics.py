# -*- coding:utf-8 -*-

def getNum():
    nums = []
    isNumStr = input("请输入数字（回车退出）")
    while isNumStr != '':
        nums.append(eval(isNumStr))
        isNumStr = input("请输入数字（回车退出）")
    return nums

# 计算平均值
def mean(numbers):
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers)

# 计算标准差
def dev(numbers, mean):
    sdev = 0.0
    for num in numbers:
        sdev = (num - mean) ** 2 + sdev
    return pow(sdev / (len(numbers) - 1), 0.5)

# 计算中位数
def median(numbers):
    new = sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        return (new[size //2 - 1] + new[size//2]) / 2
    else:
        return new[size//2]
n = getNum()
print(n)
m =mean(n)

print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m, dev(n, m), median(n)))
