from turtle import *

speed(0)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
angles = [3,4,5,6,7]


def angle(n):
    for a in range(n):
        forward(100)
        left(360/n)


for a, b in zip(colors, angles):
    color(a)
    angle(b)

mainloop()