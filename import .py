import turtle

t = turtle.Turtle()
t.speed(50)
turtle.bgcolor("white")

colors = ["red", "blue", "green", "black", "orange"]

t.width(1)

for i in range(50):
    t.color(colors[i % len(colors)])
    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.right(140)
    t.end_fill()
    t.right(3)

turtle.done()