from turtle import Turtle, Screen
import random
screen = Screen()
turtles = Turtle()
turtles.hideturtle()
screen.setup(700, 700)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["violet", "yellow", "green", "red", "blue", "orange"]
pos_y = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(6):
    turtles = Turtle(shape="turtle")
    turtles.color(colors[i])
    turtles.penup()
    turtles.goto(x=-330, y=pos_y[i])
    all_turtles.append(turtles)
game = False
if bet:
    game = True
while game:
    for turtle in all_turtles:
        if turtle.xcor() > 330:
            game = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You won the bet.The {winner} turtle is the winner.")
            else:
                print(f"You have lost the bet.The {winner} turtle is the winner.")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
