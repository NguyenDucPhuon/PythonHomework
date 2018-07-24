from turtle import *

speed(0)

def angle(n):

    for a in range(n):

        forward(100)

        left(360/n)


for i in range(3, 7):

    if i % 2 == 0:

        color("red")

        angle(i)

    else:

        color("blue")

        angle(i)

    print(i)


mainloop()
