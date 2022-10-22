from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color(color)
        self.penup()
        self.goto(position)

    def up(self):
        x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(x, new_y)

    def down(self):
        x = self.xcor()
        new_y = self.ycor() - 20
        self.goto(x, new_y)
