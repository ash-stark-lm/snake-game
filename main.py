from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import  Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# tim = Turtle()# only one object banaye mistake
# create snake

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    #in turtle class distance method works by comparing the distance from this turtle to whatever we give
        # inside the paranthesis

    if snake.head.distance(food) < 15: # our food is 10 by 10 so thoda buffer diye 15 pixel
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    #detect collision with wall

    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


# with open("scores.txt") as my_scores:




screen.exitonclick()
