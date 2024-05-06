from turtle import *
from time import sleep

n = int(input("Сколько сторон:"))
angle = int(input("угол фигуры:"))
i = 0
y = 0

width(5)
color("blue")
while y < 12:
    while i < n:
        forward (80)
        left (angle)
        i = i + 1
    # sleep(0.5)
    left(30)
    i = 0
    y = 1 + y

exitonclick ()