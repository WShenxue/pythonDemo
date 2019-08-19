# coding:utf-8
import turtle as t

t.title("自动轨迹绘制")
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)

# 数据读取
datas = []
f = open("data.txt")
for line in f:
    line = line.replace("\n", "")
    datas.append(list(map(eval, line.split(","))))
f.close()
# 自动绘制
for i in range(len(datas)):
    t.pencolor(datas[i][3], datas[i][4], datas[i][5])
    t.fd(datas[i][0])
    if datas[i][1]:
        t.right(datas[i][2])
    else:
        t.left(datas[i][2])
t.done()

# 300,0,144,1,0,0
# 300:行进距离，1:转向判断（0：左转，1：右转）,144:转向角度1,0,0:RGB三个通道颜色，0~1之间浮点数
