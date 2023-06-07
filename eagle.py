###     By Bang Bejo    ###

# You may modify the program
# There are no limits for you in your work 

from turtle import *
from time import sleep

bgcolor("black")
t = [Turtle(), Turtle()]
x = 5

colors = ["red", "blue", "orchid", "cyan"]
for index, i in enumerate(t):
    i.speed(0.1)
    i.color("white")
    i.shape("circle")
    i.shapesize(0.3)
    i.width(3)
    i.pu()
    i.seth(90)
    i.fd(360)
    i.seth(-180)
    i.pd()
t[0].pu()

delay(0)
speed(0)
ht()
sleep(2)

for i in colors:
    color(i)
    for i in range(180):
        t[0].fd(x)
        t[0].lt(1)
        pu()
        goto(t[0].pos())
        pd()
        t[1].fd(2 * x)
        t[1].lt(2)
        goto(t[1].pos())
done()
