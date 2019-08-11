# -*- coding:utf-8 -*-
import turtle

def koch(size, n):
    if n == 0:
        # 0阶：即绘制直线
        turtle.fd(size)
    else :
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)

# 3阶科赫曲线绘制
def main():
    turtle.setup(800, 400)
    turtle.penup()
    turtle.goto(-200, -50)
    turtle.pendown()
    turtle.pensize(2)
    koch(600, 3)
    turtle.hideturtle()

# 3阶科赫雪花绘制
def main2():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    # turtle.hideturtle()
    # turtle.done()

# main()
main2()