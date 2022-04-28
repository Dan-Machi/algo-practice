from turtle import Turtle, Screen
from math import isclose
import random

screen = Screen()
screen.setup(700, 700)
screen.tracer(0)
screen.bgcolor("black")
step_size = 20
draw = Turtle()
draw.hideturtle()
draw.speed(0)
draw.color("white")
draw.pensize(step_size - step_size/10)
check = Turtle()
check.hideturtle()
check.speed(0)
check.penup()
path = []

border = Turtle()
border.hideturtle()
border.penup()
border.goto(-300, 300)
for _ in range(0, 4):
    for _ in range(0, int(600/step_size)):
        path.append((border.xcor(), border.ycor()))
        border.forward(step_size)
    border.right(90)

path.append((0, 0))


def direction():
    rnd = random.randint(0, 3)
    if rnd == 0:
        if round(draw.heading()) == 180:
            return direction()
        draw.setheading(0)
        check.setheading(0)
    if rnd == 1:
        if round(draw.heading()) == 270:
            return direction()
        draw.setheading(90)
        check.setheading(90)
    if rnd == 2:
        if round(draw.heading()) == 0:
            return direction()
        draw.setheading(180)
        check.setheading(180)
    if rnd == 3:
        if round(draw.heading()) == 90:
            return direction()
        draw.setheading(270)
        check.setheading(270)


create_path = True


def direction_check():
    for i in reversed(path):
        if i == path[4*(int(600/step_size))]:
            return False
        if not (round(i[0]) + step_size, round(i[1])) in path or not (round(i[0]) - step_size, round(i[1])) in path \
                or not (round(i[0]), round(i[1]) + step_size) in path or not (round(i[0]), round(i[1]) - step_size) in path:
            draw.penup()
            draw.goto(i[0], i[1])
            draw.pendown()
            check.goto(i[0], i[1])
            break


while create_path:
    if (round(check.xcor()) + step_size, round(check.ycor())) in path and (round(check.xcor()) - step_size, round(check.ycor())) in path and (round(check.xcor()), round(check.ycor()) + step_size) in path and (round(check.xcor()), round(check.ycor()) - step_size) in path:
        if direction_check() is False:
            print(path)
            create_path = False
    direction()
    check.forward(step_size)
    if (round(check.xcor()), round(check.ycor())) in path:
        check.backward(step_size)
        continue
    if round(check.xcor()) >= 300 or round(check.xcor()) <= -300 or round(check.ycor()) >= 300 or round(check.ycor()) <= -300:
        check.backward(step_size)
        continue
    screen.tracer(1)
    draw.goto(round(check.xcor()), round(check.ycor()))
    # draw.write((round(check.xcor()), round(check.ycor())), font=("Arial", 7, "normal"))
    path.append((round(draw.xcor()), round(draw.ycor())))
    screen.tracer(0)

screen.update()
screen.exitonclick()
