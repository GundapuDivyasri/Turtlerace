from turtle import Turtle,Screen
turt = Turtle()
screen = Screen()
def move_f():
    turt.forward(10)

screen.listen()
screen.onkey(key="a" , fun=move_f)
screen.exitonclick()