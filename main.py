from turtle import *

screen = Screen()
screen.setup(400,400)
screen.bgcolor('#E6A6A6')

penup()
goto(0,100)
color('#8181E3')
style = ('Times', 40, 'bold')
write('HELLO', font=style, align='center')
right(90)
forward(60)
color('#EDED87')
write('WORLD', font=style, align='center')
hideturtle()