from turtle import Turtle

Move_distance=20

class Snake:
    def __init__(self):
        self.all_turtles=[]
        self.create_snake()
        self.head=self.all_turtles[0]

    def create_snake(self):
        x_value=0
        for i in range(3):
            baba=Turtle("square")
            baba.color("white")
            baba.penup()
            baba.goto(x=x_value,y=0)
            x_value-=20
            self.all_turtles.append(baba)

    def move(self):
        for i in range(len(self.all_turtles)-1,0,-1):
            new_x=self.all_turtles[i-1].xcor()
            new_y=self.all_turtles[i-1].ycor()
            self.all_turtles[i].goto(x=new_x,y=new_y)
        self.all_turtles[0].forward(Move_distance)
  
    def up(self):
        if self.head.heading() !=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    
    def right(self):
        if self.head.heading() !=180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    
    def big(self):
        new =Turtle("square")
        new.penup()
        new.color("white")
        new.goto(self.all_turtles[-1].position())
        self.all_turtles.append(new)