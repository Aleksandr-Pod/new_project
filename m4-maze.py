
from turtle import*
speed(6)
width(2)

forward(100)
penup()
goto(20,20)
pendown()
forward(40)
penup()
goto(80,20)
pendown()
forward(40)
penup()
goto(40,40)
pendown()
forward(40)
penup()
goto(0,80)
pendown()
forward(20)
penup()
goto(60,80)
pendown()
forward(20)
penup()
goto(20,100)
pendown()
forward(80)
penup()
goto(20,120)
pendown()
forward(100)
right(90)
forward(120)
penup()
goto(0,120)
pendown()
forward(120)
penup()
goto(20,120)
pendown()
forward(20)
penup()
goto(40,100)
pendown()
forward(60)
penup()
goto(100,100)
pendown()
forward(20)
penup()
goto(20,80)
pendown()
forward(60)
penup()
goto(60,80)
pendown()
forward(20)
penup()
goto(80,80)
pendown()
forward(40)
penup()
goto(100,60)
pendown()
forward(40)
color('red')
penup()
goto(10, 130)
pendown()
while True:
    s = input('Куди йти?')
    if 's' == s:
        forward(20)
    elif 'w' == s:
        left(180)
        forward(20)
        left(180)
    elif 'd' == s:
        left(90)
        forward(20)
        right(90)
    elif 'a' == s:
        right(90)
        forward(20)
        left(90)

exitonclick()