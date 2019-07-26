# -*- coding:utf-8 -*-
# 数码管显示日期

import turtle, time


def drawLine(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)


def drawDigit(digit):
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawDate(date):
    for i in date:
        if i == '+':
            turtle.pencolor("blue")
            turtle.write('年', font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == '-':
            turtle.pencolor("green")
            turtle.write('月', font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == '=':
            turtle.pencolor("purple")
            turtle.write('日', font=("Arial", 18, "normal"))
            turtle.fd(40)
        else:
            turtle.pencolor("red")
            drawDigit(eval(i))


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime("%Y+%m-%d=", time.gmtime()))
    turtle.hideturtle()
    turtle.done()


def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)

main()
