from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for key presses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 280 or snake.head.xcor() < -280
        or snake.head.ycor() > 280 or snake.head.ycor() < -280
    ):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# Exit game on click
screen.exitonclick()
