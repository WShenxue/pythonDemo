# -*- cofing:utf-8 -*-

import turtle


def curveMove():
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.penup()
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(90)
    turtle.circle(24, 180)
    turtle.circle(72, 70)
    turtle.left(38)
    turtle.circle(72, 70)
    turtle.circle(24, 180)
    turtle.end_fill()


def forHadi():
    turtle.speed(5)
    # 脸
    turtle.setup(800, 700)
    turtle.pensize(2)
    turtle.circle(100)
    # 右眉毛
    turtle.up()
    turtle.goto(-60, 130)
    turtle.down()
    turtle.seth(45)
    turtle.circle(-30, 90)

    # 左眉毛
    turtle.up()
    turtle.goto(60, 130)
    turtle.down()
    turtle.seth(135)
    turtle.circle(30, 90)

    # 鼻子
    turtle.up()
    turtle.goto(0, 80)
    turtle.seth(0)
    turtle.down()
    turtle.pencolor("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.pencolor("black")

    # 嘴巴
    turtle.up()
    turtle.goto(-40, 60)
    turtle.seth(-80)
    turtle.down()
    turtle.circle(40, 160)

    turtle.up()
    turtle.goto(0, 0)
    turtle.seth(0)
    turtle.down()
    turtle.right(90)
    turtle.fd(200)

    turtle.left(45)
    turtle.fd(120)
    turtle.penup()
    turtle.fd(-120)
    turtle.pendown()
    turtle.right(90)
    turtle.fd(120)
    turtle.left(45)
    turtle.penup()
    turtle.goto(0, -80)
    turtle.pendown()
    turtle.left(90)
    turtle.fd(120)

    turtle.left(45)
    turtle.fd(60)
    turtle.right(45)
    turtle.up()
    turtle.goto(0, -95)
    turtle.down()
    turtle.fd(120)
    turtle.right(45)
    turtle.fd(60)
    turtle.left(45)

    # 画心
    turtle.up()
    turtle.goto(250, -60)
    turtle.down()
    curveMove()

    # 文字
    turtle.up()
    turtle.goto(20, -65)
    turtle.pencolor("purple")
    turtle.write("to Hadi ~", font=("Arial", 14, "normal"))
    turtle.down()

    turtle.up()
    turtle.goto(-300, -100)
    turtle.write("~*.*~ 情人节快乐！！！", font=("微软雅黑", 20, "normal"))

    turtle.up()
    turtle.goto(150, -250)
    # turtle.down()
    turtle.pencolor("black")
    turtle.write("~~~^_^~~~", font=("微软雅黑", 20, "normal"))

    turtle.up()
    turtle.goto(-200, 250)
    turtle.write("惊不惊喜，意不意外，哈哈~~~", font=("微软雅黑", 20, "normal"))

    turtle.ht()

    turtle.done()

forHadi()

# curveMove()


