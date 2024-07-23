from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake=Snake()
food=Food()
score=Scoreboard()
# location =food.fruit()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.big()
        score.update()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on=False
        score.game_over()

    for i in snake.all_turtles[1:]:
        if snake.head.distance(i) <=10:
            score.game_over()
            is_game_on=False
screen.exitonclick()