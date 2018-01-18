from turtle import Turtle

p = Turtle()
p.speed(2)
p.pensize(5)
p.color("black","red")
p.begin_fill()
for i in range(5):
    p.forward(500)
    p.right(144)
p.end_fill()
