from turtle import Turtle,Screen
turtles = Turtle()
screen = Screen()
screen.listen()
def forwardkey():
    turtles.forward(100)
def backwardkey():
    turtles.backward(100)
def counter_clock():
    new_angle = turtles.heading()+10
    turtles.setheading(new_angle)
def anti_clock():
    new_angle = turtles.heading()-10
    turtles.setheading(new_angle)

def clear():
    turtles.clear()
    turtles.penup()
    turtles.home()
    turtles.pendown()
screen.onkey(key="f",fun=forwardkey)
screen.onkey(key="b", fun=backwardkey)
screen.onkey(key="r", fun=counter_clock)
screen.onkey(key="a", fun=anti_clock)
screen.onkey(key="c", fun=clear)

screen.exitonclick()



