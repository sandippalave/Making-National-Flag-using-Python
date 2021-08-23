from turtle import *
import winsound

winsound.PlaySound(r'C:\Users\SANDIP\Downloads\jana_gana_mana.wav',winsound.SND_ASYNC)



def rectangle(color):
    begin_fill()
    fillcolor(color)
    for i in range(2):
        forward(400)
        right(90)
        forward(90)
        right(90)
    end_fill()


up()
pensize(2)
goto(-100, -300)
down()
goto(-100, 300)
rectangle("orange")
goto(-100, 210)
forward(200)
color("blue")
circle(-45)
setheading(270)
forward(45)
setheading(0)
for i in range(24):
    forward(45)
    bk(45)
    left(15)

setheading(90)
forward(45)
setheading(0)
color("black")
forward(200)
right(90)
forward(90)
right(90)
forward(400)
right(90)
forward(90)
right(90)

goto(-100, 120)
rectangle("green")

text = Turtle()

text.hideturtle()

def write(msg, pos, color):
    x,y = pos
    text.goto(x,y)
    text.color(color)
    text.penup()
    style = ('Courier',30,'italic')
    text.write(msg, font=style)

right(90)
forward(100)
color("white")
text.penup()
goto(-80,-80)

write('Happy',(-80,-80), 'orange')
color("white")
goto(30,-110)
write('Ind',(30,-110),'red')
color("white")
write('epen',(100,-110),'yellow')
color("white")
write('dent',(150,-110),'blue')
color("white")
write('Day',(70,-160),'green')
color("white")
