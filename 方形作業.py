import turtle

def drew_square(t,size):
    for i in range(4):
        t.forward(size)
        t.left(90)

wn=turtle.Screen()
wn.bgcolor("lightgreen")

john=turtle.Turtle()
john.color("hotpink")

for i in range(5):
    drew_square(john,30)
    john.penup()
    john.forward(50)
    john.pendown()

window.exitonclick()
    
    
