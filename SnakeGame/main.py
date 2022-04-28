import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.listen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake(screen)


