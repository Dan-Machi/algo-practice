from turtle import Turtle
from food import Food
import time
SEGMENT_SIZE = 20
WINDOW_SIZE = 600


class Snake:

    def __init__(self, screen):
        self.screen = screen
        self.head = Turtle("square")
        self.head.penup()
        self.head.color("white")
        self.head.speed(0)
        self.body_position = [self.head.position()]
        self.snake_body = [self.head]
        self.create_border()
        self.create_snake()
        self.food = Food(self.body_position)
        self.start_game()

    def create_snake(self):
        for i in range(0, 3):
            t = Turtle("square")
            t.speed(1)
            t.penup()
            t.color("white")
            t.setx(self.snake_body[i].xcor() - SEGMENT_SIZE)
            self.snake_body.append(t)
            self.body_position.append(t.position())

    def create_border(self):
        t = Turtle("square")
        t.speed(0)
        t.penup()
        t.color("white")
        t.goto(-WINDOW_SIZE / 2, WINDOW_SIZE / 2)
        t.speed(0)
        for _ in range(0, 4):
            for _ in range(0, int(WINDOW_SIZE / SEGMENT_SIZE)):
                t.forward(SEGMENT_SIZE)
                t.stamp()
            t.right(90)

    def write_score(self, score, turtle):
        text = turtle
        text.clear()
        text.hideturtle()
        text.penup()
        text.color("white")
        text.goto(-300, 320)
        text.write(f"score: {score}", font=("Arial", 30, "normal"))

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def start_game(self):
        game_is_on = True
        score = 0
        text = Turtle()
        while game_is_on:
            self.write_score(score, text)
            text.write(f"score: {score}", font=("Arial", 30, "normal"))
            self.screen.update()
            speed = 0.2 - 0.003 * score
            time.sleep(speed)
            self.screen.onkey(key="Up", fun=self.up)
            self.screen.onkey(key="Down", fun=self.down)
            self.screen.onkey(key="Right", fun=self.right)
            self.screen.onkey(key="Left", fun=self.left)
            self.screen.update()
            self.head.forward(SEGMENT_SIZE)
            self.body_position.insert(0, (round(self.head.xcor()), round(self.head.ycor())))
            for i in self.body_position[1:]:
                if i == self.body_position[0]:
                    game_is_on = False
                    print(f"Game Over! Your score is {score}")
            for i in range(1, len(self.snake_body)):
                self.snake_body[i].setposition(self.body_position[i - 1])
            if self.body_position[0][0] == self.food.xcor() and self.body_position[0][1] == self.food.ycor():
                t = Turtle("square")
                t.speed(1)
                t.penup()
                t.color("white")
                self.snake_body.append(t)
                self.snake_body[len(self.snake_body) - 1].setposition(self.body_position[len(self.body_position) - 2])
                self.food.create_food()
                score += 1
            else:
                del self.body_position[len(self.snake_body)]
            if self.body_position[0][0] < -280 or self.body_position[0][0] > 280 or self.body_position[0][1] < -280 or self.body_position[0][1] > 280:
                game_is_on = False
                print(f"Game Over! Your score is {score}")
