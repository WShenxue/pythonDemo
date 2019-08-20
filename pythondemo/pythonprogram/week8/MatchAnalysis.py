# coding: utf-8

from random import random


# 打印提示信息
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")


# 获取输入
def getInputs():
    a = eval(input("请输入选手A的能力值(0-1)："))
    b = eval(input("请输入选手B的能力值(0-1)："))
    n = eval(input("模拟比赛的场次："))
    return a, b, n


# 判断比赛是否结束
def gameOver(scoreA, scoreB):
    return scoreA == 15 or scoreB == 15


# 模拟一场比赛
def simOnegame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = 'A'
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = 'A'
    return scoreA, scoreB


# 模拟比赛
def simGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOnegame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


# 输入总结果
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("x选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA / n))
    print("x选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB / n))


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simGames(n, probA, probB)
    printSummary(winsA, winsB)

main()