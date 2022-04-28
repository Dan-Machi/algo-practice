from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, body_position):
        super().__init__()
        self.body_position = body_position
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.color("red")
        self.create_food()

    def create_food(self):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        if (x, y) in self.body_position:
            return self.create_food()
        self.goto(int(x), int(y))