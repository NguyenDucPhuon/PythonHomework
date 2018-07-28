from turtle import *

speed(0)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
angles = [3, 4, 5, 6, 7]


def angle(n):
    rotate = 360/n
    for _ in range(n):
        forward(100)
        left(rotate)


for a, b in zip(colors, angles):
    color(a)
    angle(b)

mainloop()