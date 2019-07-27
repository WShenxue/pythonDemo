# -*- cofing:utf-8 -*-

import turtle

# turtle.setup()

def rightAngle(length):
    turtle.left(45)
    turtle.fd(length)
    turtle.penup()
    turtle.fd(-length)
    turtle.pendown()
    turtle.right(90)
    turtle.fd(length)
    turtle.left(45)

def curveMove():
    turtle.pencolor("red")
    turtle.fillcolor("pink")
    turtle.speed(5)
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
    turtle.circle(100)

    # turtle.goto(0, 0)
    turtle.right(90)
    turtle.fd(200)
    rightAngle(120)
    turtle.penup()
    turtle.goto(0, -80)
    turtle.pendown()
    turtle.left(90)
    turtle.fd(120)
    # rightAngle(60)

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
    # 文字
    turtle.up()
    turtle.goto(20, -50)
    turtle.write("to Hadi ~", font=("Arial", 14, "normal"))
    turtle.down()

    # 画心
    turtle.up()
    turtle.goto(250, -60)
    turtle.down()
    curveMove()

    turtle.done()

forHadi()

# curveMove()


