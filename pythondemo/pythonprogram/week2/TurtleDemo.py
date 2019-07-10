import turtle
#绘制风车
for i in range(4):
    turtle.seth((i + 1)*90)
    turtle.fd(150)
    turtle.seth(i * 90)
    turtle.circle(-150, 45)
    turtle.goto(0, 0)
turtle.done()





# 绘制Z
# turtle.left(45)
# turtle.fd(150)
# turtle.right(135)
# turtle.fd(300)
# turtle.left(135)
# turtle.fd(150)
