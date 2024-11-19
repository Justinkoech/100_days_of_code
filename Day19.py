#event listeners
from turtle import Turtle ,Screen
rex = Turtle()
screen = Screen()

def move_forwards():
    rex.forward(10)


screen.listen()
screen.onkey(move_forwards,"space")

screen.exitonclick()
