from turtle import Turtle

FONT = ('Courier', 24, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score1 = 0
        self.score2 = 0
        self.update()

    def update(self):
        self.goto(-190, 260)
        self.write(f"Player A: {self.score1}", font=FONT)
        self.goto(40, 260)
        self.write(f"Player B: {self.score2}", font=FONT)

    def point1(self):
        self.clear()
        self.score1 += 1
        self.update()

    def point2(self):
        self.clear()
        self.score2 += 1
        self.update()

