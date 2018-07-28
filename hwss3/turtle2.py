from turtle import *

speed(0)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']


def rectangle():
    for _ in range(2):
        forward(50)
        left(90)
        forward(80)
        left(90)
    forward(50)

for _ in colors:
    begin_fill()
    color('white', _)
    rectangle()
    end_fill()


mainloop()