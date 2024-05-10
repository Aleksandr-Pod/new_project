from turtle import *
from time import sleep

n = int(input("Сколько сторон:"))
angle = int(input("угол фигуры:"))
i = 0
y = 0
while y < 3:
    while i < n:
        forward (80)
        left (angle)
        i = i + 1
    sleep(1)
    left(120)
    i = 0
    y = y + 1

exitonclick ()